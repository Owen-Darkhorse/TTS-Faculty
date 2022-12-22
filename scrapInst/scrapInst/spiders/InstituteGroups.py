
inst_wat_list = ["CBB", "WATER", "IPR", "WCA", "WCMR"]
inst_wat_url = [
        "https://uwaterloo.ca/bioengineering-biotechnology/about/people/group/85",\
        "https://uwaterloo.ca/water-institute/about/people",\
        "https://uwaterloo.ca/institute-polymer-research/about/people",\
        "https://uwaterloo.ca/astrophysics-centre/about/people/group/46", \
        "https://uwaterloo.ca/waterloo-centre-microbial-research/about/people/group/51"
        ]

wat_list_dict = dict(zip(inst_wat_list, inst_wat_url))
wat_list_dict

views_row_name = ['IQC', 'CAMJ', 'CPTT', 'WAT.AI', 'CLIMATE', 'WATCAR']
views_row_url = [
        "https://uwaterloo.ca/institute-for-quantum-computing/contacts?title=&group%5B66%5D=66",\
        "https://uwaterloo.ca/centre-advanced-materials-joining/contacts?title=&group[72]=72",
        "https://uwaterloo.ca/centre-pavement-transportation-technology/contacts",\
        "https://uwaterloo.ca/artificial-intelligence-institute/contacts?title=",\
        "https://uwaterloo.ca/climate-institute/profiles?title=&field_uw_ct_profile_type_target_id%5B44%5D=44",

        # WATCAR has separate lists of researchers
        ["https://uwaterloo.ca/centre-automotive-research/contacts?title=&group%5B58%5D=58",\
            "https://uwaterloo.ca/centre-automotive-research/contacts?title=&group%5B59%5D=59",\
                "https://uwaterloo.ca/centre-automotive-research/contacts?title=&group%5B75%5D=75",\
                    "https://uwaterloo.ca/centre-automotive-research/contacts?title=&group%5B82%5D=82",\
                        "https://uwaterloo.ca/centre-automotive-research/contacts?title=&group%5B88%5D=88"]
       ]
views_row_dict = dict(zip(views_row_name, views_row_url))
views_row_dict

tbody_name = ['CPI', 'CTN']
tbody_url = ["https://uwaterloo.ca/cybersecurity-privacy-institute/about/people/researchers", 
    "https://uwaterloo.ca/centre-for-theoretical-neuroscience/about/people/faculty"]
tbody_dict = dict(zip(tbody_name, tbody_url))
tbody_dict

# WICI: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
# WIN: response.xpath('//div[@class="field-items"]//div[@class="custom-listing-page clearfix"]/h2/a/text()').getall()
field_item_name = ['WICI', 'WIN', 'GAME']
field_item_url = ["https://uwaterloo.ca/complexity-innovation/people/affiliate-researchers/affiliate-researchers-university-waterloo", 
    "https://uwaterloo.ca/institute-nanotechnology/our-people-0/our-members",\
    "https://uwaterloo.ca/games-institute/faculty"
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


####################   Additional personnel names ###########################
SRC_board = ['Leia Minaker', 'Christian Boudreau', 'Mark Giesbrecht', 'Changbao Wu',\
    "Daniel O'Connor", "Bernard Dunker", 'Colleen Maxwell', 'Susan Elliot', 'Sarah Wilkins-Laflamme',\
        'Dilruba Sharmin', 'Gradon Nicholls']

CCMIC_cmt = ['Hans De Sterck', 'Ryan Browne', 'Arne Storjohann', 'Ricardo Fukasawa',\
    'Michael Rubinstein']

WISA_cmt = ['Sunjoo Advani', 'Wnedy Bailey', 'Derrick Cheung', 'Logan Jones', 'Drew Hamblin', 'Rod Regier',\
    'Martin Smith', 'Peter Studer', 'Joelle Thorgrimson', 'Simon Witts', 'Ibrahim Yimer']

# fetch('https://uwaterloo.ca/complexity-innovation/people/core-members/core-members-university-waterloo')
# response.xpath('//h2[@class="anchor-name"]/a/text()').getall()
WICI_core = ['Vanessa Schweizer', 'Sharon Kirkpatrick', 'Christopher Bauch', 'Trevor Charles', 'Mark Crowley', \
    'Peter Deadman', 'Igor Grossmann', 'Keith Hipel', 'Chrystopher Nehaniv', 'Dawn Parker', 'Stephen Quilley']