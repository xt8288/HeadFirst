'''自己编写'''
# phrase="Don't panic!"
# plist=list(phrase)
# print(phrase)
# print(plist)
# letters=plist[1:8:1]
# letters.remove("'")
# letters.insert(3,letters.pop())
# letters.pop(4)
# letters.insert(2," ")
# my_letters=''.join(letters)
# print(my_letters)

'''书上编写 '''
phrase="Don't panic!"
plist=list(phrase)
print(phrase)
print(plist)
new_phrase=''.join(plist[1:3])
print(new_phrase)
new_phrase=new_phrase+''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_phrase)
