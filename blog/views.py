from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import *
from blog.forms import ContactUsForm, RegisterForm, PostForm
# Create your views here.
from django.views import View
from django.views import generic

# class HomeView(View):

#     def get(self, request, id=None):
#         posts = Post.objects.filter(status='P')
#         if id:
#             cat = Category.objects.get(id=id)
#             posts = Post.objects.filter(category = cat)
#             return render(request, 'blog/stories.html',context={'posts':posts, 'categories':Category.objects.all()})

#         categories = Category.objects.all()
#         context = {'posts':posts, 'categories':categories}
#         return render(request, 'blog/stories.html',context )

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='P')
    context_object_name = 'posts'
    template_name = 'blog/stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


# class PostView(View):
#     def get(self, request, id):
#         try:
#             post = Post.objects.get(id=id)
#             # whatever passing as key in context will become variable in template files
#             return render(request, 'blog/blog-post.html', context = {'post':post})
#         except:

#             return HttpResponse('Welcome to my blog!!!')

class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status='P')
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'



def contact_us_form_view(request):
    if request.method == 'GET':
        form = ContactUsForm()
        return render(request, 'blog/contact-us.html', context={'form':form})
        
    else:
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return render(request, 'blog/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'blog/contact-us.html', context={'form':form})

def register_form_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'blog/register.html', context={'form':form})
        
    else:
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            return render(request, 'blog/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'blog/register.html', context={'form':form})


# function view
# def post_form_view(request):
#     # for handling the image data is captured in request.FILEs
#     # print(request.FILES) 
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'blog/post.html', context={'form':form})
#     else:
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'blog/thankyou.html')
#         else:
#             print(form.errors)
#             return render(request, 'blog/post.html', context={'form':form})



# class based view
# class PostCreateView(View):

#     def get(self, request):
#         form = PostForm()
#         return render(request, 'blog/post.html', context={'form':form})
#     def post(self, request):
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'blog/thankyou.html')
#         else:
#             print(form.errors)
#             return render(request, 'blog/post.html', context={'form':form})



# url is configured with same name
# any issues with template we get : ImproperlyConfigured  Erro
class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title','content', 'status', 'category', 'image']
    template_name = 'blog/post.html'
    success_url = '/'



def post_update_form_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/post.html', context={'form':form})
    else:
        print(request.POST)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return render(request, 'blog/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'blog/post.html', context={'form':form})

def post_delete_form_view(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/delete.html' , context={'post':post})