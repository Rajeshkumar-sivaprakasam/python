print("Enter Five Subject marks:\t")
total=0;
a=[55,33,55,66,77]
for i in range(5):
   # a[i]=int(input())
    total=total+ a[i]
avg= total / len(a)
print(a[0],a[1],a[2],a[3],a[4],total,avg, sep="\n")
