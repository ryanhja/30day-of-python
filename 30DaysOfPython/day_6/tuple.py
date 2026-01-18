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

fruits = ('banana', 'orange', 'mango', 'lemon', "apple")
vegetables = ('tomato', 'onion', 'carrot', 'potato', 'garlic')
animals = ('dog', 'cat', 'lion', 'rabbit', 'elephant')

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_food_tp = food_stuff_tp[int(len(food_stuff_tp)/2)]
print(middle_food_tp)

middle_food_lt = food_stuff_tp[int(len(food_stuff_lt)/2)]
print(middle_food_lt)

del middle_food_tp