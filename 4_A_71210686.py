def ambildanbalik(a,b,c,d):
    if d==True:
        ambil=a[b-1:c]
        hasil=ambil[::-1]
        return hasil
    else:
        ambil=a[b-1:c]
        return ambil

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,True))
