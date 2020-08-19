import requests
from bs4 import BeautifulSoup as soup

# arguments order as follows -- > func(URL, class_of_newsBody, args->(sub classes), kw->(tagType =[tag name, property ]
def real_estate_stories(url, main_class, *args, **kwargs):
    request = requests.get(url)
    page = soup(request.content, 'html.parser')

    all_headlines = page.find(class_=main_class)

    if args:
        for arg in args:
            print(arg)
            all_headlines = [headline.find(class_=arg) for headline in all_headlines]

    if kwargs:
        for key, values in kwargs.items():
            if key == 'meta':
                all_headlines = all_headlines.find_all(key, itemprop=values)
                all_headlines = [heads['content']  for heads in all_headlines]

            # defining Explicitly for "a" tags
            if key == 'tag' and values == 'a':
                all_headlines = all_headlines.find_all('a')
                all_headlines = [heads['href'] for heads in all_headlines]

            # defining for all other tags except "a"
            if key == 'tag' and values != 'a':
                all_headlines = all_headlines.find_all(values)

    # Final output
    for url in all_headlines:
        if 'https' in url:
            print(url)


# New web sites cab be added here (direct link to latest news)
liveMint = 'https://www.livemint.com/topic/real-estate'
realty = 'https://realty.economictimes.indiatimes.com/latest-news'
magicBricks = 'https://content.magicbricks.com/property-news/pune-real-estate-news-industry-news'


real_estate_stories(liveMint, 'listView', meta=['url'])
real_estate_stories(realty, 'wdgt', tag='a')
real_estate_stories(magicBricks, 'leftContainer', tag='a')
