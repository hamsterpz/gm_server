from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

from core import exceptions, JWTAPIView, make_response
from .models import Payment
from .serializers import PaymentSerializer


def ignore_inspection_wrap(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)

    return inner


class TestView(JWTAPIView):

    class TestSerializer(serializers.Serializer):
        def update(self, instance, validated_data):
            pass

        def create(self, validated_data):
            pass

        page = serializers.IntegerField(required=True)
        num = serializers.IntegerField(required=True)

    @ignore_inspection_wrap
    def get(self, request: Request):
        s = self.TestSerializer(data=request.query_params)
        if not s.is_valid():
            raise exceptions.ParamsError()

        return self.make_response(s.validated_data)

    def post(self, request):
        raise exceptions.ParamsError()

    def handle_exception(self, exc):
        d = super(TestView, self).handle_exception(exc)
        print(exc)
        return d


class PaymentListView(ListAPIView):
    class _PageNumberPagination(PageNumberPagination):
        page_size_query_param = "page_size"
        max_page_size = 10

    authentication_classes = tuple()
    permission_classes = tuple()

    queryset = Payment.objects.order_by("-id").prefetch_related("user")
    serializer_class = PaymentSerializer
    pagination_class = _PageNumberPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id']

    def get(self, request, *args, **kwargs):
        d = super().get(request, *args, **kwargs)
        return make_response(data=d.data)

