#-*- coding: utf-8 -*-
import floppyforms as forms

from django.utils.translation import ugettext as _

from sanscom.utils.widgets import BooleanExtendedNumberInput, BooleanExtendedInput

from models import HomeForRentAd
from geoads.contrib.moderation.forms import BaseModeratedAdForm


class HomeForRentAdForm(BaseModeratedAdForm):
    
    class Meta:
        model = HomeForRentAd
        widgets = {
            'habitation_type':forms.Select,
            'price': forms.NumberInput,
            'maintenance_charges': forms.NumberInput,
            'surface':forms.NumberInput,
            'surface_carrez':forms.NumberInput,
            'nb_of_rooms':forms.NumberInput,
            'nb_of_bedrooms':forms.NumberInput,
            'user_entered_address':forms.TextInput,
            'colocation':forms.CheckboxInput,
            'furnished':BooleanExtendedInput(attrs={'label': _(u"Habitation meublée"),
                                                    'detail': _(u"donner le détail")}),
            'housing_tax':forms.NumberInput,
            'ground_surface':forms.NumberInput,
            'floor':forms.NumberInput,
            'ground_floor':forms.CheckboxInput,
            'top_floor':forms.CheckboxInput,
            'not_overlooked':forms.CheckboxInput,
            'duplex':forms.CheckboxInput,
            'elevator':forms.CheckboxInput,
            'intercom':forms.CheckboxInput,
            'digicode':forms.CheckboxInput,
            'doorman':forms.CheckboxInput,
            'heating':forms.Select,
            'parking':forms.Select,
            'terrace':BooleanExtendedNumberInput(attrs={'label': _(u"Terrasse"),
                                                        'detail': _(u"préciser la surface (m²)")}),
            'balcony':BooleanExtendedNumberInput(attrs={'label': _(u"Balcon"),
                                                        'detail': _(u"préciser la surface (m²)")}),
            'separate_dining_room':forms.CheckboxInput(),
            'separate_toilet':BooleanExtendedNumberInput(attrs={'label': _(u"Toilettes séparés"),
                                                                'detail': _(u"préciser leur nombre")}),
            'bathroom': BooleanExtendedNumberInput(attrs={'label': _(u"Salle de bain"),
                                                          'detail': _(u"préciser leur nombre")}),
            'shower':BooleanExtendedNumberInput(attrs={'label': _(u"Salle d'eau (douche)"),
                                                       'detail': _(u"préciser leur nombre")}),
            'description':forms.Textarea()
        }
        exclude = ('user', 'delete_date', 'location', 'address', 'visible')

    class Media:
        js = ('js/edit_form.js',)

