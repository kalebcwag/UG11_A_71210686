def ambil_tengah(x,n=None):
    if n==None:
        jum=len(x)
        bagi=(round(jum/2))
        return(x[bagi])
    else:
        jum=len(x)
        bagi=(round(jum/2))
        return (x[bagi+n-1])
    
print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))
