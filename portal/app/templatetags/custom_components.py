from loguru import logger
from django import template
from django.utils.safestring import mark_safe
import os


register = template.Library()

TAILWIND_TOP_VALUE = {
    "1": "top-[0.5rem]",
    "2": "top-[7rem]",
    "3": "top-[11.5rem]",
    "4": "top-[16rem]",
    "5": "top-[20.5rem]",
    "6": "top-[25rem]",
}


@register.inclusion_tag("components/welcome_card.html")
def welcome_card_component(choice):
    return {"choice": choice}


@register.inclusion_tag("components/google_button.html")
def google_button_component():
    return {}


@register.inclusion_tag("components/module_title.html")
def module_title_component(title):
    return {"title": title}


@register.inclusion_tag("components/menu_button.html", takes_context=True)
def menu_button_component(context, pos, side, icon="", size="small", url="#", style=""):
    """Each menu button including Icons, Flags and avatars"""
    top = TAILWIND_TOP_VALUE[pos]
    if not os.path.isfile(f"static/svg/{icon}.svg"):
        icon = "question"  # TODO: Replace question with a known good icon
    user = context["request"].user  # Get the user object from the context

    return {
        "icon": icon,
        "size": size,
        "pos": top,
        "side": side,
        "url": url,
        "style": style,
        "user": user,  # Pass the user object to the template
    }


@register.inclusion_tag("components/fuel_order_row.html", takes_context=True)
def fuel_order_row_component(context, order):
    user = context["request"].user
    return {"user": user, "order": order}


@register.simple_tag()
def input_field_component(
    label,
    name,
    type="text",
    value="",
    label_size="w-1/3",
    size="w-2/3",
    required=True,
):
    required_html = "required" if required else ""
    html = f"""
        <div class="flex justify-between space-x-1 items-center">
            <label
                class="text-xs text-pantone7689c {label_size} align-baseline text-left"
                >{ label }</label>
            <input
                class="border rounded p-1 {size} text-sm font-rubik"
                type="{ type }" 
                name="{ name }" 
                placeholder="{ label }"
                value="{ value }"
                { required_html }
                >
        </div>
    """
    return mark_safe(html)


@register.simple_tag()
def checkbox_component(label, name, checked=False):
    checked_html = "checked" if checked else ""
    html = f"""
        <div class="flex w-full space-x-2 items-center">
            <input
                class="border rounded p-1"
                type="checkbox" 
                name="{ name }" 
                { checked_html }
                >
            <label
                class="text-xs text-pantone7689c w-1/3 align-baseline text-left"
                >{ label }</label>
        </div>
    """
    return mark_safe(html)


@register.simple_tag()
def rbutton_component(caption, bg="bg-pantone7689c", fg="text-white", size=""):
    """Rounded button component"""
    html = f"""
        <button type="submit" class="{size} whitespace-nowrap rounded-full px-3 py-1 {bg} {fg} self-end font-quicksand font-bold text-sm">
            {caption}
        </button>
    """
    return mark_safe(html)
