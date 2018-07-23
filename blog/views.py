from rest_framework import mixins, viewsets

from .models import Blog
from .serializers import BlogSerializer

class BlogListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
