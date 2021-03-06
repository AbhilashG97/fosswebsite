# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect
from django.views.generic.list import ListView

import feedparser
import datetime

class ArticleListView(ListView):
    template_name = 'BlogFeedAggregator/blog.html'
    context_object_name = 'article'
    paginate_by = 10    
    queryset = Article.objects.all().order_by("-publication_date")

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'BlogFeedAggregator/blog.html', {'articles': articles })

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'BlogFeedAggregator/feeds_list.html', {'feeds': feeds})

def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)

            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

                # Example usage of the feedparser python API for crawling blog Data.
                # feed.title = feedData.feed.title
                # feed.save()

                feed.title = feedData.feed.title
                feed.save()

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    try:
                        article.description = entry.description[:entry.description.find('<img ')]
                    except:
                        article.description = entry.description

                    article.author = entry.author_detail.name

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    article.save()

            return redirect('BlogFeedAggregator.views.feeds_list')
    else:
        form = FeedForm()
        return render(request, 'BlogFeedAggregator/new_feed.html', {'form': form})
