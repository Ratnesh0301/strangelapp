from dataclasses import field, fields
from rest_framework import serializers
from .models import Safepoints, User

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
#        fields = ('name','email','phone')
        fields = '__all__'


class safePointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Safepoints
        fields = '__all__'