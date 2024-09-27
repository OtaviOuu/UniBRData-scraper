from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response


from ...items import UniversidadesbrasileirasItem


class ITA(Spider):
    name = "ita-undergraduate"
    base_url = "http://www.ita.br"

    def start_requests(self) -> Iterable[Request]:
        yield Request(url=f"{self.base_url}/grad", callback=self.extractPrograms)

    def extractPrograms(self, response: Response):
        programsList = response.css("#dhtml_menu-3277-1 li a::text").getall()[1:]

        item = UniversidadesbrasileirasItem()
        for program in programsList:

            item["universityShortName"] = "ITA"
            item["universityLongName"] = "Instituto Tecnológico de Aeronáutica"
            item["program"] = program.replace("Eng.", "Engenharia")
            item["state"] = "São Paulo"

            yield item
