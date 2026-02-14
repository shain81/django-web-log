# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from rest_framework import status
#
# from .models import Post, Comment
# from .forms import PostForm
# from django.views import generic
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import PostSerializer
#
#
# #this creator is functional
#
# # Create your views here.
# @api_view(['GET', 'POST'])
# def index(request):
#     # body
#
#     # for GET method
#     # pk=request.query_params.get('pk')
#
#     #for POST method
#     pk = request.data.get('pk')
#     print(request.data)
#     try:
#         p = Post.objects.get(pk=2)
#     except:
#         return Response({'detail': 'Post not exits'}, status=status.HTTP_404_NOT_FOUND)
#     # return HttpResponse('<h1>welcom to django</h1>')
#     serializer = PostSerializer(p)
#
#     return Response(serializer.data)
#
#
# def home(request):
#     return HttpResponse('<h3>Welcome to my blog....</h3>')
#
#
# def post_list(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'posts/post_list.html', context=context)
#
#
# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'posts/post_list.html'
#     context_object_name = 'posts'
#
#
# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(pk=post_id)
#     except Post.DoesNotExist:
#         return HttpResponseNotFound('Post is not exist')
#
#     # post = get_object_or_404(Post,pk=post_id)
#
#     comments = Comment.objects.filter(post=post)
#     context = {'post': post, 'comments': comments}
#
#     return render(request, 'posts/post_detail.html', context=context)
#
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(PostDetail, self).get_context_data()
#         context['comment'] = Comment.objects.filter(post=kwargs['object'].pk)
#     # context_object_name = 'posts'
#     #
#     # def get_queryset(self):
#     #     return get_object_or_404(Post,pk=self.request.POST['post_id'])
#
#
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print(type(form.cleaned_data))
#             print(form.cleaned_data)
#             Post.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/posts/')
#
#     else:
#         form = PostForm()
#
#     return render(request, 'posts/post_create.html', {'form': form})

# class base

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer


# @api_view(['GET', 'POST'])
# def foo(request):
#     if request.method == 'GET':
#         pass
#
#     elif request.method == 'POST':
#         pass


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response(serializer.data)

# CRUD -- create , retrieve , update , delete
