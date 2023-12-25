from bs4 import BeautifulSoup
import requests


def getFeatured():
    url = "https://aniwatch.to/home"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    url = "https://aniwatch.to/home"
    featured = {}

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        featured_container = soup.find(id="anime-featured")

        featured_list = featured_container.find_all(
            'div', {'class': 'col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12'})

        try:
            for featured_rows in featured_list:
                featured_title = featured_rows.find(
                    'div', {'class': 'anif-block-header'}).text.strip()
                featured[featured_title] = []

                for li in featured_rows.find_all('li'):
                    anime_name = li.find(
                        'a', {'class': 'dynamic-name'}).text.strip()
                    url = li.find(
                        'a', {'class': 'dynamic-name'})['href'].strip()
                    image_source = li.find(
                        'img', {'class': 'film-poster-img'})['data-src'].strip()

                    # Find episode counts
                    try:

                        ep_sub_count_elem = li.find(
                            'div', {'class': 'tick-item tick-sub'})
                        ep_sub_count = ep_sub_count_elem.text.strip() if ep_sub_count_elem else None

                        ep_dub_count_elem = li.find(
                            'div', {'class': 'tick-item tick-dub'})
                        ep_dub_count = ep_dub_count_elem.text.strip() if ep_dub_count_elem else None
                    except AttributeError as e:
                        print(e)

                    featured[featured_title].append({
                        'name': anime_name,
                        'url': url,
                        'img_src': image_source,
                        'ep_sub_count': ep_sub_count,
                        'ep_dub_count': ep_dub_count
                    })

        except AttributeError as e:
            print(e)
        return featured
    else:
        return []

# debugging
# for category, anime_list in featured.items():
#     print(f"\nCategory: {category}\n")
#     for anime in anime_list:
#         print(f"Anime Name: {anime['anime_name']}")
#         print(f"URL: {anime['url']}")
#         print(f"Image Source: {anime['image_source']}\n")
#         print(f"ep_dub_count: {anime['ep_dub_count']}\n")
#         print(f"ep_sub_count: {anime['ep_sub_count']}\n")
