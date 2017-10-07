# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite.models import NewTable, Product

# Register your models here.

admin.site.register(NewTable)
admin.site.register(Product)
