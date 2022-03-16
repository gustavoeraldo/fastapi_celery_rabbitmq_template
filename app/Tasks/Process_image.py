from celery import Task
import time

from app.Core.celery_app import app, logger


class MyCustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, info):
        """
        exc: Exception;
        task_id: str
        args: tuple
        """
        pass

    def on_success(self, retval, task_id, args, kwargs):
        pass


@app.task(
    name="identify-dogs", bind=True, default_retry_delay=1 * 10, base=MyCustomTask
)
def identify_dogs(self, image):
    logger.info(f"Identifying dogs image .Task_id: {self.id}, data: {image}")

    # simulating a process
    time.sleep(5)
    return "It's a dog"


@app.task(
    name="identify-dogs", bind=True, default_retry_delay=1 * 10, base=MyCustomTask
)
def identify_cats(self, image):
    logger.info(f"Identifying dogs image .Task_id: {self.id}, data: {image}")

    # simulating a process
    time.sleep(5)
    return "It's a cat"
