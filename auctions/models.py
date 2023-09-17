from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image_URL = models.URLField(blank=True)
    starting_price = models.ForeignKey('Bid', on_delete=models.CASCADE, related_name="starting_price", blank=True, null=True)
    category = models.CharField(max_length=64)
    auction_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date_of_auction = models.DateField(default=timezone.now().date(),null=True)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="won_auctions", blank=True, null=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    def __str__(self):
      return f"{self.title}"
    

class Bid(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    def __str__(self):
      return f"{self.bid}"
    
class Comment(models.Model):
    comment = models.TextField()
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_comments")
    def __str__(self):
      return f"{self.comment}"    

class Category(models.Model):
    category = models.CharField(max_length=44)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auctions")
         
    def __str__(self):
      return f"{self.category}"
 




    
    
    
   
    
    
    
