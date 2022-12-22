import scrapy

# from scrapy.spiders import Rule, CrawlSpider
# from scrapInst.spiders.InstituteGroups import inst_groups
import scrapInst.spiders.InstituteGroups as InstituteGroups
# from scrapy.item import Institute


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
        
        start_urls = InstituteGroups.inst_groups

        for group in start_urls:
            group_info = start_urls[group]
            name_url_pair = group_info["name-url"]
            custom_xpath = group_info["xpath"]

            for abbr in name_url_pair:
                url_collection = name_url_pair[abbr]

                if isinstance(url_collection, str): #single url per institute case
                    request = scrapy.Request(url = url_collection, callback = self.parse)
                    request.cb_kwargs['abbr_inst_name'] = abbr
                    request.cb_kwargs['xpath'] = custom_xpath
                    yield request
                else: ## multiple urls for one institute
                    for url in url_collection:
                        request = scrapy.Request(url = url, callback = self.parse)
                        request.cb_kwargs['abbr_inst_name'] = abbr
                        request.cb_kwargs['xpath'] = custom_xpath
                        yield request

                    # yield {abbr : self.parse_recursively(url_collection, abbr, custom_xpath)}
                # print((abbr, name_url_pair[abbr]), "\n")
                # print("The custom xpath is: ", custom_xpath, "\n")
    
#     # Specifically for WATCAR
#     def parse_recursively(self, url_list, xpath):
#         # if list is empty
#         if not url_list:
#             return []
#         # if list is not empty
#         else: 
#             yield scrapy.Request(url = url_list.pop(0), callback=self.parse_single) + \
#                 self.parse_recursively(url_list, xpath)
 
# # Specifically for WATCAR
#     def parse_single(self, response, xpath):
#         personnel = response.xpath(xpath).getall()
#         personnel = list(map(lambda s: s.strip(), personnel))

#         return personnel


    def parse(self, response, abbr_inst_name, xpath):
        personnel = response.xpath(xpath).getall()
        personnel = list(map(lambda s: s.strip(), personnel))

        # Add leadership and advisory board
        if abbr_inst_name == "CCMIC": 
            personnel = personnel + InstituteGroups.CCMIC_cmt
        elif abbr_inst_name == "WICI":
            personnel = personnel + InstituteGroups.WICI_core
        elif abbr_inst_name == "WISA":
            personnel = personnel + InstituteGroups.WISA_cmt

        # inst_name = response.url.split("/")[3] 
        return {abbr_inst_name: personnel}

# scrapy crawl affiliate
