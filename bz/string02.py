import io
'''
1.Python中，字符串属于不可变对象，不支持原地修改，如果需要修改其中的值，只能创建新的字符
串对象。
2。确实需要原地修改字符串，可以使用io.StringIO对象或array模块
'''
s="hello lst"
sio=io.StringIO(s)
print(sio)