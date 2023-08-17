from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstprojectReactJs.settings')

app = Celery('FirstprojectReactJs')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def my_task():
    prin('Task logic ')
    
app.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'appreact.tasks.get_and_insert_new_data',
        'schedule': crontab(minute='*/1'),
    },
}

app.autodiscover_tasks()