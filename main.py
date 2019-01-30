from selenium import webdriver
from time import sleep
from random import randint

browser = webdriver.Firefox()
browser.get('http://discordapp.com/login')
browser.find_element_by_css_selector("[type=email]").send_keys("adrijaned@gmail.com")
browser.find_element_by_css_selector("[type=password]").send_keys("CorrectHorseBatteryStaple")
browser.find_element_by_css_selector("[type=submit]").click()
while "activity" not in browser.current_url:
    pass
browser.get("https://discordapp.com/channels/270264625419911192/519493471220793345")
while True:
    sleep(125 + randint(0, 10))
    browser.find_element_by_tag_name("textarea").send_keys("g!- gooey-bridge" + webdriver.common.keys.Keys.RETURN)
