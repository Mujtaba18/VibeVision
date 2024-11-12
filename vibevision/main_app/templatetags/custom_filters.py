# custom_filters.py
from django import template

register = template.Library()

@register.filter
def format_duration(duration):
    try:
        minutes = int(duration.split(':')[0])
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours}h {remaining_minutes:02d}m"
    except (ValueError, IndexError):
        return duration  # Return the original value if parsing fails


@register.filter
def has_now_showing(movies):
    return any(movie.status == "Now Showing" for movie in movies)

@register.filter
def has_coming_soon(movies):
    return any(movie.status == "Coming Soon" for movie in movies)
