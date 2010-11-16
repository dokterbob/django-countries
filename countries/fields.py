from django.db.models import ForeignKey
from django.utils.translation import ugettext_lazy as _


class CountryField( ForeignKey ):
    """
    A ForeignKey to select a country.
    
    This field has a default value for verbose_name and a shortcut for 
    switching blank/null to True
    """
    def __init__( self, **kwargs ):
        kwargs.setdefault( 'verbose_name', _( 'countries' ) )
        if kwargs.pop( 'required', None ) == False:
            kwargs[ 'blank' ] = True
            kwargs[ 'null' ] = True
        super( CountryField, self ).__init__( 'countries.Country', **kwargs )

