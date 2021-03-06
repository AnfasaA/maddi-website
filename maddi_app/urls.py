from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("shop", views.shop, name="shop"),
  path("payment", views.payment, name="payment"),
  path("journal", views.journal, name="journal"),
  path("about", views.about, name="about"),
  path("cart", views.cart, name="cart"),
  path("login", views.login, name="login"),
  path("register", views.register, name="register"),
  path("province/", views.province, name="province"),
  path("province/<int:id>/", views.province, name="province_cities"),
  path("city/", views.city, name="city"),
  path("cost/<int:id>/", views.cost, name="cost"),
]