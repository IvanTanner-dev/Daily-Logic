def find_org(acronym):
    agency_dict = {
    "NASA": "National Avocado Storage Authority",
    "CIA": "Cats Infiltration Agency",
    "FBI": "Fluffy Beanbag Inspectors",
    "DOJ": "Department Of Jelly",
    "WHO": "Wild Honey Organization",
    "EPA": "Eating Pancakes Administration",

    }

    for i in agency_dict:
        if acronym == i:
            return agency_dict[i]