from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model

from timetable.models import Klass

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name")


class CreateUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    program = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "program"]

    def validate(self, attrs):
        email = attrs.get("email", "").strip().lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email id already exists.")

        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        program_id = int(validated_data.pop("program"))
        print("validated_data")
        print(validated_data)

        password = validated_data.pop("password1")
        user = User.objects.create_user(
            **validated_data,
            password=password,
        )
        # creating membership
        klass = Klass.objects.get(id=program_id)
        klass.members.add(user)
        klass.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email").lower()
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Please give both email and password.")

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email does not exist.")

        user = authenticate(
            request=self.context.get("request"), email=email, password=password
        )
        if not user:
            raise serializers.ValidationError("Wrong Credentials.")

        attrs["user"] = user
        return attrs
