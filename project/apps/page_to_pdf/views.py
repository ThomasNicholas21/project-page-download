from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import collect_pages


class PageDownloadView(APIView):
    def post(self, request, *args, **kwargs):
        list_urls = request.data.get("list_urls")
        collect_pages.delay(list_urls)
        return Response(
            {"initialize": "the collection has been initialized."},
            status=status.HTTP_201_CREATED
        )
