import asyncio
import logging

import aio_pika

logger = logging.getLogger(__name__)


class ConnectionManager:
    def __init__(self, rabbitmq_url: str, queue_name: str):
        self.rabbitmq_url = rabbitmq_url
        self.queue_name = queue_name

    async def send_message(self, message: str):
        connection = await aio_pika.connect_robust(self.rabbitmq_url)
        queue_name = self.queue_name
        async with connection:
            routing_key = queue_name

            channel = await connection.channel()

            await channel.default_exchange.publish(
                aio_pika.Message(body=message.encode()),
                routing_key=routing_key,
            )

    async def consume_message(self):
        while True:
            try:
                connection = await aio_pika.connect_robust(self.rabbitmq_url)
                break
            except ConnectionError:
                logger.info("waiting for connection")
                await asyncio.sleep(5)
        queue_name = self.queue_name
        async with connection:
            # Creating channel
            channel = await connection.channel()

            # Will take no more than 10 messages in advance
            await channel.set_qos(prefetch_count=10)

            # Declaring queue
            queue = await channel.declare_queue(queue_name, auto_delete=True)

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        print(message.body)  # noqa

                        if queue.name in message.body.decode():
                            break
