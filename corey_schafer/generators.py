def square_numbers(nums):

    result = []

    for num in nums:

        yield num * num


my_nums = square_numbers([2, 5 ,6, 8 ,10])

print(next(my_nums))

for num in my_nums:

    print(num)

my_detail = [{'name':"pratik", 'age': 28},{'name': 'Nikita', 'age': 28},{'name': 'Sidhu', 'age': 21}]

my_name = [first_name['name'] for first_name in my_detail]

import operator
from  operator import  itemgetter
my_names = list(map(itemgetter('name'), my_detail))
print(my_names)
