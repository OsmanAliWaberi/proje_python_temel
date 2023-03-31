#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def flatten(liste):
    t=("[","]", ",","'")
    string1 =""
    string2 = ""
    new_string = ""
    for i in liste :
        string1 += str(i)
    
    for i in string1:
        if i in t :
            continue
        else:
            string2+= i
    new_liste = string2.split(" ")
    return new_liste

    
def tersi(liste):
    liste=[]
    for i in l:
        lis=[]
        for j in i:
            lis.append(j)
    lis.reverse()
    liste.append(lis)
    return liste.reverse()

