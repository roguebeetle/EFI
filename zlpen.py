import math

data = [0.224, 0.224, 0.224]
Ua = 0.003  # Значение расширенной неопределённости из свидетельства о калибровке измерителя ИС-20
Ka = 1.65   # Коэфициент охвата при P=95%, указанный в свидетельстве о калибровке измерителя ИС-20
Rpok: float = sum(data) / len(data)
print("Среднее арифметическое: ", Rpok)
for i in range(len(data)):
    SRpok = math.sqrt(((data[i] - Rpok) ** 2) / (3 * (3 - 1)))
print("Стандартное отклонение: ", SRpok)
DRpok = (0.03 * Rpok + 0.001)
uDRpok = DRpok / math.sqrt(3)
print("Стандартная неопределённость без калибровки: %.5f" % uDRpok)
UdRpok = Ua / Ka
print("Стандартная неопределённость: %.5f" % UdRpok)
dRt = (0.03*Rpok)
UdRt = dRt/math.sqrt(3)
print("Стандартная неопределённость температуры: %.5f" % UdRt)
dRw = (0.03*Rpok)
UdRw = (dRw/math.sqrt(3))
print("Стандартная неопределённость влажности: %.5f" % UdRw)
for i in range(len(data)):
    UcR = math.sqrt((UdRpok**2)+(UdRt**2)+(UdRw**2))
print("Суммарная стандартная неопределённость: %.4f" % UcR)
U = 2*UcR
print("Расширенная неопределённость: %.3f" % U)

