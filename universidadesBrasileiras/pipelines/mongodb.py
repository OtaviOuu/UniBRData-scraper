from itemadapter import ItemAdapter

from pymongo import MongoClient


class MongoDBPipeline:
    def open_spider(self, spider):
        self.client = MongoClient(spider.settings.get('MONGODB_URI'))
        self.db = self.client[spider.settings.get('MONGODB_DATABASE')]
        self.collection = self.db['test']
    

    def close_spider(self, spider):
        self.client.close()
        
        
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.collection.insert_one(adapter.asdict())
        print("🚀 Item inserido:", adapter.asdict())
        return item