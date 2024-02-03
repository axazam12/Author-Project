from . import views
from django.urls import path
from . import views

urlpatterns = [

    path('', views.UserListBook, name='userlist'),
    path('usersearch/',views.UserSearch,name='usersearch'),
    path('detail/<int:book_id>', views.UserDetailsBook, name='userdetail'),
    path('addcart/<int:book_id>/',views.AddCart,name='addtocart'),
    path('viewcart/',views.ViewCart,name='viewcart'),
    path('increase/<int:item_id>/',views.IncreaseQty,name='increase_qty'),
    path('decrease/<int:item_id>/',views.DecreaseQty,name='decrease_qty'),
    path('remove/<int:item_id>/',views.RemoveItem,name='remove_item'),
    
    path('checkout/', views.checkout_session, name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),

    


]