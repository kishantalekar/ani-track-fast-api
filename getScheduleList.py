from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def getSchedules():
    site = "https://www.livechart.me/timetable"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    scheduleList = [

    ]

    timetable = soup.find('div', {'class': 'timetable'})

    # present slot
    timetable_present = timetable.find(
        'div', {'class': 'timetable-day today'})
    time_table_day = timetable_present.find(
        'div', {'class': 'timetable-day__heading'}).text.strip()

    timetable_presentslots = timetable_present.find_all(
        'div', {'class': 'timetable-timeslot'})

    present_list = []

    for timetable_presentslot in timetable_presentslots:
        time = timetable_presentslot.find(
            'div', {'class': 'timetable-timeslot__time'}).find('span', {'class': 'time'}).text.strip()
        innner_list = []
        timetable_anime_blocks = timetable_presentslot.find_all(
            'div', {'class': 'timetable-anime-block'})

        for timetable_anime_block in timetable_anime_blocks:
            name = timetable_anime_block.find('a', {'class': 'title'})
            name = name.text if name else name

            episode_no = timetable_anime_block.find(
                'div', {'class': 'footer'})
            episode_no = episode_no.text if episode_no else episode_no
            img_src = timetable_anime_block.find('img')
            img_src = img_src['src'] if img_src else img_src
            innner_list.append(
                {
                    "name": name,
                    "episode_no": episode_no,
                    "img_src": img_src,
                    "time": time

                }
            )
        present_list.append(innner_list)

    scheduleList.append({
        "day": time_table_day,
        "list": present_list,
        "isToday": True
    })

    # future schedule list
    timetable_future_lists = timetable.find_all(
        'div', {'class': 'timetable-day future'})

    for timetable_future_list in timetable_future_lists:
        try:
            time_table_day = timetable_future_list.find(
                'div', {'class': 'timetable-day__heading'}).text.strip()

            timetable_fututelots = timetable_future_list.find_all(
                'div', {'class': 'timetable-timeslot'})

            future_list = []
            for timetable_futurelot in timetable_fututelots:
                time = timetable_futurelot.find(
                    'div', {'class': 'timetable-timeslot__time'}).find('span', {'class': 'time'}).text.strip()
                innner_list = []
                timetable_anime_blocks = timetable_futurelot.find_all(
                    'div', {'class': 'timetable-anime-block'})

                for timetable_anime_block in timetable_anime_blocks:
                    name = timetable_anime_block.find('a', {'class': 'title'})
                    name = name.text if name else name

                    episode_no = timetable_anime_block.find(
                        'div', {'class': 'footer'})
                    episode_no = episode_no.text if episode_no else episode_no
                    img_src = timetable_anime_block.find('img')
                    img_src = img_src['src'] if img_src else img_src
                    innner_list.append(
                        {
                            "name": name,
                            "episode_no": episode_no,
                            "img_src": img_src,
                            "time": time

                        }
                    )
                future_list.append(innner_list)
            scheduleList.append({
                "day": time_table_day,
                "list": future_list,
                "isToday": False
            })

        except Exception as e:
            print(e)

    return scheduleList


# debugging
def printSchedules(schedules):
    for schedule in schedules:
        print(f"Day: {schedule['day']}")
        print(f"IsToday: {schedule['isToday']}")

        for timeslot in schedule['list']:
            for anime in timeslot:
                print(f"  Time: {anime['time']}")
                print(f"  Name: {anime['name']}")
                print(f"  Episode: {anime['episode_no']}")
                print(f"  Image Source: {anime['img_src']}")
                print("\n")


# Get schedules and print the data

# schedules = getSchedules()
