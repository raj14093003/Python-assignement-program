from collections import namedtuple

a = namedtuple('courses', 'name, technology')
s = a. make(['artificial intelligance', 'python'])
print(s)