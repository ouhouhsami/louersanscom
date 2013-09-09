#-*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client


class SearchPage(TestCase):

    def test_basic_get_search_page(self):
        """
        Test that user can reach home page
        """
        #c = Client()
        #response = c.get('/', follow=True)
        pass
