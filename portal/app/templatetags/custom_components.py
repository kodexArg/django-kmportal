from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def testing_button(text, url="#"):
    """I'm leaving this for testing purposes, it's actually not used and shouldn't be used (harmless tho)"""

    tailwind_button = "block uppercase mx-auto shadow bg-indigo-800 hover:bg-indigo-700 focus:shadow-outline focus:outline-none text-white text-xs py-3 px-10 rounded"
    tailwind_div = "absolute duration-300 inset-0 w-full h-full transition-all scale-0 group-hover:scale-100 group-hover:bg-white rounded-2xl"

    div = f"<div class='{tailwind_div}'></div>"
    button = f"<button class='{tailwind_button}' style='z-index: 9999;'>{text}</button>"

    component = f"{button}"

    return mark_safe(component)

@register.inclusion_tag('components/test_button.html')
def testing_button_component(text):
    return {"text":text}