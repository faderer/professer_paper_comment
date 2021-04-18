from django.shortcuts import render

# Create your views here.
import os
from django.http import HttpResponse, Http404


def media_file_download(request, file_path):
        with open(file_path, 'rb') as f:
            try:
                response = HttpResponse(f)
                response['content_type'] = "application/octet-stream"
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
            except Exception:
                raise Http404
