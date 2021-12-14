from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


# UI 설정부분
from rest_framework.views import APIView

from accountapp.models import NewModel
from accountapp.permissions import IsOwner
from accountapp.serializers import NewModelSerializer, UserSerializer, UserWithoutPasswordSerializer


def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리 부분
@api_view(['GET','POST'])
def hello_world(request):

    if request.method == "POST":
        input_data = request.data.get('input_data')

        new_model = NewModel()
        new_model.text = input_data
        new_model.save()

        # Serialize 하는 부분
        serializer = NewModelSerializer(new_model)

        return Response(serializer.data)

    new_model_list = NewModel.objects.all()
    serializer = NewModelSerializer(new_model_list, many=True)

    return Response(serializer.data)

def AccountCreateTemplate(request):
    return render(request, 'accountapp/create.html')

class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

def AccountLoginView(request):
    return render(request, 'accountapp/login.html')


class AccountRetrieveTemplateView(TemplateView):
    template_name = 'accountapp/retrieve.html'

class AccountUpdateTemplateView(TemplateView):
    template_name = 'accountapp/update.html'


class AccountDestroyTemplateView(TemplateView):
    template_name = 'accountapp/destroy.html'



class AccountRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithoutPasswordSerializer

    permission_classes = [IsOwner]
    authentication_classes = [TokenAuthentication]