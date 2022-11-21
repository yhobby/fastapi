from typing import Dict

from pydantic import BaseModel


class AddTaskParameters(BaseModel):
    taskid: str
    description: str
    params: Dict[str, str]
