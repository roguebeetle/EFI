import math

data = [4.98, 4.98, 4.95]
Rpok: float = sum(data) / len(data)
print("Среднее арифметическое: %.2f" % Rpok)
for i in range(len(data)):
    SRpok = math.sqrt(((data[i] - Rpok) ** 2) / (3 * (3 - 1)))
print("Стандартное отклонение: %.5f" % SRpok)
dRpok = 0.03 * Rpok + (3 * 0.01)
print("Стандартная неопределённость без калибровки: %.3f" % dRpok)
uDRpok = (0.005 / 1.65)
print("Стандартная неопределённость: %.5f" % uDRpok)
dRt = 0.015 * Rpok
udrt = dRt / math.sqrt(3)
print("Стандартная неопределённость температуры: %.3f" % udrt)
drw = (0.05 * Rpok)
udrw = (drw / (math.sqrt(3)))
print("Стандартная неопределённость влажности: %.3f" % udrw)
sumr = (math.sqrt(SRpok + uDRpok + udrt + udrw)) / 3
print("Суммарная стандартная неопределённость: %.3f" % sumr)

