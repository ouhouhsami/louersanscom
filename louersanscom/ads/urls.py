#-*- coding: utf-8 -*-
from .models import HomeForRentAd, HomeForRentAdSearch, HomeForRentAdSearchResult
from .forms import HomeForRentAdForm
from .views import HomeForRentAdSearchView

from sanscom.utils.urls import ads_urlpatterns

urlpatterns = ads_urlpatterns(HomeForRentAd, HomeForRentAdSearch,
							  HomeForRentAdSearchResult, HomeForRentAdForm, 
							  HomeForRentAdSearchView)
