from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
    
class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
    
class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)
    
# class BlogPostCategoryView(ListAPIView):
#     serializer_class = BlogPostSerializer
#     permission_classes = (permissions.AllowAny,)
    
#     def post(self, request, format=None):
#         data = self.request.data
#         category = data.get('category', '')
        
#         if not category:
#             return Response({'error': 'Category is required'}, status=400)
        
#         queryset = BlogPost.objects.filter(category__iexact=category).order_by('-date_created')
#         serializer = BlogPostSerializer(queryset, many=True)
        
#         return Response(serializer.data)

class BlogPostCategoryView(ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)
    
    def get_queryset(self):
        
        pk = self.kwargs['pk']
        return BlogPost.objects.filter(category=pk)