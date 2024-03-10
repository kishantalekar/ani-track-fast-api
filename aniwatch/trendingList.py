from bs4 import BeautifulSoup
import requests


def getTrending():

    url = "https://aniwatch.to/home"
    response = requests.get(url)

    trending = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        trending_container = soup.find(id="anime-trending")

        # Check if the trending container is found
        if trending_container:
            trending_items = trending_container.select(
                '.trending-list .swiper-slide.item-qtip')

            for item in trending_items:
                # Extract name
                name = item.find(
                    'div', {'class': 'film-title dynamic-name'}).text.strip()

                # Extract URL from anchor tag
                url = item.find('a', {'class': 'film-poster'})['href']

                # Extract image source
                img_src = item.find(
                    'img', {'class': 'film-poster-img'})['data-src']

                trending.append({"name": name, "url": url, "img_src": img_src})

            return trending

        else:
            return []
    else:
        return response.status_code
