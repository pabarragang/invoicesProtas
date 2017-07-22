"""invoicesProtas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from invoice import views

urlpatterns = [
    url(r'^list_products/$', views.getProducts),
    url(r'^form_products/$', views.formProducts),
    url(r'^save_product/$', views.saveProduct),

    url(r'^remove_product/$', views.removeProduct),

    url(r'^list_clients/$', views.getClients),
    url(r'^form_clients/$', views.formClients),
    url(r'^save_client/$', views.saveClient),

    url(r'^create_invoice/$', views.createInvoice),
    url(r'^remove_invoice/$', views.removeInvoice),
    url(r'^modified_invoice/$', views.modifiedInvoice),
    url(r'^get_invoice/$', views.getInvoice),
    url(r'^products_add/$', views.addProducts),
    url(r'^products_remove_invoice/$', views.removeProducts),
]
