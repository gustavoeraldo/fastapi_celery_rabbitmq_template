from fastapi import APIRouter
from celery.result import AsyncResult

from app.Tasks.Process_image import identify_dogs, identify_cats
from app.Core.celery_app import logger

router = APIRouter()

# Example of sending a task and not waiting for it's result
@router.post("/dogs")
async def identify_dogs_in_image():
    """This endpoint identifies dogs in an image and runs in background."""
    image = "dogs"

    try:
        identify_dogs.apply_async(queue="identify_animal", args=(image), retry=True)
    except identify_dogs.OperationationalError as exc:
        logger.exception(f"Sending task raised. Error: {exc}")

    return {"message": "Image is being processed."}


# Example of sending a task and waiting for it's result
@router.post("/cats")
async def identify_cats_in_image():
    """This endpoint identifies cats in an image and waits for the identification process."""
    image = "cats"

    try:
        task_result = identify_cats.apply_async(
            queue="identify-animal", args=(image), retry=True
        )
        status = AsyncResult(task_result.id).get()
    except identify_cats.OperationationalError as exc:
        logger.exception(f"Sending task raised. Error: {exc}")

    return {"result": status}
