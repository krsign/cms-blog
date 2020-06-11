from django.urls import path,include
from blog.views import  contact_us_form_view, register_form_view,post_update_form_view, post_delete_form_view
from blog.views import  PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('',PostListView.as_view(), name='home'),

    # path('category/<int:id>', HomeView.as_view(), name='category_filters'),
    # path('blog/<int:id>',PostView.as_view(), name='post-detail'),

    # path('blog/<int:pk>',PostDetailView.as_view(), name='post-detail'), 
    
    # if you want to keep id as id then use pk_url_kwarg = 'pk' in views
    path('blog/<int:id>',PostDetailView.as_view(), name='post-detail'), 

    path('contact', contact_us_form_view, name='contact-us'),
    path('register', register_form_view, name='register'),

    path('post', PostCreateView.as_view(), name='new-post'),
    
    path('update/<int:id>', post_update_form_view, name='update'),
    path('delete/<int:id>', post_delete_form_view, name='delete'),


   
]