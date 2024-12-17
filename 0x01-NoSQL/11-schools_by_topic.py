#!/usr/bin/env python3
''''
find a specific topic.
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of school having a specific topic.
    '''
    topic_filtered = {
        'topics': {
            '$in': [topic]
        },
    }
    return [doc for doc in mongo_collection.find(topic_filtered)]
