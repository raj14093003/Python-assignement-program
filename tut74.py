#lambda within map
mylist=(1,3,4,8,9)
p=list(map(lambda a:(a/3!=2),mylist))
print(p)