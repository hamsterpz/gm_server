from rest_framework.views import APIView, exception_handler as _exception_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework.response import Response

from . import exceptions
from .response import make_response

__all__ = ["CoreAPIView", "JWTAPIView"]


def exception_handler(exc, context):
    _ = context
    r = _exception_handler(exc, context)

    if isinstance(r, Response):
        msg = r.data.get("detail", "ok")
        r = make_response(
            code=r.status_code,
            msg=msg,
            data=r.data,
            status_code=r.status_code
        )
        return r

    if isinstance(exc, exceptions.ClientError):
        r = make_response(
            code=exc.code,
            msg=exc.msg,
            status_code=exc.status_code
        )
    return r


class CoreAPIView(APIView):

    def get_exception_handler(self):
        return exception_handler

    @staticmethod
    def make_response(*args, **kwargs):
        return make_response(*args, **kwargs)


class JWTAPIView(CoreAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
