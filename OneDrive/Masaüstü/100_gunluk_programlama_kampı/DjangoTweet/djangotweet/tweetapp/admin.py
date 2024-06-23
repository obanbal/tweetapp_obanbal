from django.contrib import admin
from tweetapp.models import Tweet
# from . import models

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Group', {"fields":['message']}),
        ('Nickname Group', {"fields":['nickname']})
    ]
    # fields = ['message', 'nickname']
# admin sayfasında hangi bilgilerin görüneceği ve nasıl görüneceği fields ile belirlenebilir.
# admin sayfasında görünecek bilgileri fieldsets ile istediğimiz gibi gruplayabiliriz.

admin.site.register(Tweet, TweetAdmin)