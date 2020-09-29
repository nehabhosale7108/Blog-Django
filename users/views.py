from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from . import serializer
from .models import User
from .serializer import UserSignUpSerializer, UserLoginSerializer


class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj = User.objects.get(email=request.data["email"])

            response_data={
                "id":obj.id,
                "first_name":obj.first_name,
                "username":obj.username,
                "password":obj.password,

            }
            return Response(response_data)
        else:
            return Response(serializer.errors)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("Request Data", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.user

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.first_name,
                "username": obj.username,

            }
            return Response(response_data)
        else:
            return Response("somthing went wrong")
# serializer.errors