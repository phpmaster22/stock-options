from django.urls import path
from option.views import Options

urlpatterns = [
    path('', Options.as_view(), name="option"),
]
