from django.urls import path

from profileapp.views import ProfileCreateAPIView

app_name='profileapp'

urlpatterns = [
    path('',ProfileCreateAPIView.as_view(), name='create')
]

