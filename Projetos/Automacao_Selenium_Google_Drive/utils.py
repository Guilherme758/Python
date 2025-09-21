from selenium import webdriver
import json

def get_settings():
    with open("settings.json", mode = 'r', encoding='utf-8') as f:
        settings = f.read()
        return json.loads(settings)

def start_driver():
    settings = get_settings()

    options = webdriver.ChromeOptions().add_experimental_option("prefs", {
            "download.default_directory": settings['Settings']['DownloadFolder']
        })

    return webdriver.Chrome(options=options)