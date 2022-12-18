##################### Group Institutes by xpath ###############################
# Institutes with list form people objects

# CBB: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall() 
# Game: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# Water: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# IPR: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# WCA: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# MICRO: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
inst_wat_list = ["CBB", "Game", "Water", "IPR", "WCA", "WCMR"]
list_wat_url = [
        "https://uwaterloo.ca/bioengineering-biotechnology/about/people",\
        "https://uwaterloo.ca/games-institute/about/people",\
        "https://uwaterloo.ca/water-institute/about/people",\
        "https://uwaterloo.ca/institute-polymer-research/about/people",\
        "https://uwaterloo.ca/astrophysics-centre/about/people/group/46", \
        "https://uwaterloo.ca/waterloo-centre-microbial-research/about/people"
        ]

# IQC: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# CAMJ: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# CPTT: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# WAT.AI: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# Climate: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()  
views_row_name = ['IQC', 'CAMJ', 'CPTT', 'WAT.AI', 'Climate']
views_row_url = [
        "https://uwaterloo.ca/institute-for-quantum-computing/contacts?title=&group%5B66%5D=66",\
        "https://uwaterloo.ca/centre-advanced-materials-joining/contacts?title=&group[72]=72",
        "https://uwaterloo.ca/centre-pavement-transportation-technology/contacts",\
        "https://uwaterloo.ca/artificial-intelligence-institute/contacts?title=",\
       "https://uwaterloo.ca/climate-institute/profiles?title=&field_uw_ct_profile_type_target_id%5B44%5D=44"
       ]
views_row_group = dict(zip(views_row_name, views_row_url))
views_row_group

# CTN: response.xpath('//tbody/tr/td[1]/a/text()').getall()
# CPI: response.xpath('//tbody/tr/td[1]/a/text()').getall()
tbody_name = ['CTN', 'CPI']
tbody_url = ["https://uwaterloo.ca/cybersecurity-privacy-institute/about/people/researchers", 
    "https://uwaterloo.ca/centre-for-theoretical-neuroscience/about/people/faculty"]
tbody_group = dict(zip(tbody_name, tbody_url))
tbody_group

# WICI: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
# WIN: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
field_item_name = ['WICI', 'WIN']
field_item_url = ["https://uwaterloo.ca/complexity-innovation/people/affiliate-researchers/affiliate-researchers-university-waterloo", 
    "https://uwaterloo.ca/institute-nanotechnology/our-people-0/our-members"
    ]
field_item_group = dict(zip(field_item_name, field_item_url))
field_item_group


# WISE:  response.xpath('//div[@class="ig-item"]//h2/a/text()').getall()
WISE = "WISE"
WISE_url = "https://wise.uwaterloo.ca/team"

wise_group = {WISE, WISE_url}

# CCMIC: response.xpath('//h2[@class="anchor-name"]/a/text()').get()     
CCMIC = "CCMIC"
CCMIC_url = "https://uwaterloo.ca/computational-mathematics/people-profiles/category/55"
ccmic_group = {CCMIC, CCMIC_url}

# GHPI: response.xpath('//div[@class="uw-copy-text"]//h2/a/text()').getall()
GHPI = "GHPI"
GHPI_url = "https://uwaterloo.ca/global-health-policy-innovation-research-centre/our-people"
ghip_group = {GHPI, GHPI_url}

#** Need to trim extracted names


