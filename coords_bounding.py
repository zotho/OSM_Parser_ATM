#!/usr/bin/env python
from math import sin, cos, sqrt, atan2, radians

R = 6373.0 # радиус земли в километрах

def distance(x,y):
    """
    Параметры
    ----------
    x : tuple, широта и долгота первой геокоординаты 
    y : tuple, широта и долгота второй геокоординаты 
    
    Результат
    ----------
    result : дистанция в километрах между двумя геокоординатами
    """
    lat_a, long_a, lat_b, long_b = map(radians, [*x,*y])    
    dlon = long_b - long_a  # long_b = long_a + dlon
    dlat = lat_b - lat_a    # lat_b = lat_a + dlat
    a = sin(dlat/2)**2 + cos(lat_a) * cos(lat_a + dlat) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


if __name__ == '__main__':
    mos = '55°45′21″ с. ш. 37°37′04″ в. д.'
    ekb = '56°50′ с. ш. 60°35′ в. д.'

    mos_coords = 55. + 45./60 + 21./3600,   37. + 37./60 + 4./3600
    ekb_coords = 56. + 50./60,              60. + 35./60

    print(f'Расстояние между\n Москвой({mos}) и Екатеринбургом({ekb})\n равно {distance(mos_coords, ekb_coords)} километров')