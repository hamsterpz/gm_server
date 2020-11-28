from django.db import transaction

from .models import Payment
from core import services


class PaymentService(services.Service):
    payment_class = Payment

    def fetch(self, user, page, num):
        pass

    def create_payment(self, user, price, desc, platform_id):
        transaction.on_commit()

