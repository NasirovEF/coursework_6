from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "/media/other/no-img.png"


@register.filter()
def slice_description(text):
    if len(text) >= 70:
        return f"{text[0:70]}..."
    else:
        return text
