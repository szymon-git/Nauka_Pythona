import pprint


def main():
    koszyk = [
                    {"nazwa": "ziemniaki","cena": 5, "VAT": 23, "unit": "kg"},
                    {"nazwa": "jajka","cena": 1, "VAT": 23, "unit": "szt"},
                    {"nazwa": "marchew","cena": 4, "VAT": 23, "unit": "kg"},
                    {"nazwa": "pietruszka","cena": 20, "VAT": 23, "unit": "kg"},
                    {"nazwa": "seler","cena": 9, "VAT": 23, "unit": "kg"}]

    f = open("koszyk.csv", "w")
    for poz in koszyk:
        for pole in ['nazwa', 'cena', 'VAT', 'unit']:
            f.write("{0},".format(poz[pole]))
        f.write('\n')
    f.close()

    koszyk2 = []
    print("#### koszyk2")

    f2 = open("koszyk.csv", "r")
    calosc = f2.read()
    linie = calosc.split('\n')
    for l in linie:
        produkt = {}
        if len(l) > 0:
            pola = l.split(',')
            produkt['nazwa'] = pola[0]
            produkt['cena'] = int(pola[1])
            koszyk2.append(produkt)

    pprint.pprint(koszyk2)

if __name__ == "__main__":
    main()
