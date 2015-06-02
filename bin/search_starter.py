"""
Starter code for simple full-text search a PLoS journal. Calling search_plos['JOURNAL_NAME']('query')
returns a PyMongo Cursor iterable. See the Wiki in GitHub for more details:
https://github.com/RiffynInc/ResourceMiner/wiki/PLOS-database.

NOTE: The search_plos functions ONLY perform full-text searches of the
Materials and Methods section.
"""

from pymongo import MongoClient
from functools import partial

uri = 'mongodb://mozsprint:plos@ec2-52-26-49-156.us-west-2.compute.amazonaws.com/plos'
client = MongoClient(uri)
db = client.plos

colls = ['plos_biol',
         'plos_genet',
         'plos_med',
         'plos_negl_trop_dis',
         'plos_one',
         'plos_pathog']


def methods_search_base(term, database, collection, limit=50):
    query = {
        "$text": {"$search": term}
    }

    return database[collection].find(query, limit=limit)

search_plos = {}

for coll in colls:
    search_plos[coll] = partial(
        methods_search_base, database=db, collection=coll)
