#!/usr/bin/env python3
''''
insert_new_document
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document in a collection
    '''
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
