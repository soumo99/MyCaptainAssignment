word = "Mississippi"
dic = {}

for n in word:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

sorted_dic = dict(sorted(dic.items(),key=lambda kv:kv[1],reverse=True))

print(sorted_dic)
