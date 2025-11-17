import streamlit as st
from file_handling import get_review_data
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.set_page_config(page_title="Movie Review Summary", page_icon="🎬")

st.title("🎥 Movie Review Summary App")
st.write("Enter a movie URL to fetch IMDb rating and summary")

# Input URL box
url = st.text_input("Movie URL", placeholder="https://www.imdb.com/title/tt1234567/")

if st.button("Get Movie Summary"):
    if not url.strip():
        st.error("⚠️ Please enter a valid movie URL.")
    else:
        with st.spinner("Fetching movie details... ⏳"):
            try:
                data = get_review_data(url)

                st.success("Movie details fetched successfully!")

                st.subheader(f"🎬 {data['name']}")
                st.write(f"⭐ **Rating**: {data['rating']} / 10")

                summary = data["summary"]["text"]
                st.subheader("📝 Summary")
                st.write(summary)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
