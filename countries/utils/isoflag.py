from django.conf import settings

def iso_flag( iso, flag_path=u'' ):
  """
  Returns path to the ISO 3166-1 alpha-2 country code flag image.

  Arguments:
    iso -- the ISO-alpha-2 country code
    flag_path -- Given in the form '<path relative to media root>/%s.png'     
      and is appended to settings.MEDIA_URL.  If a valid flag_path is not
      given, tries to use settings.COUNTRIES_FLAG_PATH (default 'flags/%s.png')
  
  """
  if not settings.MEDIA_URL or not iso:
    return u''
  
  iso = iso.lower( ).strip( )
  try:
    # flag_path should have a %s specifier in it
    flag = flag_path % ( iso )
  except ( ValueError, TypeError ):
    flag_path = getattr( settings, 'COUNTRIES_FLAG_PATH', u'flags/%s.png' )
    try:
      flag = flag_path % ( iso )
    except ( ValueError, TypeError ):
      return u''
    
  return u''.join( ( settings.MEDIA_URL, flag ) )
