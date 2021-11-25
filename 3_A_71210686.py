kata=input("Masukkan Kalimat: ")
start=int(input("Start Index: "))
stop=int(input("Stop Index: "))

def hitung_hapus():
    jum=len(kata)
    hapus=len(kata[start:stop+1])
    tot=hapus/jum*100
    return tot

print(hitung_hapus())
