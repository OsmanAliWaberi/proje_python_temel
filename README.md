# listeyi düzleştiren (flatten) fonksiyon 
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

"input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]"

"output: [1,'a','cat',2,3,'dog',4,5]"
```python

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

```

# elemanları tersine döndüren bir fonksiyon

2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

```python

def tersi(liste):
    ters_liste=[]
    for i in l:
        l=[]
        for j in i:
            l.append(j)
        l.reverse()
        ters_liste.append(lis)
    
    return ters_liste[::-1]

``` 

