import http
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from BancoDjangoLivre.models import User, Transfer
from .serializers import UserSerializer, TransferSerializer, AccountSerializer


class MainPage(APIView):
    http_method_names = ['get']

    def get(self, request):
        urls = {'Create User': 'create-user/',
                'User Detail': 'user/<str:cpf>/',
                'All Users': 'all-users/',
                'Bank Transfer': 'transfer/',
                'All Transfers': 'all-transfers/',
                'All User Transfers': 'transfer/<str:cpf>/',
                'Bank Account':'account/<str:id>/', }

        return Response(urls, status=http.HTTPStatus.OK)


class CreateUser(APIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', ]

    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(APIView):
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get(self, request):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSearch(APIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'patch']

    def get(self, request, pk):
        user = User.objects.filter(pk=pk)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateTransfer(APIView):
    serializer_class = TransferSerializer
    http_method_names = ['get', 'post']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            source_user = User.objects.get(cpf=request.data['source'])
            target_user = User.objects.get(cpf=request.data['target'])
            if (int(request.data['value']) > source_user.balance) or (source_user == target_user):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                source_user.balance = source_user.balance - int(request.data['value'])
                target_user.balance = target_user.balance + int(request.data['value'])
                target_user.save()
                source_user.save()
                serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)


class TransferViewSet(APIView):
    serializer_class = TransferSerializer
    http_method_names = ['get']

    def get(self, request):
        transfers = Transfer.objects.all()
        serializer = self.serializer_class(transfers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TransferSearch(APIView):
    serializer_class = TransferSerializer
    http_method_names = ['get']

    def get(self, request, id):
        user = Transfer.objects.filter(source=id)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountViewSet(APIView):
    serializer_class = AccountSerializer
    http_method_names = ['get']

    def get(self, request, id):
        user = User.objects.filter(cpf=id)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
