from rest_framework import serializers
from api_user.models import UserBookActivity


class UserBookActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBookActivity
        fields = '__all__'
