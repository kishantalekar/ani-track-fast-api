from bs4 import BeautifulSoup
import requests


def get_categories(query: str):

    url = f"https://aniwatch.to/{query}"
    print(query)
    response = requests.get(url)
    genre_list = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        film_list_wrap = soup.find('div', {'class': 'film_list-wrap'})

        flw_items = film_list_wrap.find_all('div', {'class': 'flw-item'})
        try:
            for flw_item in flw_items:
                anime_name = flw_item.find(
                    'a', {'class': 'dynamic-name'}).text.strip()
                url = flw_item.find(
                    'a', {'class': 'dynamic-name'})['href'].strip()
                description_elem = flw_item.find(
                    'div', {'class': 'description'})
                description = description_elem.text.strip() if description_elem else None
                image_source = flw_item.find(
                    'img', {'class': 'film-poster-img'})['data-src'].strip()
                type = flw_item.find(
                    'span', {'class': 'fdi-item'}).text.strip()

                # Find episode counts
                try:
                    ep_sub_count_elem = flw_item.find(
                        'div', {'class': 'tick-item tick-sub'})
                    ep_sub_count = ep_sub_count_elem.text.strip() if ep_sub_count_elem else None

                    ep_dub_count_elem = flw_item.find(
                        'div', {'class': 'tick-item tick-dub'})
                    ep_dub_count = ep_dub_count_elem.text.strip() if ep_dub_count_elem else None
                except AttributeError as e:
                    print(e)

                genre_list.append({
                    "anime_name": anime_name,
                    "url": url,
                    "image_source": image_source,
                    "type": type,
                    "description": description,
                    "ep_sub_count": ep_sub_count,
                    "ep_dub_count": ep_dub_count
                })

        except AttributeError as e:
            print(e)
        return genre_list
    else:
        return []


# for flw_item in genre_list:
#     print(f"\nanime name :{flw_item['anime_name']}")
#     print(f"url :{flw_item['url']}")
#     print(f"image_source :{flw_item['image_source']}")
#     print(f"type :{flw_item['type']}")
#     print(f"description :{flw_item['description']}")
#     print(f"sub :{flw_item['ep_sub_count']}")
#     print(f"dub :{flw_item['ep_dub_count']}\n")
