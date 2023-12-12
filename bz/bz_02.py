import time
# a=2000
# b=2000
# c=3000
# print("a is b", a is b)
# print("a=b?",a==b)
# a='to be or not to be'
# print(a.split())
# b=['a1','a2','a3']
# print(','.join(b))
# time01=time.time()
# a=""
# for i in range(10000000):
#     a+="sxt"
# time02=time.time()
# print("total:",str(time02-time01))
'''
time03=time.time()
li=[]
for i in range(10000000):
    li.append("stx")
a="".join(li)
time04=time.time()
print("total2:",str(time04-time03))
'''
a="teng"
a.center(10)
print(a,len(a.center(10)))
print(a.center(10,"*"))
print(a.rjust(15))
print(a.ljust(15,"*"))

