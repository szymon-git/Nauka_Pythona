import pprint

def main():
    koszyk = [
        {'nazwa':'mlekowita','cena':5,'vat':23,'jednostka':'litr','ilosc':10},
        {'nazwa':'cukier','cena':6,'vat':23,'jednostka':'kg', 'ilosc':5},
        {'nazwa':'woda','cena':2,'vat':8,'jednostka':'kg','ilosc':15}
    ]
    #pprint.pprint(koszyk)
    #print((koszyk[0]['nazwa']) + " , " + str(koszyk[0]['ilosc']))


    for i in range (len(koszyk)):
        print((koszyk[i]['nazwa']) + " , " + str(koszyk[i]['ilosc']))

    file = open('koszyk.csv', 'w')
    for poz in koszyk:
        linia ="{0};{1}\n".format(poz['nazwa'], poz ['cena'])
        file.write(linia)
    file.close()

#    for key in koszyk:
#        pprint.pprint("{0}:{1}".format(key, koszyk(key))


if __name__=="__main__":
    main()
