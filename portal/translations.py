import os
import polib
import json

BASE_DIR = "locale/{}/LC_MESSAGES/django.po"
LANGUAGES = ['en', 'es', 'pt']

# Load translations from the JSON file
with open("translations.json", "r") as f:
    translations = json.load(f)

for language in LANGUAGES:
    print(f"Processing {language}...")
    path = BASE_DIR.format(language)
    if os.path.exists(path):
        po = polib.pofile(path)
        for entry in po:
            # if entry.msgstr == "":
            # Check if the translation exists in the JSON file
            if entry.msgid in translations and language in translations[entry.msgid]:
                print(f'Setting translation for msgid "{entry.msgid}" in {language}')
                entry.msgstr = translations[entry.msgid][language]
            else:
                print(f'Translating msgid "{entry.msgid}" for language {language}')
                translation = input("Please enter the translation: ")
                entry.msgstr = translation
        po.save(path)
    else:
        print(f"File {path} does not exist.")
