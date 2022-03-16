from celery import Celery
from celery.utils.log import get_task_logger
from kombu import Exchange, Queue

from app.Settings.config import settings

logger = get_task_logger(__name__)

app = Celery(name="app_celery_name", broker=settings.RABBITMQ_URL, backend=settings.CELERY_BACKEND)

main_exchange = Exchange(name="my_exchange", type="direct", durable=True)


class Config:
    enable_utc = True
    broker_connection_max_retries = 100
    imports = ["app.Tasks.Process_image", "app.Tasks.Process_text"]
    tasks_queues = [
        Queue("identify_animal", exchange=main_exchange, routing_key="identify_animal"),
        Queue("process_text", exchange=main_exchange, routing_key="process_text"),
    ]
    result_extended = True
    database_engine_options = {"echo": True}
    database_table_schemas = {"task": "celery", "group": "celery"}
    data_base_table_names = {"task": "myapp_taskmeta", "group": "myppa_groupmeta"}


app.config_from_object(Config)
