from django import template
from django.template.defaultfilters import stringfilter

register = template.Library( )

@register.filter
@stringfilter
def iso_flag( iso, flag_path=u'' ):
  """
  Returns path to the ISO 3166-1 alpha-2 country code flag image.

  Arguments:
    iso -- the ISO-alpha-2 country code
    flag_path -- Given in the form '<path relative to media root>/%s.png'     
      and is appended to settings.MEDIA_URL.  If a valid flag_path is not
      given, tries to use settings.COUNTRIES_FLAG_PATH (default 'flags/%s.png')

  Usage:
    {{ user_profile.country.iso|iso_flag }}
    {{ user_profile.country.iso|iso_flag:"appmedia/flags/%s.png" }}
  
  """
  from countries.utils.isoflag import iso_flag
  return iso_flag( iso, flag_path )

