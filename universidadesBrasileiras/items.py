from scrapy import Field, Item


class UniversidadesbrasileirasItem(Item):
    universityShortName = Field()
    universityLongName = Field()
    program = Field()
    state = Field()
