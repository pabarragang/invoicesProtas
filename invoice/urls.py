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
    url(r'^products_list/$', views.getProducts),
    url(r'^products_form/$', views.formProducts),
    url(r'^product_create/$', views.createProduct),
    url(r'^product_remove/$', views.removeProduct),
    url(r'^product_modified/$', views.modifiedProduct),
    url(r'^get_product/$', views.getProduct),
    url(r'^get_document_types/$', views.getDocumentTypes),
    url(r'^create_client/$', views.createClient),
    url(r'^remove_client/$', views.removeClient),
    url(r'^modified_client/$', views.modifiedClient),
    url(r'^get_client/$', views.getClient),
]
