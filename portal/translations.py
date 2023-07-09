import os
import polib
import json
import subprocess
from loguru import logger
import sys
import shutil

BASE_DIR = "locale/{}/LC_MESSAGES/"
LANGUAGES = ["en", "es", "pt"]
PO_FILENAME = "django.po"
MO_FILENAME = "django.mo"


def load_translations(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def delete_files(language):


    po_path = os.path.join(BASE_DIR.format(language), PO_FILENAME)
    mo_path = os.path.join(BASE_DIR.format(language), MO_FILENAME)

    if os.path.isfile(po_path):
        os.remove(po_path)
        logger.info(f"Deleted {po_path}")
    else:
        logger.warning(f"{PO_FILENAME} not found at path: {po_path}. Continuing.")

    if os.path.isfile(mo_path):
        os.remove(mo_path)
        logger.info(f"Deleted {mo_path}")
    else:
        logger.warning(f"{MO_FILENAME} not found at path: {mo_path}. Continuing.")


def run_makemessages():
    try:
        subprocess.run(
            ["python", "manage.py", "makemessages", "-a"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        logger.info("makemessages -a command executed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error occurred during makemessages -a command: {e}")
        sys.exit(1)


def process_translations(language, translations):
    logger.info(f"Processing language <{language}>...")
    missing_entries = []
    path = BASE_DIR.format(language) + "django.po"  # Add the filename to the path
    if os.path.exists(path):
        po = polib.pofile(path)

        for entry in po:
            if entry.msgid in translations and language in translations[entry.msgid]:
                entry.msgstr = translations[entry.msgid][language]
            else:
                missing_entries.append(entry.msgid)
        po.save(path)
        logger.info(f"Translations processed successfully for {language}.")
        if missing_entries:
            logger.warning(f"Missing translations: {missing_entries}")
    else:
        logger.error(f"File {path} does not exist for {language}. Continuing.")
        sys.exit(1)


def add_missing_keys(translations, language):
    missing_keys_found_in_json = []

    po_path = os.path.join(BASE_DIR.format(language), PO_FILENAME)
    po = polib.pofile(po_path)

    for key, value in translations.items():
        found = False
        for entry in po:
            if entry.msgid == key:
                found = True
                break
        if not found:
            missing_keys_found_in_json.append(key)
            entry = polib.POEntry(msgid=key, msgstr=value.get(language, ""))
            po.append(entry)

    if missing_keys_found_in_json:
        logger.warning(f"Missing keys found in translations.json for {language}: {missing_keys_found_in_json}")
        po.save(po_path)
        logger.info(f"Added missing keys to {po_path} for {language}.")
    else:
        logger.info(f"No missing keys for {language}. All correct.")



def run_compilemessages():
    try:
        subprocess.run(
            ["python", "manage.py", "compilemessages"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        logger.info("compilemessages command executed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error occurred during compilemessages command: {e}")
        sys.exit(1)


def main():
    # load the json file
    translations = load_translations("translations.json")

    # clean the .mo and .po files
    confirm = input(f"Delete old files? (y/n): ")
    if confirm.lower() == "y":
        for language in LANGUAGES:
            delete_files(language)
    run_makemessages()

    # process the .po files
    for language in LANGUAGES:
        process_translations(language, translations)
    
    # add missing keys to the .po files
    for language in LANGUAGES:
        add_missing_keys(translations, language)

    # compile the .po files
    run_compilemessages()


if __name__ == "__main__":
    main()
