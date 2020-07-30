from django.contrib import admin
from .models import User, Activity

"""
Registering User and Activity model.
By this Django would be able to create a default form representation. 
"""
admin.site.register(User)
admin.site.register(Activity)
