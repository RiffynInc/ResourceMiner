from __future__ import division
from pymongo import MongoClient
from lxml import etree
from bson import json_util
from functools import partial
import time

def q(string):
    return string.join(["\"","\""])

pretty_json = partial(json_util.dumps, sort_keys=True,indent=4, separators=(',', ': '))

uri = 'mongodb://mozsprint:plos@ec2-52-26-49-156.us-west-2.compute.amazonaws.com/plos'
client = MongoClient(uri)
db = client.plos

colls = ['plos_biol',
         'plos_genet',
         'plos_med',
         'plos_negl_trop_dis',
         'plos_one',
         'plos_pathog']

thesaurus_file = 'data/terms/plosthes.2015-1.extract.xml'
thesaurus = etree.parse(thesaurus_file)

terms = [t.text for t in thesaurus.getiterator() if t.tag == 'T']
terms.sort()

# terms_out = u'\n'.join(terms)
#
# with open('data/terms/subject_areas.txt', 'wb') as f:
#     f.write(terms_out.encode('utf8'))


coll = 'plos_one'
results = db[coll].find({})


# Use for # subjects > # papers

# start_count = results.count()
# count = 0
# start_time = time.time()
#
# counts = {}
# for res in results:
#     count += 1
#     pct = count / start_count * 100
#     t1 = time.time() - start_time
#     t = t1 * (start_count / count - 1)
#     status = "{0} papers ({1}%) complete, {2} seconds remaining.".format(count, round(pct,1), int(t))
#     print status
#     for subject in res['subjects']:
#         if subject in counts:
#             counts[subject] += 1
#         else:
#             counts[subject] = 1
#


# Use for # papers > # subjects

start_count = len(terms)
count = 0
start_time = time.time()

counts = {}
for term in terms:
    count += 1
    pct = count / start_count * 100
    t1 = time.time() - start_time
    t = t1 * (start_count / count - 1)
    status = "{0} terms ({1}%) complete, {2} seconds remaining.".format(count, round(pct,1), int(t))
    print status
    counts[term] = db.plos_biol.find( { 'subjects': term } ).count()


file_out = '.'.join(['results/subjects_count', coll, 'json'])
with open(file_out, 'wb') as f:
    f.write(pretty_json(counts).encode('utf8'))
