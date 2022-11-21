import asyncio
import logging

from api.connection_manager import ConnectionManager
from api.constants import DEFAULT_QUEUE_NAME
from api.settings import settings

logger = logging.getLogger(__name__)


async def main() -> None:
    connection_manager = ConnectionManager(settings.RABBITMQ_URL, DEFAULT_QUEUE_NAME)
    await connection_manager.consume_message()
    logger.info("Listener services started")


if __name__ == "__main__":
    asyncio.run(main())
