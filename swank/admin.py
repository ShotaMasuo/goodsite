from django.contrib import admin
from .models import UserModel, SiteModel, Comment
# Register your models here.
admin.site.register(UserModel)
admin.site.register(SiteModel)
admin.site.register(Comment)