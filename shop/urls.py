from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.signupPage, name='signup'),
    path('profile/', views.profilePage, name='update-profile'),
    path('product/<int:p_id>/', views.productviewPage, name='product-page'),
    path('cart/', views.addtocart, name= 'add-to-cart'),
    path('cart-prdt/', views.cartview, name='cart-view-page'),
    path('change-password/', views.changepasswordPage, name='change-password'),
    
]


