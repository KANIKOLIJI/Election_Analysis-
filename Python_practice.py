counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver' :
    print(counties[1])
counties = ["Arapahoe", "Denver", "Jefferson"]

if "El paso" in counties :
    print("El paso is in the list of countries.")
else :
    print("El paso is not in the list of countries.")

counties_dict = {"Arapahoe" : 16, "Denver" : 161111, "Jefferson": 171111}
for county, vouter in counties_dict.items() :
    print(county + "county has" +" "+ str(vouter) + " " + "registered voters.")



