##Test Change
number = [1, 2, 3]
new_numbers = [n + 1 for n in number]
name = "Angela"
new_list = [letter for letter in name]
range_change = [n + 1 for n in range(1,5)]
range_change2 = [n * 2 for n in range(1,5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names_test = [name.upper() for name in names]
long_names = [name.upper() for name in names if len(name) > 4]