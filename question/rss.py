from django.contrib.syndication import Feed
from django.core.urlresolvers import reverse
from .models import Question


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Question.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem
    def item_link(self, item):
        return reverse('question', args=[item.slug])
