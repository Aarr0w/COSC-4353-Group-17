from django.contrib import admin

# Register your models here.
from .models import User
from .models import Quote
from .models import Profile
admin.site.register (Profile)
admin.site.register(User)
admin.site.register(Quote)