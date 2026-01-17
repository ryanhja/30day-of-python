# Day 6: 30 Days of python programming
tpl = tuple()
brothers = ("Joe", "Smith", "John", "Will")
print(brothers)
sisters = ("Lily", "Jane", "Alice", "Maggie")
print(sisters)

siblings = brothers + sisters
print(siblings)
print(len(siblings))

father_mother = ("Will", "Emma")
family_members = siblings + father_mother
print(family_members)

siblings = family_members[:-2]
print(siblings)

parents = family_members[-2:]
print(parents)