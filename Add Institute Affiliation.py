import pandas as pd
from datetime import datetime as dt
import scrapInst.scrapInst.spiders.InstituteGroups as InstGroup

Faculty = pd.read_excel("221216-RegularFaculty.xlsx", index_col=False)
inst_members = pd.read_json("scrapInst/scrapInst/spiders/affiliation.json", typ = "series")


## Filter out lecturers, they are not researchers
FacultyRemoved = Faculty[Faculty['Job Profile'] != "Lecturer"]


# Combine WATCAR dictionary together, and take their union set
WATCAR_list = list(filter(lambda x: list(x.keys())==['WATCAR'], inst_members))
WATCAR_union = set()
for division in WATCAR_list:
    WATCAR_union = WATCAR_union.union(set(division["WATCAR"]))

WATCAR_union = list(WATCAR_union)
inst_members = list(filter(lambda x: list(x.keys())!=['WATCAR'], inst_members)) + \
    [{"WATCAR": WATCAR_union}]



############# Preparing the csv file #############################
# Index by inst names
inst_list = list(list(group) for group in inst_members)
inst_list = list(item[0] for item in inst_list)


## Boolean Values for institute affilations
for inst in inst_members:
    inst_name = list(inst.keys())[0]
    researcher_name = inst[inst_name]
    FacultyRemoved[inst_name] = FacultyRemoved.Worker.isin(researcher_name)
    # print(inst_name)

FacultyRemoved.CBB

# Map a list of boolean into a list of affiliations for each researcher
def mapAffiliation(researcher, inst_list):
    affList = []

    for inst in inst_list:
        if researcher[inst] == True:
            affList.append(inst)
    return affList

mapAffiliation(FacultyRemoved.iloc[0], inst_list)

FacultyRemoved['AffList'] = FacultyRemoved.apply(mapAffiliation, inst_list = inst_list, axis=1)
FacultyAffiliation = FacultyRemoved.drop(inst_list, axis=1)

# Output into csv
now = dt.now()
formattednow = now.strftime("%y%m%d")
# All affilations are in one columns, shown as a list of strings
FacultyAffiliation.to_csv(formattednow + "-" + "FacultyAffiliationComplete.csv") 

# Affilations in separate columns, shown as boolean to indicate whether a given professor is in the institution or not
FacultyRemoved.to_csv(formattednow + "-" + "SeparateFacultyAffiliation.csv")