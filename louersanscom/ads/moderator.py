#-*- coding: utf-8 -*-
from geoads.contrib.moderation.moderator import AdModerator
from moderation import moderation
from .models import HomeForRentAd


moderation.register(HomeForRentAd, AdModerator)
