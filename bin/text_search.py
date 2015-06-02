from pymongo import MongoClient
from functools import partial

uri = 'mongodb://mozsprint:plos@ec2-52-26-49-156.us-west-2.compute.amazonaws.com/plos'
client = MongoClient(uri)
db = client.plos

coll = ['plos_biol',
        'plos_genet',
        'plos_med',
        'plos_negl_trop_dis',
        'plos_one',
        'plos_pathog']


def methods_search_base(term, database, collection='plos_biol', limit=50):
    query = {
        "$text": {"$search": term}
    }

    return database[collection].find(query, limit=limit)

methods_search = partial(methods_search_base, database=db)

"""

"""
