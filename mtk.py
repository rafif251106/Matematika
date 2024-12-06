def menu():
    print('Menu \n1.Perhitungan suhu \n2.Perhitungan bangun datar \n3.Perhitungan bangun ruang \n4.Exit')


def reamur_c(c):
    r=4/5*c
    return r
def fahrenhit_c(c):
    f=9/5*c+32
    return f
def kelvin_c(c):
    k=c+273
    return k
def celcius_r(r):
    c=5/4*r
    return c
def fahrenhit_r(r):
    f=9/4*r+32
    return f
def kelvin_r(r):
    k=5/4*r+273
    return k
def celcius_f(f):
    c=5/9*(f-32)
    return c
def reamur_f(f):
    r=4/9*(f-32)
    return r
def kelvin_f(f):
    k=5/9*(f-32)+273
    return k
def celcius_k(k):
    c=k-273
    return c
def reamur_k(k):
    r=4/5*(k-273)
    return r
def fahrenhit_k(k):
    f=9/5*(k-273)+32
    return f

def celcius():
    angka=eval(input('Masukkan suhu celcius: '))
    pil=int(input('Mau diubah ke suhu apa: \n1.Reamur \n2.Fahrenhit \n3.Kelvin \nMasukkan pilihanmu: '))
    if pil==1:
            print(f'Suhu {angka} celcius jika diubah ke reamur menjadi {reamur_c(angka)} reamur ')
    elif pil==2:
            print(f'Suhu {angka} celcius jika diubah ke fahrenhit menjadi {fahrenhit_c(angka)} fahrenhit ')
    elif pil==3:
            print(f'Suhu {angka} celcius jika diubah ke kelvim menjadi {kelvin_c(angka)} kelvin ')
def reamur():
    angka=eval(input('Masukkan suhu Reamur: '))
    pil=int(input('Mau diubah ke suhu apa: \n1.Celcius \n2.Fahrenhit \n3.Kelvin \nMasukkan pilihanmu: '))
    if pil==1:
            print(f'Suhu {angka} reamur jika diubah ke celcius menjadi {celcius_r(angka)} celcius ')
    elif pil==2:
            print(f'Suhu {angka} reamur jika diubah ke fahrenhit menjadi {fahrenhit_r(angka)} fahrenhit ')
    elif pil==3:
            print(f'Suhu {angka} reamur jika diubah ke kelvim menjadi {kelvin_r(angka)} kelvin ')
def fahrenhit():
    angka=eval(input('Masukkan suhu Fahrenhit: '))
    pil=int(input('Mau diubah ke suhu apa: \n1.Celcius \n2.Reamur \n3.Kelvin \nMasukkan pilihanmu: '))
    if pil==1:
            print(f'Suhu {angka} fahrenhit jika diubah ke celcius menjadi {celcius_f(angka)} celcius ')
    elif pil==2:
            print(f'Suhu {angka} fahrenhit jika diubah ke reamur menjadi {reamur_f(angka)} reamur ')
    elif pil==3:
            print(f'Suhu {angka} fahrenhit jika diubah ke kelvim menjadi {kelvin_f(angka)} kelvin ')
def kelvin():
    angka=eval(input('Masukkan suhu Kelvin: '))
    pil=int(input('Mau diubah ke suhu apa: \n1.Celcius \n2.Reamur \n3.Fahrenhit \nMasukkan pilihanmu: '))
    if pil==1:
            print(f'Suhu {angka} kelvin jika diubah ke celcius menjadi {celcius_k(angka)} celcius ')
    elif pil==2:
            print(f'Suhu {angka} kelvin jika diubah ke reamur menjadi {reamur_k(angka)} reamur ')
    elif pil==3:
            print(f'Suhu {angka} kelvin jika diubah ke fahrenhit menjadi {fahrenhit_k(angka)} fahrenhit ')
    
def suhu():
 kondisi=True
 while kondisi:
    print('Ingin merubah suhu apa: \n1.Celcius \n2.Reamur \n3.Fahrenhit \n4.Kelvin')
    user=int(input('Masukkan pilihan suhu yang ingin dirubah: '))
    if user==1:
        celcius()
    elif user==2:
        reamur()
    elif user==3:
        fahrenhit()
    elif user==4:
        kelvin()
    else:
         print('Tidak ada dalam daftar')
    user=input('Apakah anda ingin melanjutkan (iya/tidak):')
    if user=='iya':
       suhu()
    elif user=='tidak':
       main()


def main():
  menu()
  user=int(input('Masukkan pilihan menu: '))
  if user==1:
       suhu()    
main()        


