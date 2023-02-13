import logging
import random
import re
import time
from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(filename="/var/log/YouTuber/info.log", level=logging.INFO,
                    format='%(asctime)s %(name)s | %(levelname)s => %(message)s')


def random_line(input):
    lines = open(input).read().splitlines()
    return random.choice(lines)


f = open('/PYTHON/YouTuber/Input/ReverseProxy.txt', 'r')
proxies = f.readlines()
random.shuffle(proxies)

print("")
print("  +----------- START -----------+")

# Cycle
for i in range(1, 10):

    start = time.time()
    status = True

    VIDEO_ID = 'Ibhxp41-0QU'
    total_views = 0
    total_length = 0
    total_watched = 0
    elapsed_video = 0

    if len(proxies) == 0:
        f = open('/PYTHON/YouTuber/Input/ReverseProxy.txt', 'r')
        proxies = f.readlines()
        random.shuffle(proxies)

    PROXY = proxies[0]
    proxies.remove(PROXY)
    PROXY = PROXY.replace('\n', '')

    USERAGENT = random_line('/PYTHON/YouTuber/Input/UserAgent.txt')

    print("")
    print("  [+] %s" % i)
    print("  [+] %s" % PROXY)
    print("  [+] %s" % USERAGENT)

    options = webdriver.ChromeOptions()

    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("--disable-extensions");
    options.add_argument("--proxy-server=%s" % PROXY)
    options.add_argument("--user-agent=%s" % USERAGENT)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("--start-maximized")

    options.add_argument('--headless')
    # options.add_argument('--incognito')
    # options.add_argument('--mute-audio')
    options.add_argument("window-size={},{}".format(randint(600, 1900), randint(600, 1000)))

    # chrome_driver_binary = r"/PYTHON/YouTuber/Input/driver/chromedriver.exe"
    chrome_driver_binary = r"/PYTHON/YouTuber/Input/driver/chromedriver"

    chrome = webdriver.Chrome(chrome_driver_binary, options=options)

    url = 'https://www.youtube.com/watch?v=' + VIDEO_ID
    chrome.get(url)

    try:
        print("  [+] {}".format(chrome.title))

        time.sleep(20)
        start_video = time.time()
        WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()

        # chrome.find_element_by_class_name("ytp-time-display").click()
        chrome.find_element_by_class_name("ytp-volume-area").click()

        print("  [+] Title {}".format(chrome.title))

        total_views_text = chrome.find_element_by_class_name("yt-view-count-renderer").text
        total_views = re.findall(r'\d+', total_views_text)[0]
        print("  [+] Total Views: %s" % total_views)

        total_length = chrome.find_element_by_class_name("ytp-progress-bar").get_attribute("aria-valuemax")
        print("  [+] Video Length: %s seconds" % total_length)

        total_watched = chrome.find_element_by_class_name("ytp-progress-bar").get_attribute("aria-valuenow")
        print("  [+] Watched: %s seconds" % total_watched)

        # chrome.find_element_by_class_name("ytp-volume-area").click()
        # chrome.find_element_by_class_name("ytp-time-display").click()

        previous = 0
        while int(total_watched) < 40:

            time.sleep(randint(1, 3))
            chrome.find_element_by_tag_name('html').send_keys(Keys.END)
            time.sleep(randint(1, 3))
            chrome.find_element_by_tag_name('html').send_keys(Keys.HOME)
            time.sleep(randint(1, 3))

            for u in range(1, randint(5, 10)):
                chrome.execute_script("window.scrollTo(0,{})".format(randint(500, 5000)))
                time.sleep(randint(1, 5))

            chrome.find_element_by_tag_name('html').send_keys(Keys.HOME)

            time.sleep(randint(5, 10))

            chrome.find_element_by_class_name("ytp-volume-area").click()
            total_watched = chrome.find_element_by_class_name("ytp-progress-bar").get_attribute("aria-valuenow")
            print("  [+] Watched: %s seconds" % total_watched)

            if int(total_watched) > previous:
                previous = int(total_watched)
            else:
                status = False
                print("  [X] Video Watch Time not increasing")
                break

            # pprint(int(total_watched))

    except:
        print('error')

    try:
        end = time.time()
        # elapsed = format(end - start, '.2f')
        # elapsed_video = format(end - start_video, '.2f')

        elapsed = int(end - start)
        elapsed_video = int(end - start_video)

        print("  [+] Total Time: %s seconds" % elapsed)

        chrome.find_element_by_class_name("ytp-volume-area").click()

        total_views_text = chrome.find_element_by_class_name("yt-view-count-renderer").text
        total_views = re.findall(r'\d+', total_views_text)[0]
        print("  [+] Total Views: %s" % total_views)

        total_length = chrome.find_element_by_class_name("ytp-progress-bar").get_attribute("aria-valuemax")
        print("  [+] Video Length: %s seconds" % total_length)

        total_watched = chrome.find_element_by_class_name("ytp-progress-bar").get_attribute("aria-valuenow")
        print("  [+] Watched: %s seconds" % total_watched)

        if status:
            logging.info(" Video ID: {} | Views: {} | Length: {} | Watched: {} <> {} | Time: {} ".format(VIDEO_ID, total_views, total_length, total_watched, elapsed_video, elapsed))

        else:
            logging.error("Video ID: {} | Views: {} | Length: {} | Watched: {} <> {} | Time: {} ".format(VIDEO_ID, total_views, total_length, total_watched, elapsed_video, elapsed))


    except:
        print("  [+] ERROR ")
        logging.warning("Video ID: {} | Views: {} | Length: {} | Watched: {} <> {} | Time: {} ".format(VIDEO_ID, total_views, total_length, total_watched, elapsed_video, elapsed))

    chrome.quit()
