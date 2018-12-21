from django.contrib import admin
from forum.models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(UserProfile)
