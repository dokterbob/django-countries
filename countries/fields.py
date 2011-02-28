from django.db import models
from django.utils.translation import ugettext_lazy as _


class CountryFieldMixin(object):
    """
    Mixin class for `CountryField` and `CountriesField`.

    This field has a default value for verbose_name and a shortcut for
    switching blank/null to True
    """

    def __init__( self, **kwargs ):
        kwargs.setdefault( 'verbose_name', _( 'countries' ) )
        if kwargs.pop( 'required', None ) == False:
            kwargs[ 'blank' ] = True
            kwargs[ 'null' ] = True
        super(CountryFieldMixin, self ).__init__( 'countries.Country',
                                                 **kwargs)


class CountryField(CountryFieldMixin, models.ForeignKey):
    """
    A ForeignKey to select a country.
    """
    pass


class CountriesField(CountryFieldMixin, models.ManyToManyField):
    """
    A ManyToMany field to select multiple countries.
    """

