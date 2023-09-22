from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Auction,Bid,Category,Comment


def index(request):
    active_auctions = Auction.objects.filter(active=True)
    return render(request, "auctions/index.html",{
        "auctions":active_auctions
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_auction(request):
    if request.method =='GET':
        categories = Category.objects.all()
        return render (request,"auctions/create.html",{
            "categories": categories
        })
    
    if request.method =='POST':
        title= request.POST.get('title')
        image_URL= request.POST.get('imge_url')
        description= request.POST.get('description')
        starting_price= request.POST.get('price')
        category= request.POST.get('category')
        
        auction_owner= request.user
        bid = Bid(bid=starting_price, bidder=auction_owner)
        bid.save()
        auctions = Auction (title=title,
        image_URL=image_URL,
        description=description,
        starting_price=bid, 
        auction_owner=auction_owner,
       )
        auctions.save()
        category = Category(category_list=category)
        category.save()

        return HttpResponseRedirect(reverse("index"))
    
def listing(request, auction_id):
    
     auction= Auction.objects.get(id=auction_id)
     auction_watchlist = request.user in auction.watchlist.all()
     comments = Comment.objects.filter(auction=auction)
     auction_owner = request.user == auction.auction_owner
     if auction.active == False:
         winner = auction.starting_price.bidder
         return render(request,"auctions/listing_page.html",{ 
            "auction": auction,
            "auction_watchlist": auction_watchlist,
            "comments": comments,
            "auction_owner": auction_owner,
            "message": "Auction closed",
            "winner": winner
        })
     return render(request,"auctions/listing_page.html",{ 
            "auction": auction,
            "auction_watchlist": auction_watchlist,
            "comments": comments,
            "auction_owner": auction_owner
        })

def add_to_watchlist(request, auction_id):
    auction= Auction.objects.get(id=auction_id)
    user= request.user
    auction.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing", args=(auction_id,)))


def remove_from_watchlist(request, auction_id):
    auction= Auction.objects.get(id=auction_id)
    user= request.user
    auction.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing", args=(auction_id,)))
    

def watchlist(request):
    user = request.user
    watchlist= user.watchlist.all()
    print(watchlist)
    return render(request,"auctions/watchlist.html",{
        "watchlist": watchlist
    })

def bid(request, auction_id):
    if request.method == "POST":
        auction= Auction.objects.get(id=auction_id)
        bid= request.POST.get("bid")
        bidder= request.user
        if auction.starting_price.bid < float(bid):
            auction.starting_price.bid = float(bid)
            auction.starting_price.bidder = bidder
            auction.starting_price.save()
            return HttpResponseRedirect(reverse("listing", args=[auction_id]))
        else:
            return render(request,"auctions/listing_page.html",{ 
            "auction": auction,
            "message": "Bid must be higher than current price"
        })


def add_comment(request, auction_id):
    if request.method == "POST":
        auction= Auction.objects.get(id=auction_id)
        comment= request.POST.get("comment")
        commenter= request.user
        comment= Comment(comment=comment, commenter=commenter, auction=auction)
        comment.save()
        return HttpResponseRedirect(reverse("listing", args=[auction_id]))

def close_auction(request, auction_id):
    if request.method == "POST":
     auction= Auction.objects.get(id=auction_id)
     auction.active = False
     auction.save()
     auction_watchlist = request.user in auction.watchlist.all()
     comments = Comment.objects.filter(auction=auction)
     auction_owner = request.user == auction.auction_owner
     winner = auction.starting_price.bidder
     return render(request,"auctions/listing_page.html",{ 
            "auction": auction,
            "auction_watchlist": auction_watchlist,
            "comments": comments,
            "auction_owner": auction_owner,
            "message": "Auction closed",
            "winner": winner
        })
    
def winnings(request):
    user = request.user
    auctions = Auction.objects.filter(starting_price__bidder=user, active=False)
    return render(request,"auctions/winning_page.html",{
        "auctions": auctions
    })

def display_category(request, category):
     if request.method == "GET":     
        auctions = Auction.objects.filter(category__category_list=category)
        auctions= Auction.objects.all()
     return render(request,"auctions/categories.html",{
        "auctions": auctions
    })
       

def categories(request):
    categories = Category.objects.all()
    return render(request,"auctions/categories.html",{
        "categories": categories
         
    })