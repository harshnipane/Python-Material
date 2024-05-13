l =[{'rec1':{'col1':1,'col2':10,'col3':5}},{'rec2':{'col1':2,'col2':60,'col3':67}},{'rec3':{'col1':6,'col2':30,'col3':2}},{'rec4':{'col1':3,'col2':20,'col3':99}}]
l1 = []
for i in l:
    for j in i.keys():
        l1.append(i[j])
print(list(l1))
dict2 = {}
for i in l1:
    for k,e in i.items():
        if(k not in dict2.keys()):
            dict2[k] = e
        else:
            dict2[k] += e
print(dict2)  

for k in dict2.keys():
    print("mean",k,":",dict2[k]/len(l1))



    
