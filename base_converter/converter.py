#!/usr/bin/python


BASE_2 = "Base 2"
BASE_8 = "Base 8"
BASE_10 = "Base 10"
BASE_16 = "Base 16"
UNIDENTIFIED_BASE = "Unidentified base"

def base_finder(nb):
    print nb[1]
    if len(nb) <= 2:
        return UNIDENTIFIED_BASE
    else:
        return {
        'b': BASE_2,
        'o': BASE_8,
        'd': BASE_10,
        'x': BASE_16,
        }.get(nb[1], UNIDENTIFIED_BASE)

def convert_10_to_n(nb_to_convert, base):
    index=0
    converted_number = [None] * 64
    result = []#* 100# len(str(nb_to_convert))

    while nb_to_convert!=0:
        converted_number[index] = (nb_to_convert) % base
        nb_to_convert = nb_to_convert / base
        index+=1
        #print index

    index-=1
    temp=index
    for x in reversed(xrange(index)):
        result = [converted_number[index]] + result
        index-=1
    result = [converted_number[index]] + result

    end_result = result[::-1]
    end_result= ''.join(str(x) for x in end_result)
    return end_result

def convert_n_to_10(nb_to_convert, base):
    if base=10:
        return nb_to_convert

    index=0
    size=len(str(nb_to_convert))
    result=0
    for x in xrange(size):
        


x=convert_10_to_n(3,2)
print(x)
