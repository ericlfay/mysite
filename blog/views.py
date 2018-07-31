from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Blog
from .serializers import BlogSerializer

class PageNumberPaginationSet(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data, other_datas=None):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data,
        })


class BlogListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = PageNumberPaginationSet

    def list(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        result = []
        for blog in blogs:
            result.append({
                "title": blog.title,
                "excerpt": blog.excerpt,
                "category": blog.category.name,
                "tags": blog.tags.all()[0].name,
                "created_time": blog.created_time.strftime('%Y-%m-%d'),
                "author": blog.author.name,
                "views": blog.views,
                "image": str(blog.image)
                })
        page = self.paginate_queryset(result)

        return self.get_paginated_response(page)
