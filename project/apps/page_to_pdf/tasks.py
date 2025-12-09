from celery import shared_task


@shared_task
def collect_pages(list_urls):
    ...
