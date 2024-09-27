from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response


from ...items import UniversidadesbrasileirasItem

# navigation-section :nth-child(4) .menuspan9


class IME(Spider):
    name = "ime-undergraduate"
    base_url = "www.ime.eb.mil.br/"

    def start_requests(self) -> Iterable[Request]:
        yield Request(
            url=f"{self.base_url}/computacao/82-graduacao/graduacao/245-graduacao.html",
            callback=self.extractPrograms,
        )

    def extractPrograms(self, response: Response):

        # Removendo o "Curso Fundamental". Irrelevante por agora
        programsList = response.css(
            "#navigation-section :nth-child(4) .menuspan9 li::text"
        ).getall()

        item = UniversidadesbrasileirasItem()
        for program in programsList:

            item["universityShortName"] = "IME"
            item["universityLongName"] = "IME"
            # TODO: Jogar esse replace no pipeline
            item["program"] = program.replace("Eng.", "Engenharia")
            item["city"] = "São Jose dos Campos"
            item["state"] = "São Paulo"

            yield item
