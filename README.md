# Stock News Aggregator

This Django application aggregates stock news from various RSS feeds and displays them on a web page. It provides functionality to search for news based on specified topics and filter news by publication date.
Features

    Fetch Stock News by Topics:
        Aggregates news based on user-provided topics.
        Filters news articles published within a specified number of days.
        Displays news with optional image URLs.

    Fetch News from Multiple Sources:
        Aggregates news from various financial news sources.
        Filters news articles published within a specified number of days.
        Displays news with source information and optional image URLs.

Requirements

    Python 3.x
    Django 3.x or later
    Requests library
    BeautifulSoup4 library
    Feedparser library

Installation
Clone the repository:
        
        git clone <repository_url>
        cd <repository_directory>
            
Create a virtual environment:
        
        python -m venv venv

Activate the virtual environment:
    On Windows:
        
        venv\Scripts\activate

On macOS/Linux:

        source venv/bin/activate

Install the required packages:
        
        pip install -r requirements.txt

Apply migrations:

    
    python manage.py migrate
    
Run the development server:

    python manage.py runserver

Usage

###  Fetch Stock News by Topics

- Navigate to the /stock_news/ URL in your browser.
- Use the form to enter topics (comma-separated) and specify the number of days.
- Submit the form to view the aggregated news based on the topics provided.

### Fetch News from Multiple Sources

- Navigate to the /stock_news1/ URL in your browser.
- Use the form to enter topics (comma-separated) and specify the number of days.
- Submit the form to view the aggregated news from multiple sources.

Code Overview

1.fetch_stock_news(topics, days=1)
    
    Purpose: Fetches stock news based on specified topics and filters by publication date.
    Parameters:
        topics: List of topics to search for.
        days: Number of days to look back for news.
    Returns: List of news articles including title, summary, link, publication date, and image URL.
    
stock_news(request)

    Purpose: Handles HTTP POST requests to fetch stock news and render the stock_news.html template.
    Parameters:
        request: HTTP request object.
    Returns: Rendered HTML template with news articles.

2.fetch_stock_news1(topics, days=1)

    Purpose: Fetches stock news from multiple sources based on specified topics and filters by publication date.
    Parameters:
        topics: List of topics to search for.
        days: Number of days to look back for news.
    Returns: List of news articles including source, title, summary, link, publication date, and image URL.

stock_news1(request)

    Purpose: Handles HTTP POST requests to fetch news from multiple sources and render the stock_news1.html template.
    Parameters:
        request: HTTP request object.
    Returns: Rendered HTML template with news articles from various sources.

## Notes

Ensure that you have the necessary permissions and network access to fetch RSS feeds from external sources.
The application uses deprecated RSS feed URLs for some sources. Update these URLs as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
