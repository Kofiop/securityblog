from django.urls import reverse_lazy
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostsFeed(Feed):
    title = 'Cybersecurity blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)


    
