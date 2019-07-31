# phrase="Don't panic!"
# plist=list(phrase)
# print(phrase)
# for i in range(4):
#     plist.pop()            #没有告诉删除哪一个，就删除最后一项，for循环四次
# plist.remove("D")          #与plist.pop(0)是一样的
# plist.pop(2)               #plist.remove("'")
# a=[plist.pop(),plist.pop()]#没有指定删除哪一个，就删除最后一项，最后一项是a，删除后将其存放在列表第一位
# print(a)
# plist.extend(a)
# plist.insert(2,plist.pop(3))
# #plist.extend([plist.pop(),plist.pop()])
# print(plist)
# new_phrase=''.join(plist)
# print(plist)
# print(new_phrase)

# mylist=["a","b","c"]          #列表是字符串类型
# a=''.join(mylist)
# print(a)
# first=[1,2,3,4,5]
# second=first
# second.append(6)
# print(first)
# print(second)
'''如果按上述的办法，这个对象也追加到first中了，因为first和second指向
同一数据，如果修改一个列表，另一个也会改变,接下来使用copy用法'''

# first=[1,2,3,4,5]
# second=first
# third=second.copy()
# third.append(6)
# print(first)
# print(third)
# print(first[-1])  #负索引从右往左数

'''list[开始：结束：步长]中间用冒号连接'''
letters="Don't panic!"
Lletters=list(letters)
print(Lletters[0:10:3])
print(Lletters[3:])
print(Lletters[:10])
print(Lletters[::2])