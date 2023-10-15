from celery import shared_task

from api import send_to_parser


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='fetcher_mews:send_mews_object_to_parser')
def send_mews_object_to_parser(self, data: str):
    print('inside send_to_parser')
    send_to_parser.send_to_mews(data)
    print('data sent to parser')
    return 'success'
