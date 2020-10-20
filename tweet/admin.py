from django.contrib import admin
from django.contrib import admin
from .models import ProfileSettingsModel, TweetModel, FollowModel, RetweetModel

# Register your models here.

admin.site.register(ProfileSettingsModel)
admin.site.register(TweetModel)
admin.site.register(FollowModel)
admin.site.register(RetweetModel)
