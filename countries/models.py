from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country( models.Model ):
  """
  International Organization for Standardization (ISO) 3166-1 Country list
  
  Instance Variables:
   iso -- ISO 3166-1 alpha-2
   name -- Official country names (in all caps) used by the ISO 3166
   display_name -- Country names in title format
   sort_priority -- field that allows for customizing the default ordering
     0 is the default value, and the higher the value the closer to the 
     beginning of the list it will be.  An example use case would be you will
     primarily have addresses for one country, so you want that particular 
     country to be the first option in an html dropdown box.  To do this, you 
     would simply change the value in the json file or alter 
     country_grabber.py's priority dictionary and run it to regenerate 
     the json.  

  """
  iso = models.CharField( _( 'ISO alpha-2' ), max_length=2, primary_key=True  )
  name_official = models.CharField( _( 'Official Country Name' ), \
      max_length=128 )
  name = models.CharField( _( 'Country Name' ), max_length=128 )
  sort_priority = models.PositiveIntegerField( default=0 )
  
  class Meta:
    verbose_name = _( 'Country' )
    verbose_name_plural = _( 'Countries' )
    ordering = ( '-sort_priority', 'name', )
    
  class Admin:
    list_display = ( 'name', 'iso', )
    
  def __unicode__( self ):
    ''' Return the display form of the country name'''
    return _(self.name)
