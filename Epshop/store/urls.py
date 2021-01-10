
from django.urls import path
from store.views import home,signup,login,checkout,orderview
from .views import cart
from .views.login import logout

urlpatterns = [
path('',home.index.as_view(),name="homepage"),
path('signup/',signup.Signup.as_view(),name="signup"),
path('login/',login.Login.as_view(),name="login"),
path('logout',logout,name="logout"),
path('cart',cart.Cart.as_view(),name="cart"),
path('checkout',checkout.Checkout.as_view(),name="checkout"),
path('order',orderview.orderview.as_view(),name="orderview"),
# path('about/',views.about,name="about"),
# path('contact/',views.contact,name="contact"),
# path('checkout/',views.checkout,name="checkout"),
# path('productview/<int:myid>',views.productview,name="productview"),
]