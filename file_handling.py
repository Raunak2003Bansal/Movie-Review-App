import json
import os
from scraper import reviews
from summary import review_summary

CACHE_FILE = "movie_reviews.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_cache(data):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def exists_in_cache(url):
    cache = load_cache()
    for item in cache:
        if item["url"] == url:
            return item  # return entire entry from cache
    return None


def add_to_cache(entry):
    cache = load_cache()
    cache.append(entry)
    save_cache(cache)


def get_review_data(url: str):
    cached = exists_in_cache(url)

    if cached:
        print("\n📌 Found in cache! No scraping required.\n")
        return cached

    print("\n⚡ Not in cache. Scraping IMDb page...\n")
    review_data,title = reviews(url)

    if not review_data:
        return None

    # average rating
    try:
        ratings = [int(r["rating"].split("/")[0]) for r in review_data]
        avg_rating = sum(ratings) / len(ratings)
    except Exception:
        avg_rating = None

    # simple summary: first review
    review = ""
    for i in review_data:
        review = review+ i["review"]
    summary = review_summary(reviews=review)
    #summary = review_data[0]["review"][:300] if review_data else "No summary available"

    # TODO later: extract actual movie name
    movie_name = title

    entry = {
        "url": url,
        "name": movie_name,
        "rating": round(avg_rating, 1) if avg_rating else "N/A",
        "summary": summary
    }

    add_to_cache(entry)
    return entry