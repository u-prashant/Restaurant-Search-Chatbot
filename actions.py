from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import mail


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "4d01872bf8cea4ef509bbd1c0d233b41"}
        # config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85}
        count = 0
        start = 0
        response = ""
        restaurants = []
        gotMaxRestro = False

        for i in range(20):
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), start, 20)
            d = json.loads(results)
            if d['results_found'] == 0:
                response = "no results"
                break
            else:
                for restaurant in d['restaurants']:
                    restaurant = [restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'],
                                  restaurant['restaurant']['user_rating']['aggregate_rating'],
                                  restaurant['restaurant']['average_cost_for_two']]
                    if price == 'low' and restaurant[3] <= 300:
                            restaurants.append(restaurant)
                            count = count + 1
                    elif price == 'mid' and restaurant[3] > 300 and restaurant[3] <= 700:
                            restaurants.append(restaurant)
                            count = count + 1
                    elif price == 'high' and restaurant[3] > 700:
                            restaurants.append(restaurant)
                            count = count + 1
                    if count == 5:
                        gotMaxRestro = True
                        break

            if gotMaxRestro:
                break

            start = start + 20

        restaurants = sorted(restaurants, key=lambda x: x[2], reverse=True)
        for restaurant in restaurants:
            response = response + "Found " + restaurant[0] + " in " + restaurant[1] + \
                       " has been rated " + restaurant[2] + "\n"

        dispatcher.utter_message("-----\n" + response)
        return [SlotSet('location', loc)]


class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "4d01872bf8cea4ef509bbd1c0d233b41"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        email = tracker.get_slot('email')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85}
        count = 0
        start = 0
        response = ""
        restaurants = []
        gotMaxRestro = False

        for i in range(20):
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), start, 20)
            d = json.loads(results)
            if d['results_found'] == 0:
                response = "no results"
                break
            else:
                for restaurant in d['restaurants']:
                    restaurant = [restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'],
                                  restaurant['restaurant']['user_rating']['aggregate_rating'],
                                  restaurant['restaurant']['average_cost_for_two']]
                    if price == 'low' and restaurant[3] <= 300:
                            restaurants.append(restaurant)
                            count = count + 1
                    elif price == 'mid' and restaurant[3] > 300 and restaurant[3] <= 700:
                            restaurants.append(restaurant)
                            count = count + 1
                    elif price == 'high' and restaurant[3] > 700:
                            restaurants.append(restaurant)
                            count = count + 1
                    if count == 10:
                        gotMaxRestro = True
                        break

            if gotMaxRestro:
                break

            start = start + 20

        restaurants = sorted(restaurants, key=lambda x: x[2], reverse=True)
        for restaurant in restaurants:
            response = response + "\n\n\n* Restaurant Name - " + str(restaurant[0]) + \
                                      "\n  Address - " + str(restaurant[1]) + \
                                      "\n  Avg. budget for 2 people - " + str(restaurant[3]) + \
                                      "\n  Ratings - " + str(restaurant[2])

        mail.send_mail(email, response)

        return [SlotSet('location', loc)]


