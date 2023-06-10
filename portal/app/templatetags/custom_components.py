from django import template
from django.utils.safestring import mark_safe
import os


register = template.Library()

TAILWIND_TOP_VALUE = {
    "1": "top-6",  # Warning: if 'top-6' then in *_button.html will be h-20 h-20
    "2": "top-28",
    "3": "top-44",
    "4": "top-60",
    "5": "top-[19rem]",
}


@register.simple_tag
def testing_button(text, url="#"):
    """I'm leaving this for testing purposes, it's actually not used and shouldn't be used (harmless tho)"""

    tailwind_button = "block uppercase mx-auto shadow bg-indigo-800 hover:bg-indigo-700 focus:shadow-outline focus:outline-none text-white text-xs py-3 px-10 rounded"
    tailwind_div = "absolute duration-300 inset-0 w-full h-full transition-all scale-0 group-hover:scale-100 group-hover:bg-white rounded-2xl"

    div = f"<div class='{tailwind_div}'></div>"
    button = f"<button class='{tailwind_button}' style='z-index: 9999;'>{text}</button>"

    component = f"{button}"

    return mark_safe(component)


@register.inclusion_tag("components/test_button.html")
def testing_button_component(text):
    return {"text": text}


@register.inclusion_tag("components/menu_button.html")
def menu_button_component(icon, position, side, url):
    """Warning: Top-44, Top-60 and so on relies on 'safelist' on tailwind.config.js"""
    if not os.path.isfile(f"static/svg/{icon}.svg"):
        icon = "question"  # TODO: Replace question with a known good icon
    top = TAILWIND_TOP_VALUE[position]
    return {"icon": icon, "position": top, "side": side, "url": url}


@register.inclusion_tag("components/flag_button.html")
def flag_button_component(position, side, language_code):
    top = TAILWIND_TOP_VALUE[position]
    return {"position": top, "side": side, "language_code": language_code}
