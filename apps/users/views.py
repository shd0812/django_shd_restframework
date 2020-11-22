from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from apps.users import models
from apps.users.serializers import userinfoserializer, register_serializer

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['userid'] = self.user.id

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.

class MyLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 6


class UserInfoView(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.UserInfo.objects.all()
    serializer_class = userinfoserializer.UserInfoSerializers
    pagination_class = MyLimitOffsetPagination

    @action(detail=True)
    def add(self, request, *args, **kwargs):
        pass
        return Response('')

    @action(methods=['post'], detail=True)
    def display(self, request, *args, **kwargs):
        return Response("我是展示")

    # def get(self, request, *args, **kwargs):
    #
    #     query_set = self.get_queryset()
    #     page = self.paginate_queryset(query_set)
    #     ser = self.get_serializer(instance=page, many=True)
    #     return Response(page.get_paginated_response(ser.validated_data))
    #
    #
    # def post(self, request, *args, **kwargs):
    #     ser = userinfoserializer.UserInfoSerializers(data=request.data)
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
    #     return Response(ser.validated_data)


class RegisterView(CreateAPIView):
    serializer_class = register_serializer.RegisterSerializer


class UserValidView(APIView):

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        print(kwargs)
        print(username)
        dic = {
            'username': username,
            'count': User.objects.filter(username=username).count()
        }
        return Response(dic)
