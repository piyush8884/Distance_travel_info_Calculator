import os
from itertools import chain
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

from random import randint
from selenium.webdriver.support.ui import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

List_of_all = []
options = Options()

options.add_argument("--start-fullscreen")

#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

List_of_all = []
options = Options()
# options.add_argument("--window-size=1920x1080")
options.add_argument("--start-fullscreen")
# options.add_argument("--verbose")
options.add_argument("--headless")
# options.add_argument("--start-maximized")

# Get the current window size
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
from google_maps import urls
# driver.set_network_conditions(
#                 offline=False,
#                 latency=5000,  # Additional latency (ms)
#                 download_throughput=100 * 1024,  # Maximal download throughput (bytes/s)
#                 upload_throughput=100 * 1024,  # Maximal upload throughput (bytes/s)
#             )
# def find_dist(Place_1, Place_2):
# Place_1 = input("Enter origin city: ") + ',india'
# Place_2 = input("Enter destination city: ") + ',india'
# # Place_1 = "goa"+','+"india"
# # Place_2 = "bangalore"+','+"india"
# print(Place_1)
# print(Place_2)
# if Place_1 and Place_2:
#     if Place_1 != Place_2:
#         print("We are searching. Please wait...")
#         driver.get(urls.maps)
#         print("driver open")
#     else:
#         raise Exception("Origin and destination cannot be the same.")
# else:
#     raise Exception("Origin and/or destination not entered.")

