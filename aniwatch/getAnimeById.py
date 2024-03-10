from bs4 import BeautifulSoup
import requests
import json


def getAnimeById(id):
    print(id)
    url = f"https://aniwatch.to/{id}"
    response = requests.get(url)
    print(response.status_code)

    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            ani_detail = soup.find(id="ani_detail")

            anime_info = {

            }
            # getting the image
            try:
                anisc_poster = ani_detail.find(
                    'div', {'class': 'anisc-poster'})
                img_src = anisc_poster.find(
                    'img', {'class': 'film-poster-img'})['src']

                anime_info['img_src'] = img_src
            except Exception as e:
                print(1)
                print(e)

            # getting the name,film stats,description
            try:
                anisc_detail = ani_detail.find(
                    'div', {'class': 'anisc-detail'})

                name = anisc_detail.find(
                    'h2', {'class': 'film-name'}).text.strip()

                film_stats = anisc_detail.find('div', {'class': 'film-stats'})

                tick_pg = film_stats.find(
                    'div', {'class': 'tick-pg'}).text.strip()
            except Exception as e:
                print(2)
                print(e)

            try:
                tick_dub = film_stats.find(
                    'div', {'class': 'tick-dub'}).text.strip()
            except AttributeError:
                tick_dub = None

            try:
                tick_quality = film_stats.find(
                    'div', {'class': 'tick-quality'}).text.strip()
            except AttributeError:
                tick_quality = None

            try:
                tick_sub = film_stats.find(
                    'div', {'class': 'tick-sub'}).text.strip()

                film_stats_type_duration = film_stats.find_all(
                    'span', {'class': 'item'})
                ani_type = film_stats_type_duration[0].text.strip()
                ani_duration = film_stats_type_duration[1].text.strip()

                film_description = anisc_detail.find(
                    'div', {'class': 'film-description'})
                film_description = film_description.find(
                    'div', {'class': 'text'}).text.strip()
            except Exception as e:
                print(3)
                print(e)

            anime_info['name'] = name
            anime_info['tick_pg'] = tick_pg
            anime_info['tick_quality'] = tick_quality
            anime_info['tick_sub'] = tick_sub
            anime_info['tick_dub'] = tick_dub
            anime_info['ani_type'] = ani_type
            anime_info['ani_duration'] = ani_duration
            anime_info['description'] = film_description

        #    aired,premired,duration,status,genres,studios,producers
            try:
                anisc_info_wrap = ani_detail.find(
                    'div', {'class': 'anisc-info-wrap'})
                anisc_info = anisc_info_wrap.find(
                    'div', {'class': 'anisc-info'})
                anisc_info_items = anisc_info.find_all(
                    'div', {'class': "item item-title"})
                addtional_info = {}
                for row in anisc_info_items:
                    key = row.find('span', {'class': 'item-head'}).text.strip()
                    value = row.find('span', {'class': 'name'})
                    if value == None:
                        key = "genre_list"
                        value = row.find_all('a')
                        value = [text.text.strip() for text in value]
                    else:
                        value = value.text.strip()
                    addtional_info[key] = value

                genreList = anisc_info.find('div', {'class': 'item-list'})

            except Exception as e:
                print(4)
                print(e)

            anime_info["addtional_info"] = addtional_info

            # characters and voice actors
            try:

                try:
                    main_content = soup.find(id="main-content")

                    block_area_actors = main_content.find(
                        'section', {'class': 'block_area-actors'})
                    character_voice_actor_list = []
                    if block_area_actors != None:

                        block_actors_content = block_area_actors.find(
                            'div', {'class': 'block-actors-content'})
                        bac_list_wrap = block_actors_content.find(
                            'div', {'class': 'bac-list-wrap'})
                        bac_items = bac_list_wrap.find_all(
                            'div', {'class': 'bac-item'})

                        for bac_item in bac_items:
                            ltr = bac_item.find('div', {'class': 'ltr'})
                            name = ltr.find('h4', {'class': 'pi-name'}
                                            ).find('a').text.strip()

                            img_src = ltr.find('img')['data-src']

                            rtl = bac_item.find('div', {'class': 'rtl'})
                            name = rtl.find('h4', {'class': 'pi-name'}
                                            ).find('a').text.strip()
                            img_src = rtl.find('img')['data-src']
                            char_actor = {
                                "character_name": name,
                                "character_img_src": img_src, "actor_name": name,
                                "actor_img_src": img_src
                            }
                            character_voice_actor_list.append(char_actor)
                    else:
                        pass
                    anime_info['character_actor_list'] = character_voice_actor_list
                except Exception as e:
                    print(e)
                    print(10)

                try:
                    block_area_category = main_content.find(
                        'section', {'class': "block_area_category"})
                    tab_content = block_area_category.find('div', {
                        'class': 'tab-content'
                    })
                    film_list_wrap = tab_content.find(
                        'div', {'class': 'film_list-wrap'})
                    flw_items = film_list_wrap.find_all(
                        'div', {'class': 'flw-item'})
                    more_like_this = []
                    for flw_item in flw_items:
                        img_src = flw_item.find('img')['data-src']

                        try:
                            tick_rate = flw_item.find(
                                'div', {'class': 'tick-rate'}).text.strip()
                        except AttributeError:
                            tick_rate = None

                        try:
                            tick_dub = flw_item.find(
                                'div', {'class': 'tick-dub'}).text.strip()
                        except AttributeError:
                            tick_dub = None

                        try:
                            tick_sub = flw_item.find(
                                'div', {'class': 'tick-sub'}).text.strip()
                        except AttributeError:
                            tick_sub = None
                        try:
                            tick_eps = flw_item.find(
                                'div', {'class': 'tick-eps'}).text.strip()
                        except AttributeError:
                            tick_quality = None
                        name = flw_item.find(
                            'a', {'class': 'dynamic-name'}).text.strip()
                        url = flw_item.find(
                            'a', {'class': 'dynamic-name'})['href']

                        more_like_this.append({
                            "name": name,
                            "url": url,
                            "img_src": img_src,
                            "tick_dub": tick_dub,
                            "tick_sub": tick_sub,
                            "tick_eps": tick_eps,
                            "tick_rate": tick_rate,
                            "tick_quality": tick_quality,
                        })
                except Exception as e:
                    print(7)
                    print(e)
                anime_info['more_like_this'] = more_like_this
            except Exception as e:
                print(e)
                print(5)
            info = {
                "anime_info": anime_info
            }
            return info
        else:
            return response.status_code
    except Exception as e:
        print(e)


# # print(json.dumps(getTrending(), indent=2))
# result = getAnimeByid()
# if result:
#     print("Anime Information:")
#     print("-------------------")
#     for key, value in result.items():
#         if isinstance(value, list):
#             print(f"{key}:")
#             for item in value:
#                 print(f"  - {item}")
#         else:
#             print(f"{key}: {value}")
# else:
#     print("No anime information available.")

# print(result['character_actor_list'])
