#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def main():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_c = client.logs.nginx

    n_logs = nginx_c.count_documents({})
    print(f"{n_logs} logs")
    methods: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for m in methods:
        c: int = nginx_c.count_documents({"method": m})
        print(f"\tmethod {m}: {c}")

    st_c: int = nginx_c.count_documents({"method": "GET", "path": "/status"})
    print(f"{st_c} status check")
    print("IPs:")
    top_ips = nginx_c.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
        ]
    )

    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
        

if __name__ == "__main__":
    main()
