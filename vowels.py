'''List'''
'''vowels=['a', 'e', 'i', 'o', 'u']
word=input("Provide a word to search for voweis:")
found=[]
for letter in word:       #取单词中的各个字母
    if letter in vowels:  #如果它在vowels列表中
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)'''
     #打印出来
# found=[]
# found.append('a')
# found.append('e')
# found.append('i')
# found.append('o')
# if 'u' not in found:
#     found.append('u')
# print(len(found))
nums=[0,1,5,3]
# nums.append(4)
# nums.remove(3)        #3是要删除的值，不是索引值
# nums.pop(3)           #3是索引值对应列表中的第4位，删除
# nums.extend([5,6])    #提供对象列表，追加到现有列表
#nums.insert(2,"python") #前面1是插入对象索引在这个位置之前，python是要插入的对象
#print(nums)



