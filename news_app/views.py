from django.shortcuts import render
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import requests
from django.http import request
import io
import base64
import feedparser
import urllib.parse
import warnings
warnings.filterwarnings("ignore", message="'T' is deprecated", category=FutureWarning)

def fetch_stock_news(topics, days=1):
    # Calculate the date 'days' ago
    days = int(days)
    target_date = datetime.now() - timedelta(days=days)

    # Encode the topics for the URL
    encoded_topics = '+'.join(urllib.parse.quote(topic.strip()) for topic in topics)

    # Create the RSS feed URL for the stock symbol
    rss_url = f"https://news.google.com/rss/search?q={encoded_topics}"

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Extract news articles from the feed published in the last 'days' days
    news_list = []
    for entry in feed.entries:
        # Parse the publication date of the article
        published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
        # Check if the article was published in the last 'days' days
        published_date = published_date.replace(tzinfo=None)

        if published_date >= target_date:
            # Extract image URL if available
            image_url = None
            if 'media_content' in entry and len(entry.media_content) > 0:
                # Attempt to extract image URL from 'media_content'
                image_url = entry.media_content[0]['url']
            elif 'enclosures' in entry and len(entry.enclosures) > 0:
                # Attempt to extract image URL from 'enclosures'
                image_url = entry.enclosures[0]['url']
            elif 'links' in entry and len(entry.links) > 0:
                # Attempt to extract image URL from 'links'
                for link in entry.links:
                    if link.get('type', '').startswith('image/'):
                        image_url = link['href']
                        break

            news_list.append({
                'title': entry.title,
                'summary': entry.summary,
                'link': entry.link,
                'published': published_date.strftime("%Y-%m-%d %H:%M:%S"),
                'image_url': image_url  # Include image URL in the news information
            })

    return news_list

def stock_news(request):
    if request.method == 'POST':
        topics = request.POST.get('topics', '').split(',')
        days = request.POST.get('days', 1)  # Default to 1 if not provided
        news = fetch_stock_news(topics, days)
        return render(request, 'stock_news.html', {'news': news, 'topics': ', '.join(topics)})
    else:
        return render(request, 'stock_news.html')



def fetch_stock_news1(topics, days=1):
    # Calculate the date 'days' ago
    days = int(days)
    target_date = datetime.now() - timedelta(days=days)
    target_date = target_date.replace(tzinfo=None)  # Make target_date offset-naive

    # List of RSS feed URLs for different sources
    rss_feeds = {
        'Economic Times': 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms',
        'Financial Times': 'https://www.ft.com/news-feed/rss',
        'Mint': 'https://www.livemint.com/rss/markets',
        'Business Line': 'https://www.thehindubusinessline.com/markets/stock-markets/?service=rss',
        'Moneycontrol': 'https://www.moneycontrol.com/rss/latestnews.xml',
        'Investors Business Daily': 'https://www.investors.com/feed/',
        'Goodreturns': 'https://www.goodreturns.in/rss/goodreturns-fb.xml',
        'NDTV Profit': 'https://feeds.feedburner.com/NDTVProfit-LatestNews'
    }

    news_list = []
    for source, rss_url in rss_feeds.items():
        # Parse the RSS feed
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            # Parse the publication date of the article
            published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
            # Convert published_date to offset-naive
            published_date = published_date.replace(tzinfo=None)
            # Check if the article was published in the last 'days' days
            if published_date >= target_date:
                image_url = None
                if 'media_content' in entry and len(entry.media_content) > 0:
                    # Attempt to extract image URL from 'media_content'
                    image_url = entry.media_content[0]['url']
                elif 'enclosures' in entry and len(entry.enclosures) > 0:
                    # Attempt to extract image URL from 'enclosures'
                    image_url = entry.enclosures[0]['url']
                elif 'links' in entry and len(entry.links) > 0:
                    # Attempt to extract image URL from 'links'
                    for link in entry.links:
                        if link.get('type', '').startswith('image/'):
                            image_url = link['href']
                            break
                news_list.append({
                    'source': source,
                    'title': entry.title,
                    'summary': entry.summary,
                    'link': entry.link,
                    'published': published_date.strftime("%Y-%m-%d %H:%M:%S"),
                    'image_url': image_url  # Include image URL in the news information

                })

    return news_list


def stock_news1(request):
    if request.method == 'POST':
        topics = request.POST.get('topics', '').split(',')
        days = request.POST.get('days', 1)  # Default to 1 if not provided
        news = fetch_stock_news1(topics, days)
        return render(request, 'stock_news1.html', {'news': news, 'topics': ', '.join(topics)})
    else:
        return render(request, 'stock_news1.html')
