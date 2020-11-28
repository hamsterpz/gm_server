from rest_framework import status

__all__ = [
    "ClientError",
    "ClientErrorCodeCol",
    "ParamsError"
]

DEFAULT_CODE = 0
DEFAULT_MSG = "ok"


class BaseClientErrorCode:
    def __init__(self, code, msg, status_code=status.HTTP_200_OK):
        self.code = code
        self.msg = msg
        self.status_code = status_code


class ClientErrorCodeCol:
    """自定义的错误码集合
    """
    INVALID_PARAMS = BaseClientErrorCode(1, "参数错误", status.HTTP_422_UNPROCESSABLE_ENTITY)


class ClientError(Exception):
    error_code = None

    def __init__(self, code=None, msg=None, status_code=None, error_code_ins=None):
        # 初始化错误码
        self.init_error_code()

        if code is not None:
            self.code = code
        if msg is not None:
            self.msg = msg
        if status_code is not None:
            self.status_code = status_code

        # 如果输入了参数 error_code_ins 那么久用这个的
        self.load_error_code_ins(error_code_ins)

        assert self.status_code is not None

    def init_error_code(self):
        self.load_error_code_ins(self.error_code)

    def load_error_code_ins(self, error_code_ins: BaseClientErrorCode):
        if isinstance(self.error_code, BaseClientErrorCode):
            self.code = error_code_ins.code
            self.status_code = error_code_ins.status_code
            self.msg = error_code_ins.msg


class ParamsError(ClientError):
    error_code = ClientErrorCodeCol.INVALID_PARAMS
