import pandas as pd
import datetime as dt

Faculty = pd.read.csv("221216-RegularFaculty.xlsx")

FacultyRemoved = Faculty.drop(Faculty.Position == "Lecturer", axis = 0)

pd.to_csv(FacultyRemoved, "221216-RegularFaculty.csv")