from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response


from ...items import UniversidadesbrasileirasItem


class UFSC(Spider):
    name = "ufsc-undergraduate"

    def start_requests(self) -> Iterable[Request]:
        baseUrl = "https://prograd.ufsc.br/cursos-de-graduacao-da-ufsc/"

        yield Request(url=baseUrl, callback=self.extractPrograms)

    def extractPrograms(self, response: Response):
        programsTable = response.css("tbody tr")

        for index, row in enumerate(programsTable):
            # Forma bizarra de pular a primeira linha da tabela
            if index == 0:
                continue

            item = UniversidadesbrasileirasItem()

            item["universityShortName"] = "UFSC"
            item["universityLongName"] = "Universidade Federal de Santa Catarina"

            item["program"] = row.css("td:nth-child(1) a::text").get()
            item["state"] = "Santa Catarina"

            yield item
