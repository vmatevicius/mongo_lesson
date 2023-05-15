from pymongo import MongoClient
from typing import Dict, Any

class TaskManager():
    def __init__(self, host:str, port:int, db_name:str, collection_name: str):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def create_task(self, task: Dict[str, Any]) -> str:
        result = self.collection.insert_one(task)
        return str(result.inserted_id)        