# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from invoice.models import *
from django.http import HttpResponse
import json

# Create your views here.

def createProduct(request):
	response = {}
	if request.POST['name']:
		if request.POST['packing']:
			if request.POST['price']:
				iva = None
				if request.POST['iva']:
					iva = request.POST['iva']
				product = Product(name=request.POST['name'],packing=request.POST['packing'],price=request.POST['price'],iva=iva)
				product.save()
				response['response'] = "Creado"
			response['response'] = "Without price"
		response['response'] = "Without packing"
	response['response'] = "Without name"
	return HttpResponse(json.dumps(response))


