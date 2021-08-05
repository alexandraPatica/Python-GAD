import math


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return '%d/%d' % (self.numarator, self.numitor)

    def __add__(self, fractie):
        rezultat = Fractie(0, 1)
        if self.numitor == fractie.numitor:
            rezultat.numitor = self.numitor
            rezultat.numarator = self.numarator + fractie.numarator

        else:
            lcm = math.lcm(self.numitor, fractie.numitor)
            rezultat.numitor = lcm
            rezultat.numarator = int(self.numarator * (lcm / self.numitor) + fractie.numarator * (lcm / fractie.numitor))

        divizor = math.gcd(rezultat.numarator, rezultat.numitor)
        rezultat.numarator /= divizor
        rezultat.numitor /= divizor

        return rezultat

    def __sub__(self, fractie):
        rezultat = Fractie(0, 1)
        if self.numitor == fractie.numitor:
            rezultat.numitor = self.numitor
            rezultat.numarator = self.numarator - fractie.numarator

        else:
            lcm = math.lcm(self.numitor, fractie.numitor)
            rezultat.numitor = lcm
            rezultat.numarator = int(self.numarator * (lcm / self.numitor) - fractie.numarator * (lcm / fractie.numitor))

        divizor = math.gcd(rezultat.numarator, rezultat.numitor)
        rezultat.numarator /= divizor
        rezultat.numitor /= divizor

        return rezultat

    def inverse(self):
        fractie = Fractie(0, 1)
        fractie.numarator = self.numitor
        fractie.numitor = self.numarator

        return fractie


fractie1 = Fractie(10, 2)
print(fractie1)

fractie2 = Fractie(4, 5)
print(fractie2)

print(fractie1.__add__(fractie2))
print(fractie1.__sub__(fractie2))
print(fractie1.inverse())
