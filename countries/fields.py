from django.db import models
from django.utils.translation import ugettext_lazy as _


class CountryFieldMixin(object):
    """
    Mixin class for `CountryField` and `CountriesField`.

    This field has a default value for verbose_name and a shortcut for
    switching blank/null to True
    """

    def __init__( self, **kwargs ):
        super(CountryFieldMixin, self ).__init__( 'countries.Country',
                                                 **kwargs)


class CountryField(CountryFieldMixin, models.ForeignKey):
    """
    A ForeignKey to select a country.
    """
    def __init__( self, **kwargs ):
        kwargs.setdefault( 'verbose_name', _( 'country' ) )

        super(CountryField, self ).__init__(**kwargs)

    def get_internal_type(self):
        return "ForeignKey"


class CountriesField(CountryFieldMixin, models.ManyToManyField):
    """
    A ManyToMany field to select multiple countries.
    """
    def __init__( self, **kwargs ):
        kwargs.setdefault( 'verbose_name', _( 'countries' ) )

        super(CountriesField, self ).__init__(**kwargs)

    def get_internal_type(self):
        return "ManyToManyField"


# rules for South migrations tool (for version >= 0.7)
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^countries\.fields\.CountryField"])
    add_introspection_rules([], ["^countries\.fields\.CountriesField"])
except ImportError:
    pass
