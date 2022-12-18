import scrapy

inst_wat_list = ["CBB", "Game", "Water", "IPR", "WCA", "MICRO"]
inst_wat_url = [
        "https://uwaterloo.ca/bioengineering-biotechnology/about/people",\
        "https://uwaterloo.ca/games-institute/about/people",\
        "https://uwaterloo.ca/water-institute/about/people",\
        "https://uwaterloo.ca/institute-polymer-research/about/people",\
        "https://uwaterloo.ca/astrophysics-centre/about/people/group/46", \
        "https://uwaterloo.ca/waterloo-centre-microbial-research/about/people"
        ]

wat_list_dict = dict(zip(inst_wat_list, inst_wat_url))
wat_list_dict


class AffiliateSpider(scrapy.Spider):
    name = 'affiliate'
    allowed_domains = ['uwaterloo.ca']

    custom_settings = {
        'FEEDS' : {
            'affiliation.json': {
                'format': 'json',
                'overwrite': True,
                'encoding': 'utf8'
            }
        }
    }

    def start_requests(self):
        start_urls = wat_list_dict

        for abbr in start_urls:
            request = scrapy.Request(url = start_urls[abbr], callback = self.parse)
            request.cb_kwargs['abbr_inst_name'] = abbr
            yield request
            # print((abbr, start_urls[abbr]))

            # yield scrapy.Request(url = start_urls[abbr], callback = self.parse)

    def parse(self, response, abbr_inst_name):
        personnel = response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
        inst_name = abbr_inst_name
        # inst_name = response.url.split("/")[3] 
        return {inst_name: personnel}

# scrapy crawl affiliate