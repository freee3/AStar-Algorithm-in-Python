from math import sqrt


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printLocation(self):
        print(self.x, self.y)


# area is my map, these numbers are the distance from the target. -1 is block, 0 is goal block
Area = [
    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4],
    [15, 14, 13, -1, 11, 10, -1, -1, 7, 6, -1, -1, 1, 2, 3],
    [16, -1, 14, -1, 12, 11, -1, -1, 8, 7, -1, 1, 0, 1, 2],
    [15, 14, 13, -1, 11, 10, 9, 8, 7, 6, -1, 2, 1, 2, 3],
    [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4]
]


# Intuitively calculates bird flight distance
def h(x, y):
    return sqrt(((12 - x) ** 2 + (2 - y) ** 2))


# g(n) ' e göre yönleri kontrol ediyoruz
def Yonler(x, y):
    if (x < 5 and y < 15) and (x >= 0 and y >= 0):
        yon = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        if (y > 0):
            if (Area[x][y - 1] > -1):
                yon[0][0] = 1  # Sola
                yon[4][0] = yon[4][0] + 1
                degisken = Area[x][y - 1]
                degisken2 = h(x, y - 1)
                yon[0][1] = degisken + degisken2
            else:
                yon[0][0] = -1
        else:
            yon[0][0] = -1

        if (x > 0):
            if (Area[x - 1][y] > -1):
                yon[1][0] = 1  # Yukarıya
                yon[4][0] = yon[4][0] + 1
                degisken = Area[x - 1][y]
                degisken2 = h(x - 1, y)
                yon[1][1] = degisken + degisken2
            else:
                yon[1][0] = -1
        else:
            yon[1][0] = -1

        if (y < 14):
            if (Area[x][y + 1] > -1):
                yon[2][0] = 1  # Sağa
                yon[4][0] = yon[4][0] + 1
                degisken = Area[x][y + 1]
                degisken2 = h(x, y + 1)
                yon[2][1] = degisken + degisken2
            else:
                yon[2][0] = -1
        else:
            yon[2][0] = -1

        if (x < 4):
            if (Area[x + 1][y] > -1):
                yon[3][0] = 1  # Aşşagıya
                yon[4][0] = yon[4][0] + 1
                degisken = Area[x + 1][y]
                degisken2 = h(x + 1, y)
                yon[3][1] = degisken + degisken2
            else:
                yon[3][0] = -1
        else:
            yon[3][0] = -1

        return yon
    else:
        return print("Girilen indis 15x5 lik matrisin dışındadır!(Harita Dışı)")

