nums = [2, 6, 8, 12, 10, 20, 16, 4, 9]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list2 = [n for n in nums]
print(my_list2)

#my_listt = [n * n for n in nums]
#print("n*n", my_listt)

my_list_lambda = list(map(lambda n: n * n, nums))
print(my_list_lambda)

even_list=[]
for n in nums:
    if n %2==0:
        even_list.append(n)
print(even_list)

even_list2 = [n for n in nums if n % 2==0]
print(even_list2)

even_list3 = list(filter(lambda n: n%2==0, nums))
print(even_list3)

digit_num_list=[]

for letter in "abcd":
    for num in range(4):
        digit_num_list.append((letter,num))
#print(digit_num_list)

digit_num_list2= [(letter,num) for letter in "abcd" for num in range(4)]
print(digit_num_list2)

