import asyncio
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
import re
url = "https://www.imdb.com/title/tt5463162/?ref_=hm_tpks_t_1_pd_tp1_pbr_ic"


def extract_h1_headings(markdown_text):
    pattern = r"^# (.+)$"  # Matches lines starting with "# "
    return re.findall(pattern, markdown_text, flags=re.MULTILINE)



def get_review_links(links):

    review_links = []
    count=0
    for link in links:
        if "review" in link['href']:
            split = link['href'].split("/")[-1]
            if split[0:7]=="reviews":
                review_links.append(link['href'])
    return review_links[0]

def clean_text(raw_text):
    # Regex to capture rating, title, and review text
    pattern = re.compile(
        r'(\d{1,2}/10)\s*'                 
        r'### (.*?)\n'                      
        r'(.+?)(?=Helpful•|\Z)',         
        re.DOTALL
    )

    review = []
    for match in pattern.finditer(raw_text):
        rating = match.group(1).strip()
        title = match.group(2).strip()
        review_text = match.group(3).strip()
    
        # Clean extra spaces, newlines
        review_text = re.sub(r'\s+', ' ', review_text)
    
        review.append({
            "rating": rating,
            "title": title,
            "review": review_text
        })

    return review


def remove_all_links(text):
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'<a [^>]*>(.*?)</a>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    return text

async def main(url:str):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        return result  # Show the first 300 characters of extracted text


result = asyncio.run(main(url))
#print(result.markdown)
print(extract_h1_headings(result.markdown))
