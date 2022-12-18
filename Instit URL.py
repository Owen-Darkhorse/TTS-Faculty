#Institutes using list of personnels
inst_list = ["CBB", "Game", "IQC", "Water", "CAMJ", \
    "CPATT", "IPR", "WAT.AI", "WCA", \
    "WCMR", "MICRO"]
list_url = [
        "https://uwaterloo.ca/bioengineering-biotechnology/about/people",\
        "https://uwaterloo.ca/games-institute/about/people",\
        "https://uwaterloo.ca/institute-for-quantum-computing/contacts?title=&group%5B66%5D=66",\
        "https://uwaterloo.ca/water-institute/about/people",\
        "https://uwaterloo.ca/centre-advanced-materials-joining/contacts?title=&group[72]=72",
        "https://uwaterloo.ca/centre-pavement-transportation-technology/contacts",\
        "https://uwaterloo.ca/institute-polymer-research/about/people",\
        "https://uwaterloo.ca/artificial-intelligence-institute/contacts?title=",\
        "https://uwaterloo.ca/astrophysics-centre/about/people/group/46",
        "https://uwaterloo.ca/waterloo-centre-microbial-research/about/people"]

#Institute using blocks of personnels
inst_block = "Climte"
block_url = "https://uwaterloo.ca/climate-institute/profiles?title=&field_uw_ct_profile_type_target_id%5B44%5D=44"

#Instiute using tables of personnels
inst_table = ["CPI", "CTN"]
table_url = ["https://uwaterloo.ca/cybersecurity-privacy-institute/about/people/researchers"
    "https://uwaterloo.ca/centre-for-theoretical-neuroscience/about/people/faculty"]

################## Other Formats #######################
WISE = "WISE"
WISE_url = "https://wise.uwaterloo.ca/team"

WIN = "WIN"
WIN_url = "https://uwaterloo.ca/institute-nanotechnology/our-people-0/our-members"

## CCMIC has pages for each department's affiliated faculty members
CCMIC = "CCMIC"
CCMIC_url = "https://uwaterloo.ca/computational-mathematics/people-profiles/category/55"

GHPI = "GHPI"
GHPI_url = "https://uwaterloo.ca/global-health-policy-innovation-research-centre/our-people"

WICI = "WICI"
WICI_url = "https://uwaterloo.ca/complexity-innovation/people/affiliate-researchers/affiliate-researchers-university-waterloo"


# Institutes with list form people objects
inst_wat_list = ["CBB", "Game", "Water", "IPR", "WCA", "MICRO"]
list_wat_url = [
        "https://uwaterloo.ca/bioengineering-biotechnology/about/people",\
        "https://uwaterloo.ca/games-institute/about/people",\
        "https://uwaterloo.ca/water-institute/about/people",\
        "https://uwaterloo.ca/institute-polymer-research/about/people",\
        "https://uwaterloo.ca/astrophysics-centre/about/people/group/46", \
        "https://uwaterloo.ca/waterloo-centre-microbial-research/about/people"
        ]

# CBB: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall() 
# Game: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# Water: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# IPR: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# WCA: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()
# MICRO: response.xpath('//div[@class="entry clearfix"]//h2/a/text()').getall()


# IQC: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# CAMJ: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# CPTT: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# WAT.AI: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()
# Climate: response.xpath('//div[@class="views-row"]//h2/a/text()').getall()  

# CTN: response.xpath('//tbody/tr/td[1]/a/text()').getall()
# CPI: response.xpath('//tbody/tr/td[1]/a/text()').getall()

# WICI: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
# WIN: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()

# WISE:  response.xpath('//div[@class="ig-item"]//h2/a/text()').getall()

# CCMIC: response.xpath('//h2[@class="anchor-name"]/a/text()').get()     

# GHPI: response.xpath('//div[@class="uw-copy-text"]//h2/a/text()').getall()
#** Need to trim extracted names


