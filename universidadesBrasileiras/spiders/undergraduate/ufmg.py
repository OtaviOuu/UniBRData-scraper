from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response


from ...items import UniversidadesbrasileirasItem


class UFMG(Spider):
    name = "ufmg-undergraduate"
    base_url = "https://www.ufmg.br"

    def start_requests(self) -> Iterable[Request]:

        yield Request(
            url=f"{self.base_url}/prograd/cursos-de-graduacao/",
            callback=self.coursesPage,
        )

    def coursesPage(self, response: Response):
        # TODO: Tratar EAD
        campus = response.css(".content-text a::attr(href)").getall()[1:-1]

        self.logger.info(f"{campus}")

        yield from response.follow_all(urls=campus, callback=self.extractPrograms)

    def extractPrograms(self, response: Response):
        programs = response.css("#main li a::text").getall()

        for programName in programs:
            item = UniversidadesbrasileirasItem()

            item["program"] = programName
            item["universityShortName"] = "UFMG"
            item["universityLongName"] = "Universidade Federal de Minas Gerais"
            item["state"] = "Minas Gerais"

            yield item
