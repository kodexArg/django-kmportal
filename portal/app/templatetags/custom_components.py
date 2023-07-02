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


@register.inclusion_tag("components/std_button.html", takes_context=True)
def std_button_component(
    context,
    text,
    color="bg-pantone7689c",
    url="#",
    svg=None,
    is_left=False,
    is_right=False,
):
    return {
        "text": text,
        "color": color,
        "svg": svg,
        "url": url,
        "is_left": is_left,
        "is_right": is_right,
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


@register.inclusion_tag("components/row_fuelorder/main.html", takes_context=True)
def row_fuelorder_component(context, order):
    user = context["request"].user
    return {"user": user, "order": order}


@register.inclusion_tag("components/row_fuelorder/popup.html", takes_context=True)
def row_fuelorder_popup_component(context, order):
    return {"order": order}


@register.inclusion_tag("components/row_fuelorder/row.html", takes_context=True)
def row_fuelorder_row_component(context, order):
    return {"order": order}


@register.inclusion_tag("components/row_fuelorder/buttons.html", takes_context=True)
def row_fuelorder_buttons_component(context, order):
    return {"order": order}


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


@register.simple_tag()
def fueltank_component(fuel):
    """Returns a colored icon with gray text.
    long_fuel names and color_map should be checked in models.py
    """

    color_map = {
        "infinia_diesel": "#225722",
        "diesel_500": "#1453FF",
        "infinia": "#FF4500",
        "super": "#ffa500",
    }

    long_fuel = {
        "infinia_diesel": "Infinia Diesel",
        "infinia": "Infinia",
        "diesel_500": "Diesel 500",
        "super": "Super",
    }

    html = f"""
    <article class="flex flex-col items-center justify-center w-full aspect-1">
        <svg fill="{ color_map.get(fuel) }" viewBox="0 0 14 14" role="img" focusable="false" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
                <path
                    d="m 6.0976824,12.991789 c -1.51883,-0.1195 -2.4375,-0.3967 -2.97186,-0.8965 -0.22464,-0.2101 -0.263,-0.2767 -0.263,-0.4565 0,-0.1176 0.0538,-0.3016 0.12196,-0.4171 0.1181,-0.2002 0.12219,-0.2603 0.12924,-1.8971 0.007,-1.6607 0.005,-1.6954 -0.12196,-1.9773 -0.16215,-0.3599 -0.16344,-0.567 -0.005,-0.7689 0.12404,-0.158 0.12436,-0.1638 0.10651,-1.9255 -0.0167,-1.6455 -0.0252,-1.7765 -0.12442,-1.9025 -0.35934,-0.4569 0.14409,-1.129 1.063,-1.4193 0.87797,-0.2774 1.33909,-0.3301 2.8948,-0.3309 1.56582,-8.0003e-4 2.24417,0.073 3.0787406,0.3367 0.92859,0.293 1.3577,0.8773 1.03086,1.4036 -0.11514,0.1854 -0.12113,0.2649 -0.14255,1.8928 -0.0222,1.6831 -0.0212,1.701 0.10011,1.8713 0.193,0.2711 0.2044,0.597 0.0312,0.8925 l -0.14465,0.2468 0,1.6609 0,1.6609 0.14492,0.2593 c 0.5558,0.9945 -0.92476,1.6881 -3.7668606,1.7647 -0.48661,0.013 -1.00916,0.014 -1.16123,0 z m 2.64572,-0.5468 c 0.69387,-0.091 1.23259,-0.2388 1.5241406,-0.4183 l 0.18849,-0.116 -0.034,-1.993 c -0.0187,-1.0961 -0.0413,-1.9999 -0.0503,-2.0085 -0.009,-0.01 -0.22405,0.054 -0.4780106,0.1398 -0.25396,0.085 -0.66015,0.1729 -0.90265,0.1943 -0.24984,0.022 -0.44923,0.066 -0.46011,0.1021 -0.023,0.076 -0.0813,2.3538 -0.0824,3.2239 l -8.1e-4,0.6172 -0.23484,0.04 c -0.41484,0.07 -2.19566,0.035 -2.83413,-0.055 -0.98446,-0.1397 -1.80535,-0.4093 -2.01475,-0.6616 -0.10539,-0.127 -0.18245,-0.1068 -0.14168,0.037 0.12972,0.4579 1.12801,0.8056 2.7094,0.9436 0.63955,0.056 2.23735,0.03 2.81161,-0.045 z m 0.0362,-4.6395 c 0.6705,-0.092 1.03885,-0.1768 1.3654706,-0.3152 0.19636,-0.083 0.23771,-0.1293 0.2699,-0.3009 0.0341,-0.1817 -0.0208,-3.845 -0.0583,-3.8847 -0.008,-0.01 -0.26863,0.059 -0.5781306,0.1509 -0.30951,0.092 -0.71919,0.1832 -0.91041,0.2028 l -0.34768,0.036 -0.0363,1.4123 c -0.02,0.7767 -0.0363,1.6536 -0.0363,1.9486 l 0,0.5363 -0.29031,0.035 c -0.50973,0.061 -2.09611,0.035 -2.66806,-0.044 -1.16229,-0.1609 -1.753,-0.3486 -2.0955,-0.666 -0.11436,-0.106 -0.15487,-0.1196 -0.1779,-0.06 -0.093,0.2424 0.56443,0.6568 1.32037,0.8321 1.10347,0.2559 2.87201,0.3047 4.24318,0.117 z m 0.29933,-4.6437 c 0.63923,-0.122 1.2799806,-0.3608 1.5147506,-0.5647 0.11234,-0.098 0.18749,-0.1946 0.167,-0.2156 -0.0205,-0.021 -0.23201,0.049 -0.47003,0.1555 -0.7512206,0.3361 -1.7525506,0.4832 -3.2805406,0.482 -1.56137,0 -2.50912,-0.1448 -3.3276,-0.504 -0.21303,-0.093 -0.40175,-0.1556 -0.41939,-0.138 -0.0638,0.064 0.24218,0.326 0.53167,0.4557 0.33916,0.1519 1.07418,0.3333 1.63936,0.4045 0.60094,0.076 3.12696,0.023 3.64478,-0.075 z m -3.533,-0.8956 c 0.69058,-0.3277 -0.41654,-0.8125 -1.14937,-0.5033 -0.35173,0.1484 -0.34241,0.3912 0.0199,0.5182 0.27716,0.097 0.91083,0.089 1.12947,-0.015 z">
                </path>
            </g>
        </svg>
        <div>
            <p class="font-quicksand font-bold text-xxxs text-sky-900 text-center leading-none p-0.5">{ long_fuel.get(fuel) }</p>
        </div>
    </article>
    """

    return mark_safe(html)
