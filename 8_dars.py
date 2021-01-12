# Ikkita qayiq turg'un suvda bir-biriga tomon a km/soat va b km/soat tezlik bilan suzmoqda
# Ular orasidagi masofa s km bo'lsa ular qancha vaqtda uchrashadi

# a va b foydalanuvchi tomonidan kiritiladi

v1 = int(input('Birinchi qayiq tezligi = '))
v2 = int(input('Ikkinchi qayiq tezligi = '))
s = int(input('Oralaridagi masofa = '))
v = v1 + v2
t = s / v
s = v * t
t = s / v
 
print('t =' , t , 'soat')  