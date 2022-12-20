import scrapy
from scrapy.spiders import Rule, CrawlSpider
# from scrapy.item import Institute

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

views_row_name = ['IQC', 'CAMJ', 'CPTT', 'WAT.AI', 'Climate']
views_row_url = [
        "https://uwaterloo.ca/institute-for-quantum-computing/contacts?title=&group%5B66%5D=66",\
        "https://uwaterloo.ca/centre-advanced-materials-joining/contacts?title=&group[72]=72",
        "https://uwaterloo.ca/centre-pavement-transportation-technology/contacts",\
        "https://uwaterloo.ca/artificial-intelligence-institute/contacts?title=",\
       "https://uwaterloo.ca/climate-institute/profiles?title=&field_uw_ct_profile_type_target_id%5B44%5D=44"
       ]
views_row_dict = dict(zip(views_row_name, views_row_url))
views_row_dict

tbody_name = ['CTN', 'CPI']
tbody_url = ["https://uwaterloo.ca/cybersecurity-privacy-institute/about/people/researchers", 
    "https://uwaterloo.ca/centre-for-theoretical-neuroscience/about/people/faculty"]
tbody_dict = dict(zip(tbody_name, tbody_url))
tbody_dict

# WICI: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
# WIN: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
field_item_name = ['WICI', 'WIN']
field_item_url = ["https://uwaterloo.ca/complexity-innovation/people/affiliate-researchers/affiliate-researchers-university-waterloo", 
    "https://uwaterloo.ca/institute-nanotechnology/our-people-0/our-members"
    ]
field_item_dict = dict(zip(field_item_name, field_item_url))
field_item_dict


# WISE:  response.xpath('//div[@class="ig-item"]//h2/a/text()').getall()
WISE = "WISE"
WISE_url = "https://wise.uwaterloo.ca/team"
wise_dict = {WISE: WISE_url}

# CCMIC: response.xpath('//h2[@class="anchor-name"]/a/text()').get()     
CCMIC = "CCMIC"
CCMIC_url = "https://uwaterloo.ca/computational-mathematics/people-profiles/category/55"
ccmic_dict = {CCMIC: CCMIC_url}

# GHPI: response.xpath('//div[@class="uw-copy-text"]//h2/a/text()').getall()
GHPI = "GHPI"
GHPI_url = "https://uwaterloo.ca/global-health-policy-innovation-research-centre/our-people"
ghip_dict = {GHPI: GHPI_url}

# WISA: response.xpath('//div[contains(@class, "block-layout-builder")]//h2/text()').getall()
WISA = "WISA"
WISA_url = "https://uwaterloo.ca/sustainable-aeronautics/our-people/members"
wisa_dict = {WISA: WISA_url}

inst_groups = {
    "wat_list_group" : {
        "name-url" : wat_list_dict,
        "xpath" : '//div[@class="entry clearfix"]//h2/a/text()'
    },

    "views_row_group": {
        "name-url" : views_row_dict,
        "xpath" : '//div[@class="views-row"]//h2/a/text()'
    },
    "tbody_group": {
        "name-url" : tbody_dict,
        "xpath" : '//tbody/tr/td[1]/a/text()'
    },
    "field_item_group": {
        "name-url" : field_item_dict,
        "xpath" : '//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()'
    },
    "wise_group": {
        "name-url" : wise_dict,
        "xpath": '//div[@class="ig-item"]//h2/a/text()'
    },
    "ccmic_group": {
        "name-url": ccmic_dict,
        "xpath": '//h2[@class="anchor-name"]/a/text()'
    },
    "ghip_group": {
        "name-url": ghip_dict,
        "xpath": '//div[@class="uw-copy-text"]//h2/a/text()'
    },
    "wisa_group": {
        "name-url": wisa_dict,
        "xpath": '//div[contains(@class, "block-layout-builder")]//h2/text()'
    }

}
# inst_groups

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
        start_urls = inst_groups

        for group in start_urls:
            group_info = start_urls[group]
            name_url_pair = group_info["name-url"]
            custom_xpath = group_info["xpath"]

            for abbr in name_url_pair:
                request = scrapy.Request(url = name_url_pair[abbr], callback = self.parse)
                request.cb_kwargs['abbr_inst_name'] = abbr
                request.cb_kwargs['xpath'] = custom_xpath
                yield request
                # print((abbr, name_url_pair[abbr]), "\n")
                # print("The custom xpath is: ", custom_xpath, "\n")



    def parse(self, response, abbr_inst_name, xpath):
        personnel = response.xpath(xpath).getall()
        personnel = list(map(lambda s: s.strip(), personnel))
        inst_name = abbr_inst_name
        # inst_name = response.url.split("/")[3] 
        return {inst_name: personnel}

# scrapy crawl affiliate
