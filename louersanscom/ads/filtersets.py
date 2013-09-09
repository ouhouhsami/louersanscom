#-*- coding: utf-8 -*-
import django_filters
import floppyforms as forms

from sanscom.utils.widgets import LeafletWidget, IndifferentNullBooleanSelect, SpecificRangeWidget
from sanscom.utils.filters import OpenRangeNumericFilter
from geoads.filters import LocationFilter, BooleanForNumberFilter

from models import HomeForRentAd, HABITATION_TYPE_CHOICES

from sanscom.utils.widgets import BootstrapSpecificRangeWidget
from sanscom.utils.filtersets import NicerFilterSet


class HomeForRentAdFilterSet(NicerFilterSet):
    """
    FilterSet for HomeForRentAd
    Used to filter home for rent ads in the home page
    """
    habitation_type = django_filters.ChoiceFilter(label="Type", choices=HABITATION_TYPE_CHOICES, widget=forms.Select())
    price = OpenRangeNumericFilter(label="Loyer", widget=BootstrapSpecificRangeWidget({'size': '6'}, '€/mois'))
    nb_of_rooms = OpenRangeNumericFilter(label="Nb. pièces", widget=SpecificRangeWidget({'size': '6'}))
    nb_of_bedrooms = OpenRangeNumericFilter(label="Chambres", widget=SpecificRangeWidget({'size': '6'}))
    surface = OpenRangeNumericFilter(label="Surface", widget=BootstrapSpecificRangeWidget({'size': '6'}, 'm²'))
    furnished = BooleanForNumberFilter(label="Meublé", widget=IndifferentNullBooleanSelect())
    elevator = BooleanForNumberFilter(label="Ascenceur", widget=IndifferentNullBooleanSelect())
    colocation = BooleanForNumberFilter(label="Colocation", widget=IndifferentNullBooleanSelect())
    location = LocationFilter(widget=LeafletWidget(), required=False)

    def __init__(self, *args, **kwargs):
        super(HomeForRentAdFilterSet, self).__init__(*args, **kwargs)
        self.form.fields['location'].widget = LeafletWidget(ads=[], fillColor="pink", strokeColor="#9d81a1")

    class Meta:
        model = HomeForRentAd
