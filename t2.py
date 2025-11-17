import asyncio
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
import re
from urllib.parse import urljoin
from scraper import reviews

def get_review_links(links):

    review_links = []
    count=0
    for link in links:
        if "review" in link['href']:
            split = link['href'].split("/")[-1]
            if split[0:7]=="reviews":
                review_links.append(link['href'])
    return review_links[0]

async def main(url:str):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        return result

url = input("Enter the URL")

review = reviews(url)

print(review[0])

    
