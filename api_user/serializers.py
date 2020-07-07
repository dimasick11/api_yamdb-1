
from rest_framework import serializers
from .models import User

from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
      class Meta:
            fields = ('username', 'id', 'first_name', 'last_name', 'email', 'role', 'bio')
            model = User