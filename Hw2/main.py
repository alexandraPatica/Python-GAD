# 1
# Să se scrie o funcție care primește un număr nedefinit de
# parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.

def my_function(*args, **kwargs):
    my_sum = 0
    for i in range(len(args)):
        if type(args[i]) == int:
            my_sum += args[i]
    return my_sum


if __name__ == '__main__':
    a = ["teo", "ale", 7, 5, 1, "moni", "tudi", (1, 1), []]
    S = sum(filter(lambda x: type(x) == int, a))
    print(" ".join(filter(lambda x: type(x) == str, a)))
    print(S)

my_sum = my_function(2, 4, 'abc', param_1=2)
print(my_sum)
my_sum = my_function(1, 5, -3, 'abc', [12, 56, 'cad'])
print(my_sum)
my_sum = my_function()
print(my_sum)


# 2
# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#  suma tuturor numerelor de la [0, n]
#  suma numerelor pare de la [0, n]
#  suma numerelor impare de la [0. n]
def meine_zweite_Funktion(n):
    if n == 0:
        return 0, 0, 0
    else:
        rez = meine_zweite_Funktion(n - 1)
        return rez[0] + n, rez[1] + (n if n % 2 == 0 else 0), rez[2] + (n if n % 2 == 1 else 0)


my_tuple = meine_zweite_Funktion(5)
print(my_tuple)


# 3
# Să se scrie o funcție care citește de la tastatură și returnează
# valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.
def meine_dritte_funktion():
    n = input().strip()
    try:
        return int(n)
    except ValueError as e:
        return 0


print(meine_dritte_funktion())


