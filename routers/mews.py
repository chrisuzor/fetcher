from celery import group
from fastapi import APIRouter
from starlette.responses import JSONResponse

from api import send_to_parser
from celery_tasks.tasks import send_mews_object_to_parser
from config.celery_utils import get_task_info
from schemas.mews import MewsData

router = APIRouter(prefix='/mews', tags=['Mews'], responses={404: {"description": "Not found"}})


@router.post("/parse")
async def get_universities_async(data: MewsData):
    """
    Send data to Parser microservice
    """
    task = send_mews_object_to_parser.apply_async(args=[data])
    return JSONResponse({"task_id": task.id})


@router.get("/task/{task_id}")
async def get_task_status(task_id: str) -> dict:
    """
    Return the status of the submitted Task
    """
    return get_task_info(task_id)
