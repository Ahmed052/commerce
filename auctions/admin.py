from django.contrib import admin
from .models import User, Auction,Bid,Category,Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)
