#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# listeyi düzleştiren (flatten) fonksiyon 
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


# elemanları tersine döndüren bir fonksiyon
def tersi(liste):
    ters_liste=[]
    for i in l:
        l=[]
        for j in i:
            l.append(j)
        l.reverse()
        ters_liste.append(lis)
    
    return ters_liste[::-1]

