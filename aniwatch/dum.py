from bs4 import BeautifulSoup
import requests


def get_trending_anime():
    trending_dict = {}
    url = "https://aniwatch.to/home"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        trending_list = soup.find(id="anime-trending")
        trending_items = trending_list.find_all('div', {'class': 'item'})

        for row in trending_items:
            anime_title = row.find('div', {'class': 'film-title'}).text.strip()
            anime_src = row.find(
                'img', {'class': 'film-poster-img'})['data-src']
            anime_id = row.find(
                'a', {'class': 'film-poster'}
            )['href']
            print(anime_id)

            trending_dict[anime_title] = anime_src
    else:
        print("Failed to get the data")

    return trending_dict


def get_featured_anime():
    trending_dict = {}
    url = "https://aniwatch.to/home"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        featured_container = soup.find(id="anime-featured")

        featured_list = featured_container.find_all(
            'div', {'class': 'col-xl-3 col-lg-6 col-md-6 col-sm-12 col-xs-12'})

        featured = {}
        for featured_rows in featured_list:

            featured_names_row = featured_rows.find_all(
                'a', {'class': 'dynamic-name'})
            featured_names = [row.text.strip() for row in featured_names_row]

            featured_images_row = featured_rows.find_all(
                'img', {'class': 'film-poster-img'})
            featured_images = [row["data-src"].strip()
                               for row in featured_images_row]

            featured_title = featured_rows.find(
                'div', {'class': 'anif-block-header'}).text

            featured[featured_title] = {
                "names": featured_names,
                "images": featured_images
            }

        for row in featured.keys():
            print('\n')
            print(row)
            print(featured[row]['names'])
            print(featured[row]['images'])
            print('\n')

        # print(featured_list[0].find('div',{'class':'anif-block-header'}).text)

        # featured_names = featured_list[0].find_all('a',{'class':'dynamic-name'})
        # featured_img = featured_list[0].find_all('img',{'class':'film-poster-img'})

        # for row in range(len(featured_names)):
        #     print(featured_names[row].text)
        #     print(featured_img[row]['data-src'])
        #     print('\n')

        # for row in featured_list:
        #     print(row)
        #     print('\n')
        # featured_title = featured_list.find_all('div',{'class':'anif-block-header'})
        # print(featured_title)

    else:
        print("Failed to get the data")

    return trending_dict

    pass


def print_trending_anime(trending_dict):
    for item in trending_dict.keys():
        print(f"Anime Title: {item}")
        print(f"Image Source: {trending_dict[item]}")
        print("\n")


if __name__ == "__main__":
    trending_anime_data = get_trending_anime()

    if trending_anime_data:
        print_trending_anime(trending_anime_data)

    # get_featured_anime()
