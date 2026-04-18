class Mahsulot:
    def __init__(self, nomi, narxi, chegirma):
        self.nomi = nomi
        self.narxi = narxi
        self.chegirma = chegirma

    def yangi_narx(self):
        yangi_narx = self.narxi * (1 - self.chegirma / 100)
        return f"Yangi narx: {int(yangi_narx)} so‘m (Chegirma: {self.chegirma}%)"


mahsulotlar = [
    Mahsulot("TV", 2000000, 10),
    Mahsulot("Telefon", 1500000, 15),
    Mahsulot("Komp", 3000000, 20),
]

for mahsulot in mahsulotlar:
    print(mahsulot.nomi + ": " + mahsulot.yangi_narx())
