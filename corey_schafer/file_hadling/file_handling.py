
# one way
#f = open('test.txt', 'r') # write in file 'w' and to read a file 'r' and to append the file 'a'
#
# print(f.name)
# print(f.mode)
# f.close()

# second way is context manager

with open('test.txt', 'r') as f:
    f_content = f.read()
    print(f_content)
