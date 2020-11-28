from rest_framework import serializers

from apps.payment import models


class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    price = serializers.DecimalField(10, 2)
    desc = serializers.CharField()
    username = serializers.CharField(source="user.username")

    class Meta:
        model = models.Payment
        fields = ("id", "price", "desc", "username")
