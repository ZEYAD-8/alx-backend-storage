# ALX Backend Storage - NoSQL Project

This repository contains a set of Python scripts that interact with a MongoDB database. The scripts perform various tasks related to managing data in a MongoDB database.

## Installation and Setup

Before running the scripts, ensure you have the following prerequisites:

- Python 3.7
- PyMongo 3.10
- MongoDB installed and running on your system
- Git (optional, for cloning the repository)

To install PyMongo, you can use `pip`:

```bash
pip install pymongo==3.10
```

## Clone the Repository

If you haven't already, you can clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/alx-backend-storage.git
```

## Usage

### Task 0: List all databases

This script lists all databases in MongoDB.

```bash
./0-list_databases.py
```

### Task 1: Create a database

This script creates or uses the database `my_db`.

```bash
./1-use_or_create_database.py
```

### Task 2: Insert document

This script inserts a document into the `school` collection.

```bash
./2-insert.py
```

### Task 3: All documents

This script lists all documents in the `school` collection.

```bash
./3-all.py
```

### Task 4: All matches

This script lists all documents with the name "Holberton school" in the `school` collection.

```bash
./4-match.py
```

### Task 5: Count

This script displays the number of documents in the `school` collection.

```bash
./5-count.py
```

### Task 6: Update

This script adds a new attribute to all documents with the name "Holberton school" in the `school` collection.

```bash
./6-update.py
```

### Task 7: Delete by match

This script deletes all documents with the name "Holberton school" in the `school` collection.

```bash
./7-delete.py
```

### Task 8: List all documents in Python

This Python function lists all documents in a collection.

```python
from pymongo import MongoClient
from 8-all import list_all

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
schools = list_all(school_collection)

for school in schools:
    print("[{}] {}".format(school.get('_id'), school.get('name')))
```

### Task 9: Insert a document in Python

This Python function inserts a new document into a collection based on kwargs.

```python
from pymongo import MongoClient
from 8-all import list_all
from 9-insert_school import insert_school

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
print("New school created: {}".format(new_school_id))

schools = list_all(school_collection)
for school in schools:
    print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
```

### Task 10: Change school topics

This Python function changes all topics of a school document based on the name.

```python
from pymongo import MongoClient
from 8-all import list_all
from 10-update_topics import update_topics

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

schools = list_all(school_collection)
for school in schools:
    print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

update_topics(school_collection, "Holberton school", ["iOS"])

schools = list_all(school_collection)
for school in schools:
    print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
```

### Task 11: Where can I learn Python?

This Python function returns a list of schools having a specific topic.

```python
from pymongo import MongoClient
from 8-all import list_all
from 9-insert_school import insert_school
from 11-schools_by_topic import schools_by_topic

client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school

j_schools = [
    { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
    { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
    { 'name': "UCLA", 'topics': ["C", "Python"]},
    { 'name': "UCSD", 'topics': ["Cassandra"]},
    { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
]

for j_school in j_schools:
    insert_school(school_collection, **j_school)

schools = schools_by_topic(school_collection, "Python")
for school in schools:
    print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
```

### Task 12: Log stats

This Python script provides some statistics about Nginx logs stored in MongoDB.

```bash
./12-log_stats.py
```

## Credits

This project is part of the ALX Software Engineering program.