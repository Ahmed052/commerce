from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_auction", views.create_auction, name="create_auction"),
    path("listing/<int:auction_id>", views.listing, name="listing"),
    path("add_to_watchlist/<int:auction_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<int:auction_id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bid/<int:auction_id>", views.bid, name="bid"),
    path("add_comment/<int:auction_id>", views.add_comment, name="add_comment"),
    path("close_auction/<int:auction_id>", views.close_auction, name="close_auction"),
    path("categories", views.categories, name="categories"),
    path("winnings", views.winnings, name="winnings"),
    path("display_category/<str:category>", views.display_category, name="display_category")
]
