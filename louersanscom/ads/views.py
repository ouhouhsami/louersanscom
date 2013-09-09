#-*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy
from django.middleware.csrf import get_token

from geoads.views import AdSearchView

from models import HomeForRentAd


class HomeForRentAdSearchView(AdSearchView):
    model = HomeForRentAd

    def get_custom_append_msg(self):
        return _(u'<br/> <a class="btn btn-primary" href="%s">Inscrivez-vous</a> pour \
            créer une alerte email ou déposer une demande de location \
            et être contacté directement par les propriétaires.' % reverse_lazy('userena_signup'))

    def get_no_results_msg(self):
        msg = super(HomeForRentAdSearchView, self).get_no_results_msg()
        if not self.request.user.is_authenticated():
            return msg + self.get_custom_append_msg()
        return msg

    def get_results_msg(self):
        msg = super(HomeForRentAdSearchView, self).get_results_msg()
        if not self.request.user.is_authenticated():
            return msg + self.get_custom_append_msg()
        else:
            if self.ad_search_form:
                save_search_form = '''
                    <form method="POST" action="" class="form-inline" role="form">
                        %s <input type='hidden' name='csrfmiddlewaretoken' value='%s'>
                        <input type="submit" class="btn btn-primary" value="Enregistrer la recherche" />
                    </form>
                ''' % (self.ad_search_form, get_token(self.request))
                return msg + save_search_form
            else:
                return None
