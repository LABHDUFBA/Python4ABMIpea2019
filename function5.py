import math


def area_circle(r):
    area = math.pi * r ** 2
    return area


if __name__ == '__main__':
    raio = 2
    result = area_circle(raio)
    print('A área é: {:.2f}'.format(result))
