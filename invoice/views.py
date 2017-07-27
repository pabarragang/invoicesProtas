# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from invoice.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import redirect
import json


def getProducts(request):
    products = Product.objects.all()
    template = loader.get_template('invoice/product_table.html')
    context = {'products': products}
    return HttpResponse(template.render(context, request))


def formProducts(request):
    template = loader.get_template('invoice/product_form.html')
    context = {}
    try:
        product = Product.objects.get(pk=request.GET['id_product'])
        context = {'product': product}
    except Exception:
        pass
    return HttpResponse(template.render(context, request))


def saveProduct(request):
    response = {}
    if request.method == 'POST':
        try:
            product = Product()
            if request.POST['id'] != '':
                product = Product.objects.get(id=request.POST['id'])
            product.name = request.POST['name']
            product.packing = request.POST['packing']
            product.price = request.POST['price']
            product.iva = request.POST['iva']
            product.save()
            response = redirect('/invoice/list_products/')
        except Exception as e:
            response = JsonResponse({'error': str(e)})
    else:
        response = JsonResponse({'error': 'no method get allowed'})
    return response


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


def suggestionsProduct(request):
    response = {}
    if request.method == 'GET':
        try:
            search_text = request.GET['search_text']
            products = Product.objects.filter(name__contains=search_text)
            dictProducts = [{'id': product.id, 'name': product.name}
                            for product in products]
            response = JsonResponse({'products': dictProducts})
        except Exception as e:
            response = JsonResponse({'error': str(e)})
    else:
        response = JsonResponse({'error': 'no methos post allowed'})
    return response


def getClients(request):
    clients = Client.objects.all()
    template = loader.get_template('invoice/client_table.html')
    context = {'clients': clients}
    return HttpResponse(template.render(context, request))


def formClients(request):
    template = loader.get_template('invoice/client_form.html')
    context = {}
    document_types = DocumentType.objects.all()
    context = {'document_types': document_types}
    try:
        client = Client.objects.get(pk=request.GET['id_client'])
        context.update({'client': client})
    except Exception as e:
        print str(e)
    return HttpResponse(template.render(context, request))


def saveClient(request):
    response = {}
    if request.method == 'POST':
        try:
            client = Client()
            if request.POST['id'] != '':
                client = Client.objects.get(id=request.POST['id'])
            client.document = request.POST['document']
            client.name = request.POST['name']
            client.last_name = request.POST['last_name']
            client.address = request.POST['address']
            client.cell_phone = request.POST['cell_phone']
            client.phone = request.POST['phone']
            client.document_type = DocumentType.objects.get(
                id=request.POST['document_type'])
            client.save()
            response = redirect('/invoice/list_clients/')
        except Exception as e:
            response = JsonResponse({'error': str(e)})
    else:
        response = JsonResponse({'error': 'no method get allowed'})
    return response


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


def getInvoices(request):
    invoices = Invoice.objects.all()
    template = loader.get_template('invoice/invoice_table.html')
    context = {'invoices': invoices}
    return HttpResponse(template.render(context, request))


def formInvoices(request):
    template = loader.get_template('invoice/invoice_form.html')
    context = {}
    try:
        product = Product.objects.get(pk=request.GET['id_product'])
        context = {'product': product}
    except Exception:
        pass
    return HttpResponse(template.render(context, request))


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
                        document_type = Document_type.objects.get(
                            id=request.POST['client_document_type'])
                        invoice = Invoice(number=number,
                                          created_at=created_at,
                                          total_value=total_value,
                                          total_iva=total_iva,
                                          total_rte=total_rte,
                                          client_id=client,
                                          client_document_type=document_type)
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
                invoice.client_id = Client.objects.get(
                    id=request.POST['client_id'])
            if request.POST['client_document_type']:
                invoice.client_document_type = Document_type.objects.get(
                    id=request.POST['client_document_type'])
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
            response['number'] = invoice.number
            response['created_at'] = invoice.created_at
            response['total_value'] = invoice.total_value
            response['total_iva'] = invoice.total_iva
            response['total_rte'] = invoice.total_rte
            response['client_id'] = invoice.client_id
            response['client_document_type'] = invoice.client_document_type
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
                invoices_has_product = Invoices_has_product(
                    invoice=invoice, product=product_to_add,
                    quantity=quantities[product.id])
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
