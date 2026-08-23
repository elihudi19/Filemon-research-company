from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def lfield(context, obj, field_prefix):
    """
    Inaonyesha nyanja sahihi (name_en au name_sw) kulingana na lugha
    iliyochaguliwa na mtumiaji. Matumizi: {% lfield sector "name" %}
    """
    request = context.get("request")
    lang = getattr(request, "LANG", "en") if request else "en"
    value = getattr(obj, f"{field_prefix}_{lang}", None)
    if not value:
        value = getattr(obj, f"{field_prefix}_en", "")
    return value


@register.filter
def video_embed_url(url):
    """
    Inabadilisha link ya kawaida ya YouTube kuwa link ya 'embed'
    inayoweza kuonekana moja kwa moja kwenye ukurasa.
    """
    import re

    if not url:
        return ""

    match = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]{11})", url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    return url
