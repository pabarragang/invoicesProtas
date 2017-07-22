# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=45,null=False,blank=False)
	packing = models.CharField(max_length=45,null=False,blank=False)
	price = models.IntegerField()
	iva = models.FloatField(null=True)

class DocumentType(models.Model):
	name = models.CharField(max_length=45,null=False,blank=False)

class Client(models.Model):
	document = models.CharField(max_length=11,unique=True,null=False,blank=False)
	name = models.CharField(max_length=45,blank=False,null=False)
	last_name = models.CharField(max_length=45,blank=False,null=False)
	address = models.CharField(max_length=45,null=False,blank=False)
	phone = models.CharField(max_length=7,null=True,blank=False)
	cell_phone = models.CharField(max_length=10,null=False,blank=False)
	document_type = models.ForeignKey(DocumentType)

class Invoice(models.Model):
	number = models.CharField(max_length=45,null=False,blank=False)
	created_at = models.DateTimeField(null=False,blank=False)
	total_value = models.IntegerField()
	total_iva = models.IntegerField()
	total_rte = models.IntegerField()
	client_id = models.ForeignKey(Client, null=False,blank=False)
	client_document_type = models.ForeignKey(DocumentType)

class Invoices_has_product(models.Model):
	invoice = models.ForeignKey(Invoice,null=False,blank=False)
	product = models.ForeignKey(Product,null=False,blank=False)
	quantity = models.FloatField(null=False,blank=False)
