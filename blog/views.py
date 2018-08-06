from django.db.models import Q

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Blog, Tag
from .serializers import BlogSerializer, TagSerializer

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
        search = self.request.GET.get('search', "")
        tag_id = self.request.GET.get('tag_id', "")
        result = []
        if search:
            blogs = blogs.filter(Q(title__icontains=search)|
                                 Q(category__name__icontains=search)|
                                 Q(tags__name__icontains=search)|
                                 Q(contents__icontains=search))
        if tag_id:
            tag = Tag.objects.get(id=tag_id)
            blogs = blogs.filter(tags=tag)


        for blog in blogs:
            result.append({
                "id": blog.id,
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

    def retrieve(self, request, *args, **kwargs):
        blog_id = self.kwargs["pk"]
        blog = Blog.objects.get(id=blog_id)
        blog.increase_views()
        tags = []
        for tag in blog.tags.all():
            tags.append(tag.name)
        return Response({
            "id": blog.id,
            "title": blog.title,
            "tags": tags,
            "created_time": blog.created_time.strftime('%Y-%m-%d'),
            "author": blog.author.username,
            "views": blog.views,
            "contents": blog.contents,
            "author_email": blog.author.email
            })


class TagListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
