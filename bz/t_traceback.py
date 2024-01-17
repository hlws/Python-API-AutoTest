import traceback
try:
    print("step1")
    num=1/0
except:
    with open("D:\\Python-API-AutoTest\\bz\\a.log","a") as f:
        traceback.print_exc(file=f)