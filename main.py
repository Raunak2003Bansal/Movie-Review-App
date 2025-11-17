import json
import os
from scraper import reviews
from file_handling import get_review_data



if __name__ == "__main__":
    url = input("Enter the URL of the movie : ")

    data = get_review_data(url)
    print(type(data))
    print("\n--- MOVIE INFO ---")
    print(f"Title   : {data['name']}")
    print(f"Rating  : {data['rating']}")
    print(f"Summary : {data['summary']['text']}\n")
