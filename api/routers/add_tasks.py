import logging

from fastapi import APIRouter

from api.constants import SwaggerTags
from api.schemas.add_task import AddTaskParameters
from api.services.base_service import service

logger = logging.getLogger(__name__)
router = APIRouter(tags=[SwaggerTags.ADD_TASKS])

# TODO connect to real DB
DB = 0


@router.post("/AddTasks")
async def add_tasks(args: AddTaskParameters):
    logger.info("Received a request to add tasks")
    await service.add_tasks(args)
    global DB
    DB += 1
    return {"status": "ok"}


@router.get("/GetStats")
def get_stats():
    logger.info("Received a request to get stats")
    return {"result": DB}
