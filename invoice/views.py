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
				response['response'] = "Creted"
			response['response'] = "Without price"
		response['response'] = "Without packing"
	response['response'] = "Without name"
	return HttpResponse(json.dumps(response))

def removeProduct(request):
	response = {}
	if request.POST['id']:
		product = Product.objects.get(id=request.POST['id'])
		if product:
			product.delete()
			response['response'] = "Deleted"
		else:
			response['response'] = "This product does nor exist"
	else:
		response['response'] = "Without id"
	return HttpResponse(json.dumps(response))

def modifiedProduct(request):
	response = {}
	if request.POST['id']:
		product = Product.objects.get(id=request.POST['id'])
		if product:
			if request.POST['name']:
				product.name = request.POST['name']
			if request.POST['packing']:
				product.packing = request.POST['packing']
			if request.POST['price']:
				product.price = request.POST['price']
			if request.POST['iva']:
				product.iva = request.POST['iva']
			product.save()
			response['response'] = "Modified"
		else:
			response['response'] = "This product does not exist"
		return HttpResponse(json.dumps(response))
	else:
		response['response'] = "Without id"
		return HttpResponse(json.dumps(response))

def getProduct(request):
	response = {}
	if request.POST['id']:
		product = Product.objects.get(id=request.POST['id'])
		if product:
			response['name']=product.name
			response['packing']=product.packing
			response['price']=product.price
			response['iva']=product.iva
			return HttpResponse(json.dumps(response))
		else:
			response['response'] = "This product does not exist"
			return HttpResponse(json.dumps(response))
	else:
		response['response'] = "Without id"
		return HttpResponse(json.dumps(response))

