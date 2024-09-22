import os
import importlib
from scrapy.crawler import CrawlerProcess
import scrapy

# Maneira bem estranha para rodar todos os spiders so mesmo tempo...


def main():
    undergraduate_path = os.path.join(
        os.path.dirname(__file__),
        "universidadesBrasileiras",
        "spiders",
        "undergraduate",
    )

    if not os.path.exists(undergraduate_path):
        print(f"Path does not exist: {undergraduate_path}")
        return

    process = CrawlerProcess(
        settings={
            "FEED_URI": "data.json",
            "FEED_FORMAT": "json",
            "FEED_EXPORT_ENCODING": "utf-8",
            "LOG_LEVEL": "INFO",  # Para ver logs
        }
    )

    for filename in os.listdir(undergraduate_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = (
                f"universidadesBrasileiras.spiders.undergraduate.{filename[:-3]}"
            )
            module = importlib.import_module(module_name)

            for spider_name in dir(module):
                spider = getattr(module, spider_name)
                if isinstance(spider, type) and issubclass(spider, scrapy.Spider):
                    process.crawl(spider)

    process.start()


if __name__ == "__main__":
    main()
