from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Category
from .serializer import blogSerializer,categorySerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

def home(request):
    return HttpResponse("<h1>Hello from Home</h1>")

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk'].split('-')
        print(params)
        if len(params)==1:
            blog = Blog.objects.filter(
                category=params[0])
        if (len(params)>1):
            blog = Blog.objects.filter(
                category=params[0], age = params[1])
        serilizer = blogSerializer(blog, many=True)
        return Response(serilizer.data)
    
    def destroy(self, request, *args, **kwargs):
        user_log = request.user
        if (user_log =='admin'):
            blog = self.get_object()
            blog.delete()
            return Response({'message':'Blog deleted.'})
        else:
            return Response({'message':'Not Allowed'})

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def create(self, request, *args, **kwargs):
        categories = Category.objects.filter(name=request.data['name'])
        if len(categories)>0:
            return Response({'message':'Existance of category before !'})
        else:
            cate = Category(name=request.data['name'])
            cate.save()
            serializer = categorySerializer(cate)
        return Response(serializer.data)
