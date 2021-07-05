from objects.TourList import TourList
from objects.OrderList import OrderList
from objects.CustomerList import CustomerList
import os
import pymongo
import json

class Lists(object):
    tour_list = TourList()
    order_list = OrderList()
    archive_tour_list = TourList()
    customer_list = CustomerList()

    client = pymongo.MongoClient()
    db = client['travelcompany']

    tour_coll = db['tours']
    order_coll = db['orders']
    archive_tour_coll = db['archive_tours']
    customer_coll = db['customers']

    def add_tour(t):
        Lists.tour_list.append(t)
        Lists.tour_coll.insert_one(t.to_dict())

    def add_archive_tour(t):
        Lists.archive_tour_list.append(t)
        Lists.archive_tour_coll.insert_one(t.to_dict())

    def add_order(o):
        Lists.order_list.append(o)
        Lists.order_coll.insert_one(o.to_dict())

    def add_customer(o):
        Lists.customer_list.append(o)
        Lists.customer_coll.insert_one(o.to_dict())

    def update_tour(t):
        Lists.tour_list.update(t)
        Lists.tour_coll.update_one({'ID': t.ID}, {'$set': t.to_dict()})

    def delete_tour(t):
        Lists.tour_list.delete(t)
        Lists.tour_coll.delete_one({'ID': t.ID})

    def delete_archive_tour(t):
        Lists.archive_tour_list.delete(t)
        Lists.archive_tour_coll.delete_one({'ID': t.ID})

    def load():
        dict0 = []
        for i in Lists.tour_coll.find():
            i.pop('_id')
            dict0.append(i)
        Lists.tour_list = TourList().from_dict(dict0)

        dict0 = []
        for i in Lists.order_coll.find():
            i.pop('_id')
            dict0.append(i)
        Lists.order_list = OrderList().from_dict(dict0)

        dict0 = []
        for i in Lists.archive_tour_coll.find():
            i.pop('_id')
            dict0.append(i)
        Lists.archive_tour_list = TourList().from_dict(dict0)

        dict0 = []
        for i in Lists.customer_coll.find():
            i.pop('_id')
            dict0.append(i)
        Lists.customer_list = CustomerList().from_dict(dict0)

    def save():
        Lists.tour_coll.delete_many({})
        Lists.order_coll.delete_many({})
        Lists.archive_tour_coll.delete_many({})
        Lists.customer_coll.delete_many({})

        if len(Lists.tour_list.to_dict()) > 0:
            Lists.tour_coll.insert_many(Lists.tour_list.to_dict())
        if len(Lists.order_list.to_dict()) > 0:
            Lists.order_coll.insert_many(Lists.order_list.to_dict())
        if len(Lists.archive_tour_list.to_dict()) > 0:
            Lists.archive_tour_coll.insert_many(Lists.archive_tour_list.to_dict())
        if len(Lists.customer_list.to_dict()) > 0:
            Lists.customer_coll.insert_many(Lists.customer_list.to_dict())

    def save_json():
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'resources', 'tours.json'), 'w') as file:
            file.write(json.dumps(Lists.tour_list.to_dict()))
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'resources', 'orders.json'), 'w') as file:
            file.write(json.dumps(Lists.order_list.to_dict()))
    
    def load_json():
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'resources', 'tours.json'), 'r') as file:
            Lists.tour_list = TourList().from_dict(json.loads(file.read()))
        with open(os.path.join(os.path.split(os.path.dirname(__file__))[0], 'resources', 'orders.json'), 'r') as file:
            Lists.order_list = OrderList().from_dict(json.loads(file.read()))