import os
from loguru import logger
from django import template
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from pytest import mark

register = template.Library()


# NAVBAR BOTTOM
## Button
@register.inclusion_tag("components/nav_button.html")
def nav_buttom_component(tooltip, icon, url, left=False, right=False):
    if left:
        leftright = "rounded-l-full"
    elif right:
        leftright = "rounded-r-full"
    else:
        leftright = ""
    return {"tooltip": tooltip, "icon": icon, "leftright": leftright, "url": url}


@register.simple_tag()
def liters_field_component(id, ph, field_name, name):
    html = f"""
        <span class="text-black mr-2 w-full">
            {name}
        </span>
        <div class="flex w-full">
            <input type="number"
                   class="w-36 text-black text-right rounded-md h-8 pr-10 appearence-none"
                   placeholder="{ph} lts."
                   name="{field_name}"
                   id="{id}"
            />
        </div>

    """

    return mark_safe(html)


@register.simple_tag()
def camera_icon_component(name, label_id):
    # hidden input field for file upload and a camera svg icon instead
    html = f"""
        <div class="pl-10 w-10">
            <input type="file"
                accept="image/*"
                capture="camera"
                class="hidden"
                name="{name}"
                id="{label_id}"
            />
            <label for="{label_id}" class="cursor-pointer">
                <svg class="w-8 h-8 p-1"
                    fill="#000000"
                    viewBox="0 0 32 32"
                    version="1.1"
                    xmlns="http://www.w3.org/2000/svg">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier"><title>photo</title>
                        <path d="M0 28v-20q0-0.832 0.576-1.408t1.44-0.576h4q0.8 0 1.408-0.576t0.576-1.44 0.576-1.408 1.44-0.576h12q0.8 0 1.408 0.576t0.576 1.408 0.576 1.44 1.44 0.576h4q0.8 0 1.408 0.576t0.576 1.408v20q0 0.832-0.576 1.44t-1.408 0.576h-28q-0.832 0-1.44-0.576t-0.576-1.44zM6.016 16q0 2.048 0.768 3.904t2.144 3.168 3.2 2.144 3.872 0.8q2.72 0 5.024-1.344t3.648-3.648 1.344-5.024-1.344-4.992-3.648-3.648-5.024-1.344q-2.016 0-3.872 0.8t-3.2 2.112-2.144 3.2-0.768 3.872zM10.016 16q0-2.464 1.728-4.224t4.256-1.76 4.256 1.76 1.76 4.224-1.76 4.256-4.256 1.76-4.256-1.76-1.728-4.256z">
                    </path></g>
                </svg>
            </label>
        </div>
    """

    return mark_safe(html)


@register.simple_tag()
def fuel_type_component(color, short):
    html = f"""
        <div class="w-18 px-2 text-xxs ml-2 rounded-full border-white border-2 whitespace-nowrap flex justify-center items-center"
             style="background:{color}">
            {short}
        </div>
    """

    return mark_safe(html)
