from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path("features/", views.features, name="features"),
    path("featureFresh/", views.featureFresh, name="featureFresh"),
    path("freeDel/", views.freeDel, name="freeDel"),
    path("easyPay", views.easyPay, name="easyPay"),
    path("categories/", views.categories, name="categories"),
    path("product/", views.product, name="product"),
    path("search/", views.Search, name="search"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/', views.Checkout, name="checkout"),
    path("placeorder/", views.placeorder, name="placeorder"),
    path("thankYou/", views.thankYou, name="thankYou"),
    path('review/', views.review, name="review"),
    path('blogVege/', views.blogVege, name="blogVege"),
    path('blogFruit/', views.blogFruit, name="blogFruit"),
    path('blogDairy/', views.blogDairy, name="blogDairy"),
    path('blog/', views.blog, name="blog"),
    path('forgotPass/', views.forgotPass, name="forgotPass"),
    path('orderStatus/', views.order_status, name="orderStatus"),
    path('salesReport/<str:period>/', views.generate_sales_report, name="salesReport")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
