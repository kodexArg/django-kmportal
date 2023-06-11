from django import template
from django.utils.safestring import mark_safe
import os


register = template.Library()

TAILWIND_TOP_VALUE = {
    "1": "top-2",
    "2": "top-28",
    "3": "top-44",
    "4": "top-60",
    "5": "top-[19rem]",
}

@register.inclusion_tag("components/welcome_card.html")
def welcome_card_component(choice):
    return {"choice": choice}

@register.inclusion_tag("components/google_button.html")
def google_button_component():
    return {}

## BUTTONS
# Menu Button
@register.inclusion_tag("components/menu_button.html")
def menu_button_component(icon, size, position, side, url):
    if not os.path.isfile(f"static/svg/{icon}.svg"):
        icon = "question"  # TODO: Replace question with a known good icon
    top = TAILWIND_TOP_VALUE[position]
    return {"icon": icon, "size": size, "position": top, "side": side, "url": url}

# Flags - change language button
@register.inclusion_tag("components/flag_button.html")
def flag_button_component(size, position, side, language_code):
    top = TAILWIND_TOP_VALUE[position]
    return {"size": size, "position": top, "side": side, "language_code": language_code}

# Avatar button
@register.inclusion_tag("components/avatar_button.html")
def avatar_button_component(icon, size, position, side, url):
    top = TAILWIND_TOP_VALUE[position]
    return {"icon": icon, "size": size, "position": top, "side": side, "url": url}

