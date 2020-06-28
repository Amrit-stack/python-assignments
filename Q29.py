def Merge(dict1, dict2,dict3): 
    res = {**dict1, **dict2, **dict3} 
    return res 
      
 
dict1 = {1:10, 2:20} 
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60} 
dict4 = Merge(dict1, dict2,dict3) 
print(dict4) 