# Exercise to compare a number to a numbers in an ordered list and return TRUE if number exist in list or return FALSE 

def look_in(x, liste):
    liste = sorted(liste)
    for y in liste:
        if y == x:
            return True
    return False


def look_binary(x, liste):
    liste = sorted(liste)
    liste = liste.copy()
    while len(liste) > 1:
        grenze = int(len(liste)/2)
        if x == liste[grenze] or x == liste[grenze - 1]:
            return True
        elif x < liste[grenze]:
            liste = liste[0:grenze]
        else:
            liste = liste[grenze + 1:]
    return False


__name__ = "__main__"

number_list = [0, 4, 4, 8, 2, 44, 30, 42, 69, 42, 8]
number = 7

print(look_in(number, number_list))

print(look_binary(number, number_list))