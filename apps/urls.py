from django.contrib import admin
from django.urls import path

from apps.utils import PyClickMerchantAPIView
from apps.views import IndexView, AboutView, ServicesView, PackagesView, PackageDetailView, ContactModelFormView, \
    BookingFormView, PackageSearchView, CreateClickTransactionView, ClickTransactionTestView, ClickMerchantServiceView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('services', ServicesView.as_view(), name='services'),
    path('packages', PackagesView.as_view(), name='packages'),
    path('packages/<str:slug>', PackageDetailView.as_view(), name='package-detail'),
    path('contact', ContactModelFormView.as_view(), name='contact'),
    path('booking', BookingFormView.as_view(), name='booking'),
    path('search', PackageSearchView.as_view(), name='trip-search'),
    path("click-pay", PyClickMerchantAPIView.as_view()),
    path("process/click/transaction/create/", CreateClickTransactionView.as_view()),
    path("process/click/transaction/", ClickTransactionTestView.as_view()),
    path("process/click/service/<service_type>", ClickMerchantServiceView.as_view()),
]


'''
http://localhost:8000/en/process/click/transaction/create/

'''