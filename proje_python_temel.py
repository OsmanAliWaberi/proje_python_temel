#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def flatten(liste):
    t=("[","]", ",","'")
    string =""
    for i in liste :
        string += str(i)
    new_string = ""
    for i in s:
        if i in t :
            continue
        else:
            string+= i
    new_liste = string.split(" ") 
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

