# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from invoice.models import *
from django.http import HttpResponse
from django.template import loader
import json


def getProducts(request):
    products = Product.objects.all()
    template = loader.get_template('invoice/product_table.html')
    context = {'products': products}
    return HttpResponse(template.render(context, request))


def formProducts(request):
    template = loader.get_template('invoice/product_form.html')
    context = {}
    return HttpResponse(template.render(context, request))


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

def getDocumentTypes(request):
	response = {}
	document_types = Document_type.objects.all()
	for document_type in document_types:
		response[str(document_type.id)] = document_type.name
	return HttpResponse(json.dumps(response))

def createClient(request):
	response = {}
	if request.POST['document']:
		document = request.POST['document']
		if request.POST['name']:
			name = request.POST['name']
			if request.POST['last_name']:
				last_name = request.POST['last_name']
				if request.POST['address']:
					address = request.POST['address']
					if request.POST['cell_phone']:
						cell_phone = request.POST['cell_phone']
						if request.POST['document_type']:
							document_type = request.POST['document_type']
							phone = None
							if request.POST['phone']:
								phone = request.POST['phone']
							client = Client(document=document,name=name,last_name=last_name,address=address,phone=phone,cell_phone=cell_phone,document_type=Document_type.objects.get(id=document_type))
							client.save()
							response['response'] = "Created"
						else:
							response['response'] = "Without document_type"
					else:
						response['response'] = "Without cell_phone"
				else:
					response['response'] = "Without address"
			else:
				response['response'] = "Without last_name"
		else:
			response['response'] = "Without name"
	else:
		response['response'] = "Without document"
	return HttpResponse(json.dumps(response))

def removeClient(request):
	response = {}
	if request.POST['id']:
		client = Client.objects.get(id=request.POST['id'])
		if client:
			client.delete()
			response['response'] = "Deleted"
		else:
			response['response'] = "This client does not exist"
	else:
		response['response'] = "Without id"
	return HttpResponse(json.dumps(response))

def modifiedClient(request):
	response = {}
	if request.POST['id']:
		client = Client.objects.get(id=request.POST['id'])
		if client:
			if request.POST['document']:
				client.document = request.POST['document']
			if request.POST['name']:
				client.name = request.POST['name']
			if request.POST['last_name']:
				client.last_name = request.POST['last_name']
			if request.POST['address']:
				client.address = request.POST['address']
			if request.POST['cell_phone']:
				client.cell_phone = request.POST['cell_phone']
			if request.POST['document_type']:
				client.document_type = request.POST['document_type']
			if request.POST['phone']:
				client.phone = request.POST['phone']
			client.save()
		else:
			response['response'] = "This client does not exist"
	else:
		response['response'] = "Without id"
	return HttpResponse(json.dumps(response))

def getClient(request):
	response = {}
	if request.POST['id']:
		client = Client.objects.get(id=request.POST['id'])
		if client:
			response['document']=client.document
			response['name']=client.name
			response['last_name']=client.last_name
			response['address']=client.address
			response['cell_phone']=client.cell_phone
			response['document_type']=client.document_type
			response['phone']=client.phone
			return HttpResponse(json.dumps(response))
		else:
			response['response'] = "This client does not exist"
			return HttpResponse(json.dumps(response))
	else:
		response['response'] = "Without id"
		return HttpResponse(json.dumps(response))
