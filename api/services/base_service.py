import json
import logging

from api.connection_manager import ConnectionManager
from api.constants import DEFAULT_ROUTING_KEY
from api.schemas.add_task import AddTaskParameters
from api.settings import settings

logger = logging.getLogger(__name__)


class BaseService:
    async def add_tasks(self, args: AddTaskParameters) -> None:
        connection_manager = ConnectionManager(settings.RABBITMQ_URL, DEFAULT_ROUTING_KEY)
        await connection_manager.send_message(json.dumps(args.dict()))


service = BaseService()
