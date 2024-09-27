from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response

from ...items import UniversidadesbrasileirasItem


class USP(Spider):
    name = "usp-undergraduate"

    def start_requests(self) -> Iterable[Request]:
        baseUrl = "https://www5.usp.br/ensino/graduacao/"

        yield Request(url=baseUrl, callback=self.extractPrograms)

    def extractPrograms(self, response: Response):
        programSelector = ".elementor-accordion-title::text"
        programs = response.css(programSelector).getall()

        # cidades possiveis = ["Piracicaba", "Pirassununga", "São Carlos", "São Paulo", "Bauru", "Lorena", "Ribeirão Preto"]
        for program in programs:
            item = UniversidadesbrasileirasItem()

            item["universityShortName"] = "USP"
            item["universityLongName"] = "Universidade de São Paulo"

            item["program"] = program
            item["state"] = "São Paulo"
            # item['city'] = '[]'

            yield item
