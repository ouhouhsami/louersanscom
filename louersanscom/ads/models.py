#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.http import QueryDict
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string

from geoads.models import AdSearch, AdSearchResult
from geoads.contrib.moderation.models import ModeratedAd
from geoads.contrib.moderation.register import moderated_geoads_register


HABITATION_TYPE_CHOICES = (
    ('0', _(u'Appartement')),
    ('1', _(u'Maison')),
)

HEATING_CHOICES = (
    ('1', _(u'Individuel gaz')),
    ('2', _(u'Individuel électrique')),
    ('3', _(u'Collectif gaz')),
    ('4', _(u'Collectif fuel')),
    ('5', _(u'Collectif réseau de chaleur')),
    ('13', _(u'Autres'))
)

PARKING_CHOICES = (
    ('1', _(u'Place de parking')),
    ('2', _(u'Box fermé')),
)


class HomeForRentAd(ModeratedAd):
    """
    HomeFormRentAd model
    """
    price = models.PositiveIntegerField(_(u"Loyer"))
    colocation = models.BooleanField(_(u"Colocation possible"))
    furnished = models.TextField(_(u"Habitation meublée"), null=True, blank=True)
    habitation_type = models.CharField(_(u"Type de bien"), max_length=1, choices=HABITATION_TYPE_CHOICES)
    surface = models.IntegerField(_(u"Surface habitable"))
    surface_carrez = models.IntegerField(_(u"Surface Loi Carrez"), null=True, blank=True)
    nb_of_rooms = models.PositiveIntegerField(_(u"Nombre de pièces"))
    nb_of_bedrooms = models.PositiveIntegerField(_(u"Nombre de chambres"))
    housing_tax = models.IntegerField(_(u"Taxe d'habitation"), null=True, blank=True)
    maintenance_charges = models.IntegerField(_(u'Charges'), null=True, blank=True)
    ground_surface = models.IntegerField(_(u'M²'), null=True, blank=True)
    floor = models.PositiveIntegerField(_(u'Etage'), null=True, blank=True)
    ground_floor = models.BooleanField(_(u'Rez de chaussé'))
    top_floor = models.BooleanField(_(u'Dernier étage'))
    not_overlooked = models.BooleanField(_(u'Sans vis-à-vis'))
    elevator = models.BooleanField(_(u"Ascenceur"))
    intercom = models.BooleanField(_(u"Interphone"))
    digicode = models.BooleanField(_(u"Digicode"))
    doorman = models.BooleanField(_(u"Gardien"))
    heating = models.CharField(_(u"Chauffage"), max_length=2, choices=HEATING_CHOICES, null=True, blank=True)
    duplex = models.BooleanField(_(u"Duplex"))
    terrace = models.IntegerField(_(u"Terrasse"), null=True, blank=True)
    balcony = models.IntegerField(_(u"Balcon"), null=True, blank=True)
    separate_dining_room = models.BooleanField(_(u"Cuisine séparée"))
    separate_toilet = models.IntegerField(_(u"Toilettes séparés"), null=True, blank=True)
    bathroom = models.IntegerField(_(u"Salle de bain"), null=True, blank=True)
    shower = models.IntegerField(_(u"Salle d'eau (douche)"), null=True, blank=True)
    parking = models.CharField(_(u"Parking"), max_length=2, choices=PARKING_CHOICES, null=True, blank=True)
    orientation = models.CharField(_(u"Orientation"), max_length=255, null=True, blank=True)

    default_filterset = 'louersanscom.ads.filtersets.HomeForRentAdFilterSet'

    def _icon(self):
        return "/static/img/apartment.png"
    icon = property(_icon)

    def get_full_description(self, instance=None):
        return _(u"location-%s-%spieces-%se_par_mois-%sm2") % (self.get_habitation_type_display(), 
                                               self.nb_of_rooms, 
                                               self.price, self.surface)
    def __unicode__(self):
        return render_to_string('geoads/resume.html', {'ad':self})

    def get_absolute_url(self):
        return reverse('view', args=[str(self.slug)])

    class Meta:
        app_label = 'ads'


class HomeForRentAdSearch(AdSearch):
    """
    this class acts as proxy for AdSearch model
    """
    def __unicode__(self):
        search = QueryDict(self.search, mutable=True)
        print search
        if 'habitation_type' in search:
            search['habitation_type'] = [HABITATION_TYPE_CHOICES[int(i)][1] for i in search['habitation_type']]
        return render_to_string('geoads/search_resume.html', {'search':search})

    class Meta:
        proxy = True


class HomeForRentAdSearchResult(AdSearchResult):
    """
    This class acts as proxy for AdPotentialBuyersView model
    This is a way to get the above __unicode__ for related HomeForSaleAdSearch instance
    """
    @property
    def ad_search(self):
        # joel cross proposition
        # http://stackoverflow.com/questions/3891880/django-proxy-model-and-foreignkey
        return HomeForRentAdSearch.objects.get(id=self.ad_search_id)
        # below approach should be better, without hitting db may be, but doesn't work
        #new_inst = HomeForSaleAdSearch()
        #new_inst.__dict__ = super(HomeForSaleAdSearch, self).ad_search.__dict__
        #return new_inst

    class Meta:
        proxy = True


moderated_geoads_register(HomeForRentAd)






