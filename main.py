import os
import importlib
import asyncio
from twisted.internet import asyncioreactor

# Força o uso do AsyncioSelectorReactor
asyncioreactor.install()

from scrapy.crawler import CrawlerProcess
import scrapy
import multiprocessing


def run_spider(spider):
    process = CrawlerProcess()
    process.crawl(spider)
    process.start()


def main():
    undergraduate_path = os.path.join(
        os.path.dirname(__file__),
        "universidadesBrasileiras",
        "spiders",
        "undergraduate",
    )

    spiders = []

    for filename in os.listdir(undergraduate_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = (
                f"universidadesBrasileiras.spiders.undergraduate.{filename[:-3]}"
            )
            module = importlib.import_module(module_name)

            for spider_name in dir(module):
                spider = getattr(module, spider_name)
                if isinstance(spider, type) and issubclass(spider, scrapy.Spider):
                    spiders.append(spider)

    processes = []
    for spider in spiders:
        p = multiprocessing.Process(target=run_spider, args=(spider,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
