from rest_framework.response import Response
from rest_framework import status

from . import exceptions

__all__ = ["CoreResponse", "make_response"]


class CoreResponse(Response):
    pass


def make_response(
        data=None,
        code=exceptions.DEFAULT_CODE,
        msg=exceptions.DEFAULT_MSG,
        status_code=status.HTTP_200_OK,
        **kwargs
):
    """返回response对象
    参数:
      - data: 数据
      - code: 自定义的状态码
      - msg: 消息内容
      - status_code: http状态码
    """
    body = dict(
        data=data,
        code=code,
        msg=msg
    )
    body.update(kwargs)

    r = CoreResponse(body, status=status_code)
    return r
