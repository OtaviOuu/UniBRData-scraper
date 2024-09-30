from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response


from ...items import UniversidadesbrasileirasItem


class UFCG(Spider):
    name = "ufcg-undergraduate"
    baseUrl = "https://portal.ufcg.edu.br"

    def start_requests(self) -> Iterable[Request]:

        yield Request(
            url=f"{self.baseUrl}/graduacao",
            callback=self.extractPrograms,
        )

    def extractPrograms(self, response: Response):
        programs = response.css("#cursos a::text").getall()

        for program in programs:
            item = UniversidadesbrasileirasItem()

            item["universityShortName"] = "UFCG"
            item["universityLongName"] = "Universidae Federal de Campina Grande"
            item["state"] = "Paraíba"

            # TODO: Pipeline para remover lixo
            item["program"] = program.strip()

            yield item
