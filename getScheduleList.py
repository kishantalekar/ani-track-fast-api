from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


"""
<div class="lc-timetable-timeslot lc-timeslot-past" data-controller="timeslot" data-timestamp="1709324520" data-timetable-day-target="timeslot">
    <div class="lc-time-slot__line"></div><div class="lc-timetable-timeslot__content">
    <div class="lc-timetable-timeslot__time text-sm">
    <span class="lc-time">
    <span data-timeslot-target="time">1:52 AM</span>
    </span> 
    <time class="text-xs text-base-content/75" data-controller="countdown" data-style="short" data-timestamp="1709324520"></time></div>
    <div class="lc-timetable-anime-block" data-controller="schedule-anime" data-schedule-anime-id="1966" data-schedule-anime-ranges="[399,399]" 
    data-schedule-anime-release-date-value="1709324520" data-schedule-anime-title="Bonobono (TV 2016)" data-timeslot-target="anime">
    <img alt="Bonobono (TV 2016)" class="lc-tt-poster row-span-3" data-schedule-anime-target="poster" decoding="async" height="80" 
    loading="lazy" src="https://u.livechart.me/anime/1966/poster_image/d16566d5a5802d8d1fa288ff0740bb26.png/small.jpg" 
    srcset="https://u.livechart.me/anime/1966/poster_image/d16566d5a5802d8d1fa288ff0740bb26.png/small.jpg 1x, 
    https://u.livechart.me/anime/1966/poster_image/d16566d5a5802d8d1fa288ff0740bb26.png/large.jpg 2x" width="56"/>
    <a class="text-sm font-medium line-clamp-2 link-hover lc-tt-anime-title" data-schedule-anime-target="preferredTitle" href="/anime/1966" title="Bonobono (TV 2016)">Bonobono (TV 2016)</a>
    <a class="lc-tt-release-label text-xs text-base-content/75 truncate link-hover" href="/anime/1966/schedules/857">
    <span class="font-medium">EP399</span> · TV (JP)</a>
 
"""


def getSchedules():
    site = "https://www.livechart.me/schedule?layout=timetable"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    scheduleList = [

    ]

    timetable = soup.find('div', {'class': 'lc-timetable'})

    # present slot
    timetable_present = timetable.find(
        'div', {'class': 'lc-timetable-day lc-today'})
    time_table_day = timetable_present.find(
        'div', {'class': 'lc-timetable-day__heading'}).text.strip()

    timetable_presentslots = timetable_present.find_all(
        'div', {'class': 'lc-timetable-timeslot'})

    present_list = []

    for timetable_presentslot in timetable_presentslots:
        time = timetable_presentslot.find(
            'div', {'class': 'lc-timetable-timeslot__time'})
        if not time:
            continue
        time = time.find('span', {'class': 'lc-time'}).find('span').text

        innner_list = []
        timetable_anime_blocks = timetable_presentslot.find_all(
            'div', {'class': 'lc-timetable-anime-block'})

        for timetable_anime_block in timetable_anime_blocks:
            name = timetable_anime_block.find(
                'a', {'class': 'lc-tt-anime-title'})
            name = name.text if name else name

            episode_no = timetable_anime_block.find(
                'a', {'class': 'lc-tt-release-label'}).find('span')
            episode_no = episode_no.text if episode_no else 'N/A'
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
        'div', {'class': 'lc-timetable-day lc-future'})

    for timetable_future_list in timetable_future_lists:
        try:
            time_table_day = timetable_future_list.find(
                'div', {'class': 'lc-timetable-day__heading'}).text.strip()

            timetable_fututelots = timetable_future_list.find_all(
                'div', {'class': 'lc-timetable-timeslot'})

            future_list = []

            for timetable_futurelot in timetable_fututelots:
                time = timetable_futurelot.find(
                    'div', {'class': 'lc-timetable-timeslot__time'})

                if not time:
                    continue
                time = time.find(
                    'span', {'class': 'lc-time'}).find('span').text
                innner_list = []
                timetable_anime_blocks = timetable_futurelot.find_all(
                    'div', {'class': 'lc-timetable-anime-block'})

                for timetable_anime_block in timetable_anime_blocks:

                    name = timetable_anime_block.find(
                        'a', {'class': 'lc-tt-anime-title'})
                    name = name.text if name else name

                    episode_no = timetable_anime_block.find(
                        'a', {'class': 'lc-tt-release-label'}).find('span')
                    episode_no = episode_no.text if episode_no else 'N/A'
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
# printSchedules(schedules)
