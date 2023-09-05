
courses = ["Physics", "Maths", "Science", "Art", "chemistry"]
courses2 = ["Geography", "Geometry"]
print(courses2)
# append add the elemen at the end of the list
courses.append("Marathi")
# if we add the list into list in another list with append() it wont add as element
#output : #['Physics', 'Maths', 'Science', 'Art', 'chemistry', ['Geography', 'Geometry']]
#courses.append(courses2)
print(courses)

# add list into list as elements
# output : ['Physics', 'Maths', 'Science', 'Art', 'chemistry', 'Marathi', 'Geography', 'Geometry']
courses.extend(courses2)
print(courses)

streams = ["Physics", "Maths", "Science", "Art", "chemistry"]
#streams.remove("Maths")

#ele = streams.pop()
#print(ele)

for i in streams:
    item=streams.pop()
    streams.append(item)
print("modified reverse:", streams)



nums =[25, 62, 2, 10, 8, 10, 4]

#nums.sort()
print(nums)

sorted_list = sorted(nums)
print(sorted_list)

streams1 = ["Physics", "Maths", "Science", "Art", "chemistry"]
streams1[1]="Pratik"
course_str = ','.join(streams1)
print(course_str)
for index, course in enumerate(streams1, start=1):
    print(index, course)

# Tuple details
tuple_data = ("Pratik","sagar","Nikita","Kranti")
#tuple_data[0] = "Sangeeta"



# set

subjects = {"Marathi","English", "Science","Geography","Geometry"}
art_subject = {"Art", "commerce","Marathi"}

common_subject = subjects.intersection(art_subject)
print("common subjects :", common_subject)

union_set = subjects.union(art_subject)

print("union of two set :", union_set)


# creating empty list, set, tuple

#1) creating empty list
nums =[]
empty_nums = list()

#2)creating empty tuple
tup = ()
empty_tup = tuple()


#3)creating empty set

empty_set = {} # this is not the correct way it creates empty dictioary

e_set = set()



