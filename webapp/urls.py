from django.urls import path
from . import views

urlpatterns = [
     path("",views.index,name="index"),
     path("index",views.index,name="index"),
     path("login",views.login,name="login"),
     path("signup",views.signup,name="signup"),
     path("insert",views.insert,name="insert"),
     path("profile",views.profile,name="profile"),
     path("logout",views.logout,name="logout"),
     path("books",views.books,name="books"),
     path("returnb",views.returnb,name="returnb"),
     path("history",views.history,name="history"),
     path("book_details",views.book_details,name="book_details"),
     path("rent",views.rent,name='rent'),
     path("rent_update",views.rent_update,name="rent_update"),
     path("policy",views.policy,name="policy"),
     path("term",views.term,name="term"),
     path("refund",views.refund,name="refund"),
     path("shipping",views.shipping,name="shipping"),
     path("contact",views.contact,name="contact"),
     path("contact1",views.contact1,name="contact1"),
     path("about",views.about,name="about"),
]

