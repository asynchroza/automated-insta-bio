from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv, path
from time import sleep
from random import random


load_dotenv()
script_dir = path.dirname(path.abspath(__file__))

def get_lyrics() -> str:
    lines = []
    file_path = path.join(script_dir, "lyrics.txt")
    with open(file_path) as file:
        for line in file:
            lines.append(line.strip())

    return lines[int(random() * len(lines))]


def main():
    USERNAME = getenv("USERNAME")
    PASSWORD = getenv("PASSWORD")

    # chrome_driver_path = "./chromedriver_mac_arm64/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://instagram.com")

    sleep(3)
    username_input = driver.find_element(By.NAME, value="username")
    password_input = driver.find_element(By.NAME, value="password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    sleep(8)

    try:
        not_now_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Not Now')]"
        )

        not_now_button.click()
    except Exception as e:
        print(e)

    sleep(2)
    profile_link = driver.find_element(By.XPATH, f"//a[contains(@href, '{USERNAME}')]")
    profile_link.click()

    sleep(2)
    edit_profile = driver.find_element(
        By.XPATH, "//a[contains(text(), 'Edit Profile')]"
    )
    edit_profile.click()

    sleep(4)
    bio = driver.find_element(By.XPATH, "//textarea")
    bio.clear()

    value = get_lyrics()
    bio.send_keys(value)

    sleep(2)
    submit_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Submit')]")
    submit_button.click()

    sleep(3)
    driver.close()


if __name__ == "__main__":
    main()
