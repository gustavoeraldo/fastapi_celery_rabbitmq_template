from sqlalchemy.orm import Session
from celery import Task

from app.Core.celery_app import app, logger


class MyCustomTask2(Task):
    def on_failure(self, exc, task_id, args, kwargs, info):
        """
        exc: Exception;
        task_id: str
        args: tuple
        """
        # Do some custom steps
        pass

    def on_success(self, retval, task_id, args, kwargs):
        # Do some custom steps
        pass


@app.task(
    name="translate-text", bind=True, default_retry_delay=1 * 10, base=MyCustomTask2
)
def translate_text(self, data):
    logger.info(f"Translating text task {self.id}")
    # Add some processing
    return


@app.task(
    name="identify-emotion", bind=True, default_retry_delay=1 * 10, base=MyCustomTask2
)
def identify_emotion(self, data):
    logger.info(f"Identifying text emotion, task_id = {self.id}")
    # Add some processing
    return
