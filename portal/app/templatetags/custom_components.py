from django import template
from django.utils.safestring import mark_safe
import os


register = template.Library()

TAILWIND_TOP_VALUE = {
    "1": "top-[1.4rem]",
    "2": "top-[6rem]",
    "3": "top-[9.5rem]",
    "4": "top-[13rem]",
    "5": "top-[16.5rem]",
    "6": "top-[20rem]",
}


@register.inclusion_tag("components/welcome_card.html")
def welcome_card_component(choice):
    return {"choice": choice}


@register.inclusion_tag("components/google_button.html")
def google_button_component():
    return {}


@register.inclusion_tag("components/menu_button.html", takes_context=True)
def menu_button_component(context, pos, side, icon="", size="small", url="#", style=""):
    """Each menu button including Icons, Flags and avatars
    """
    top = TAILWIND_TOP_VALUE[pos]
    if not os.path.isfile(f"static/svg/{icon}.svg"):
        icon = "question"  # TODO: Replace question with a known good icon
    user = context['request'].user  # Get the user object from the context
    return {
        "icon": icon,
        "size": size,
        "pos": top,
        "side": side,
        "url": url,
        "style": style,
        "user": user,  # Pass the user object to the template
    }

