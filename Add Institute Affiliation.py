import pandas as pd
from datetime import datetime as dt

Faculty = pd.read_excel("221216-RegularFaculty.xlsx", index_col=False)
inst_members = pd.read_json("scrapInst/scrapInst/spiders/affiliation.json", typ = "series")

## Filter out lecturers, they are not researchers
FacultyRemoved = Faculty[Faculty['Job Profile'] != "Lecturer"]
Faculty.shape
FacultyRemoved.shape
FacultyRemoved.columns

## List of institute names
inst_list = list(list(group) for group in inst_members)
inst_list = list(item[0] for item in inst_list)
inst_list

## Boolean Values for institute affilations
for inst in inst_members:
    inst_name = list(inst.keys())[0]
    researcher_name = inst[inst_name]
    FacultyRemoved[inst_name] = FacultyRemoved.Worker.isin(researcher_name)

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
FacultyAffiliation.to_csv(formattednow + "-" + "FacultyAffiliationComplete.csv")