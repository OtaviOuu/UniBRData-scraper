from typing import Iterable
from scrapy import Spider
from scrapy.http import Request, Response

# Não funciona =================================

from ...items import UniversidadesbrasileirasItem


class UFPE(Spider):
    name = "ufpe-undergraduate"

    def start_requests(self) -> Iterable[Request]:
        baseUrl = "https://www.ufpe.br/"

        yield Request(url=f"{baseUrl}/cursos", callback=self.extractPrograms)

    def extractPrograms(self, response: Response):
        programsTable = response.css("#layout-column_column-3")

        print(programsTable)
