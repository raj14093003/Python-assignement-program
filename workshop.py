a=[2,4,5,6,7]
"""max=a[0]

for i in range(1,len(a)):
    if a[i] > max:
        max=a[i]

print(max)"""

if a[0]>a[1]:
    s_max=a[0]
    max=a[1]
else:
    s_max=a[1]
    max=a[0]

for i in range(3,len(a)):
    if a[i]>max:
        s_max=max
        max=a[i]
    elif a[i]>s_max:
        s_max=a[i]



