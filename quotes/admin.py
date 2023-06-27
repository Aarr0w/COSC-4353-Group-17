from django.contrib import admin

# Register your models here.
from .models import User
from .models import Quote
admin.site.register(User)
admin.site.register(Quote)