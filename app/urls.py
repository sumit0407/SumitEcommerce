
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm
urlpatterns = [
    path('', views.home,name='home'),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),

    path('pluscart/', views.plus_cart, name='pluscart'),

    path('minuscart/', views.minus_cart, name='minuscart'),    
    
    path('laptop/',views.laptop,name='laptop'),

    path('removecart',views.remove_cart,name='removecart'),
    
    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(),name='profile'),
    
    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),
    
    path('mobiles/', views.mobile,name='mobile'),
    
    path("mobiledata/<str:data>",views.mobile,name="mobiledata"),

    path("laptopdata/<str:data>/",views.laptopdata,name="laptopdata"),

    path('wearspage/',views.wearspage,name='wears'),
    
    path('wearspage/<str:data>/',views.wearspage,name='wearsdata'),
    
    path('accounts/login',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    
    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('passwordchange/', auth_views.PasswordChangeView.
    as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/' ),name='passwordchange'),
    
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    
    
    

]
