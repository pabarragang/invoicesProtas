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



def createInvoice(request):
	response = {}
	if request.POST['number']:
		number = request.POST['number']
		if request.POST['created_at']:
			created_at = request.POST['created_at']
			if request.POST['total_value']:
				total_value = request.POST['total_value']
				total_iva = None
				total_rte = None
				if request.POST['total_iva']:
					total_iva = request.POST['total_iva']
				if request.POST['total_rte']:
					total_rte = request.POST['total_rte']
				if request.POST['client_id']:
					client = Client.objects.get(id=request.POST['client_id'])
					if request.POST['client_document_id']:
						document_type = Document_type.objects.get(id=request.POST['client_document_type'])
						invoice = Invoice(number=number,created_at=created_at,total_value=total_value,total_iva=total_iva,total_rte=total_rte,client_id=client,client_document_type=document_type)
						invoice.save()			
						response['response'] = "Creted"
					else:
						response['response'] = "Without document type"
				else:
					response['response'] = "Without client"
			else:
				response['response'] = "Without total_value"
		else:
			response['response'] = "Without created_at"
	else:
		response['response'] = "Without number"
	return HttpResponse(json.dumps(response))

def removeInvoice(request):
	response = {}
	if request.POST['id']:
		invoice = Invoice.objects.get(id=request.POST['id'])
		if invoice:
			invoice.delete()
			response['response'] = "Deleted"
		else:
			response['response'] = "This invoice does nor exist"
	else:
		response['response'] = "Without id"
	return HttpResponse(json.dumps(response))

def modifiedInvoice(request):
	response = {}
	if request.POST['id']:
		invoice = Invoice.objects.get(id=request.POST['id'])
		if invoice:
			if request.POST['number']:
				invoice.number = request.POST['number']
			if request.POST['created_at']:
				invoice.created_at = request.POST['created_at']
			if request.POST['total_value']:
				invoice.total_value = request.POST['total_value']
			if request.POST['total_iva']:
				invoice.total_iva = request.POST['total_iva']
			if request.POST['total_rte']:
				invoice.total_rte = request.POST['total_rte']
			if request.POST['client_id']:
				invoice.client_id = Client.objects.get(id=request.POST['client_id'])
			if request.POST['client_document_type']:
				invoice.client_document_type = Document_type.objects.get(id=request.POST['client_document_type'])
			invoice.save()
			response['response'] = "Modified"
		else:
			response['response'] = "This invoice does not exist"
		return HttpResponse(json.dumps(response))
	else:
		response['response'] = "Without id"
		return HttpResponse(json.dumps(response))

def getInvoice(request):
	response = {}
	if request.POST['id']:
		invoice = Invoice.objects.get(id=request.POST['id'])
		if invoice:
			response['number']=invoice.number
			response['created_at']=invoice.created_at
			response['total_value']=invoice.total_value
			response['total_iva']=invoice.total_iva
			response['total_rte']=invoice.total_rte
			response['client_id']=invoice.client_id
			response['client_document_type']=invoice.client_document_type
			return HttpResponse(json.dumps(response))
		else:
			response['response'] = "This invoice does not exist"
			return HttpResponse(json.dumps(response))
	else:
		response['response'] = "Without id"
		return HttpResponse(json.dumps(response))

def addProducts(request):
	response = {}
	if request.POST['invoice_id']:
		invoice = Invoice.objects.get(id=request.POST['invoice_id'])
		if request.POST['product_list'] and request.POST['quantity_list']:
			products = json.loads(request.POST['product_list'])
			quantities = json.loads(request.POST['quantity_list'])
			for product in products:
				product_to_add = Product.objects.get(id=product.id)
				invoices_has_product = Invoices_has_product(invoice=invoice,product=product_to_add,quantity=quantities[product.id])
				invoices_has_product.save()
		else:
			response['response'] = "Without products or quantities"
	else:
		response['response'] = "Without invoice"

def removeProducts(request):
	response = {}
	if request.POST['id']:
		item = Invoices_has_product.objects.get(id=request.POST['id'])
		if item:
			item.delete()
			response['response'] = "Deleted"
		else:
			response['response'] = "This item does nor exist"
	else:
		response['response'] = "Without id"
	return HttpResponse(json.dumps(response))