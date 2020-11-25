from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Event, Invitation, User, Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'picture', 'theme', 'teams', 'is_active')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'picture', 'announcement')

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('team', 'inviter', 'invitee_email', 'date_invited', 'code')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('team', 'name', 'start', 'end', 'details', 'invited', 'not_going', 'picture')

class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email', 'phone', 'picture', 'theme')