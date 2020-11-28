from django.http.response import JsonResponse

from rest_framework import status


def make_response(code=0, data=None, msg="", status_code=status.HTTP_200_OK):
    """响应数据
    """
    r = JsonResponse({
        "code": code,
        "data": data if data else dict(),
        "msg": msg
    }, status=status_code)

    return r
