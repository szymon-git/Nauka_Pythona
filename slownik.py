#samolot = {'name':'boeing', 'przebieg':10000, 'type':'pasazerski'}
#for key in samolot:
#    print("{0}:{1}".format(key, samolot[key]))
#for key,value in samolot.iteritems():
#    print("{0}:{1}".format(key, value))
#def print_dict(d):
#    for key in samolot:
#        print("{0}:{1}".format(key, d[key]))
#if __name__ == "__main__":
#    samolot = {'name':'boeing','przebieg':10000, 'type':'pasazerski'}
#print_dict(samolot)
def calculate_vat(netto):
    vat=float(netto*23)/100
    return vat
if __name__=="__main__":
    vat=calculate_vat(10000)
    print("{0}".format(vat))
