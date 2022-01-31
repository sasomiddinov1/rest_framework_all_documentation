from account.api.views import (
    registration_view,
    account_properties_view,
    update_account_view,
    ObtainAuthTokenView,
)
from django.urls import path
app_name = 'account'

urlpatterns = [
    path('properties', account_properties_view, name='properties'),
    path('properties/update', update_account_view, name='update'),
    path('login', ObtainAuthTokenView.as_view(), name='login'),
    path('register', registration_view, name='register'),

]























































































