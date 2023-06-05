
import json
import polib

# Load translations from JSON file
with open("translations.json") as file:
    translations = json.load(file)

# Cycle through each language in the translations
for language in translations[list(translations.keys())[0]].keys():
    # Load the .po file for this language
    po_file_path = f'./portal/locale/{language}/LC_MESSAGES/django.po'
    po = polib.pofile(po_file_path)

    # Cycle through the translations in the .po file
    for entry in po:
        if entry.msgid in translations:
            entry.msgstr = translations[entry.msgid][language]

    # Save the modified .po file
    po.save(po_file_path)
