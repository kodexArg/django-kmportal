import os
import time
from selenium import webdriver

""" Browser Reloader

    This script will check if the files in the portal folder have been modified.
    If so, it will refresh the portal page in chrome.

    There is probably an extension that does this...
"""

CHECK_EVERY_SECONDS = 2

def check_files_changed(path):
    check_time = time.time()
    chrome_driver_path = "/usr/share/bash-completion/completions/chrome"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get("http://127.0.0.1:8000/")
    
    while True:
        # Iterate through the subfolders in the path
        for foldername, subfolders, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith((".html", ".py")):
                    file_path = os.path.join(foldername, filename)
                    modified_time = os.path.getmtime(file_path)

                    if modified_time > check_time:
                        print(f"Changes detected! on file {file_path}")
                        check_time = time.time()
                        driver.refresh()
                        break

        # print(f"{time.strftime('%H:%M:%S')} - no changes detected")
        time.sleep(CHECK_EVERY_SECONDS)


if __name__ == "__main__":
    path_to_check = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "portal",
    )
    print(path_to_check)
    check_files_changed(path_to_check)
