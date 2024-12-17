#!/usr/bin/env python3
''''
list_all
'''


def list_all(mongo_collection):
    '''
    List all documents in Python
    '''
    return [doc for doc in mongo_collection.find()]
