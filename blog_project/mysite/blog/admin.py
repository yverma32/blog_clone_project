# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Post,Comment
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
