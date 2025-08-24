  
import pandas as pd

''' def remove(a):
    List = []
    for i in a:
        if i not in List:
            List.append(i)
    return List
a = [1,2,3,4,5,6,1,2,4]
print(remove(a))
#We can't use set because it doesn't maintain order of elements.
#Same for '''
dic1 = {
    'Name': ['Tom', 'nick', 'krish', 'jack'],
    'Age': [20, 21, 19, 18],
    'city': ['Tom', 'nick', 'krish', 'jack'],
}
df = pd.DataFrame(dic1)
print(df)
