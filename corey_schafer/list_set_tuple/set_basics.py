

#s1 = set([1, 2, 2, 6, 9, 12])
s1 = {1, 2, 2, 6, 9, 12}
s2 = {11, 55, 33, 99}
s1.add(10)
s1.update([12, 23], s2)

# removing the element
# using remove()

s1.remove(9)
# if we try to remove element which is does not exist, then through an error

#s1.remove(1000)
#(Traceback (most recent call last):
  #File "C:\Users\Lenovo\PycharmProjects\python_basics\corey_schafer\list_set_tuple\set_basics.py", line 15, in <module>
  #  s1.remove(1000)
#KeyError: 1000)

s1.discard(100)
print(type(s1))
print(s1)