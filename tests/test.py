import unittest
from app import property_handler
import json


class TestPropertyServices(unittest.TestCase):

    def test_get_properties_with_filter(self):
        f = open("resources/event_api_poperty.json")
        event = json.load(f)
        f.close()
        res = property_handler(event, None)
        self.assertEqual(res['statusCode'], 200)

    def test_get_properties_without_filter(self):
        f = open("resources/event_api_poperty_not_filters.json")
        event = json.load(f)
        f.close()
        res = property_handler(event, None)
        self.assertEqual(res['statusCode'], 200)

    def test_get_properties_filter_year(self):
        f = open("resources/event_api_poperty_year.json")
        event = json.load(f)
        f.close()
        res = property_handler(event, None)
        self.assertEqual(res['statusCode'], 200)
