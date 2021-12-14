from django.urls import path
from django.views.generic import TemplateView

from accountapp.views import hello_world, hello_world_template, AccountCreateTemplate, AccountCreateAPIView, \
    AccountLoginView, AccountRetrieveAPIView, AccountRetrieveTemplateView, AccountUpdateAPIView, \
    AccountUpdateTemplateView, AccountDestroyAPIView
from rest_framework.authtoken import views

app_name = 'accountapp'

urlpatterns = [
    # UI를 보기 위한 부분
    path('hello_world_template/', hello_world_template, name='hello_world_template'),
    # 로직 처리 위한 부분
    path('hello_world/', hello_world, name='hello_world'),

    # UI 로그인
    path('login_template/', AccountLoginView, name='login_template'),
    # 로그인 로직
    path('login/', views.obtain_auth_token, name='login'),

    path('logout_template/',TemplateView.as_view(template_name='accountapp/logout.html'), name='logout'),

    # UI 가입
    path('create_template/',AccountCreateTemplate,name='create_template'),
    # 가입 로직
    path('create/',AccountCreateAPIView.as_view(), name='create'),

    # UI 디테일
    path('retrieve_template/<int:pk>',AccountRetrieveTemplateView.as_view(), name='retrieve_template'),

    # UI 로직
    path('retrieve/<int:pk>',AccountRetrieveAPIView.as_view(), name='retrieve'),

    path('update_template/<int:pk>', AccountUpdateTemplateView.as_view(), name='update_template'),
    path('update/<int:pk>', AccountUpdateAPIView.as_view(), name='update'),

    path('delete/<int:pk>', AccountDestroyAPIView.as_view(), name='delete'),
]
