from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost:6379', include=['matrix_tasks'])