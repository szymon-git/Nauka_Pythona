samochody = ['syrena', 'polonez', 'fiat','kia']
ilosc=[3,5,4]

print(samochody[0])
print(samochody[1])

#for s in samochody:
#    print(s)
for idx in range(len(samochody)):
    print("idx: "+str(idx)+ " : "+samochody [idx])
    print(samochody[idx]+" ma ilosc drzwi "+str(ilosc[idx]))
