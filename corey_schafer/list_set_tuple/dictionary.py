# dictionary comprehension
name =['Bruce', 'Clark', 'Peter', 'logan', 'Wade']
heros =['Batman', 'Superman', 'Spiderman', 'Wolverfine', 'Pratik']
my_dict ={}

# for name, hero in zip(name, heros):
#     my_dict[name]=hero
# #print(my_dict)

my_dict2 ={name: hero for name, hero in zip(name, heros) if name !='Peter'}
print(my_dict2)


