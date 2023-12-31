from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateUserSerializer, UpdateUserSerializer, LoginSerializer
from knox import views as knox_views
from django.contrib.auth import login
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UpdateUserAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            login(request, user)
            response = super().post(request, format=None)
            klass = user.klass_set.first()
            if klass:
                response.data["class_id"] = klass.id

        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(response.data, status=status.HTTP_200_OK)
