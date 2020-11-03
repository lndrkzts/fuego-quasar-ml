import math

from .constants import EPSILON


def get_message(messages):
    array = [None] * len(messages[0])
    
    for message in messages:
        for index, word in enumerate(message):
            if array[index] == None and word != '':
                array[index] = word

    if None in array:
        return None

    return ' '.join(e for e in array)


def get_location(satellites):
    """
    dx: Distancia horizontal entre los centros del círculo
    dy: Distancia vertical entre los centros del círculo
    d: Distancia en linea recta entre los dos centros del círculo
    dd: Distancia directa entre el s0 y s1
    guide_point: Punto donde la línea que atraviesa los puntos de intersección del círculo cruza la línea entre los centros del círculo
    """
    s0 = satellites.get('kenobi')
    s1 = satellites.get('skywalker')
    s2 = satellites.get('sato')
    
    result = { 'x': 0, 'y': 0 }

    dx = s1['x'] - s0['x']
    dy = s1['y'] - s0['y']

    d0 = math.sqrt((dy ** 2) + (dx ** 2))

    # Checkea si los circulos no se intersectan
    if d0 > (s0['r'] + s1['r']):
        return None

    # Checkea si un circulo esta dentro del otro
    if d0 < abs(s0['r'] - s1['r']):
        return None

    # Distancia directa entre s0 y s1
    dd = ((s0['r'] ** 2) - (s1['r'] ** 2) + (d0 ** 2)) / (2.0 * d0)

    guide_point_x = s0['x'] + (dx * dd / d0)
    guide_point_y = s0['y'] + (dy * dd / d0)

    # Distancia desde el punto guia y los puntos de interseccion
    h = math.sqrt((s0['r'] ** 2) - (dd ** 2))

    rx = -dy * (h / d0)
    ry = dx * (h / d0)

    # Puntos de interseccion
    intersection_point_1_x = guide_point_x + rx
    intersection_point_1_y = guide_point_y + ry

    intersection_point_2_x = guide_point_x - rx
    intersection_point_2_y = guide_point_y - ry

    # Checkea si el circulo de p2 se cruza con alguno de los puntos de intersección
    dx = intersection_point_1_x - s2['x']
    dy = intersection_point_1_y - s2['y']
    d1 = math.sqrt((dy ** 2) + (dx ** 2))

    dx = intersection_point_2_x - s2['x']
    dy = intersection_point_2_y - s2['y']
    d2 = math.sqrt((dy ** 2) + (dx ** 2))

    if abs(d1 - s2['r']) < EPSILON:
        result['x'], result['y'] = round(intersection_point_1_x, 1), round(intersection_point_1_y, 1)
        return result

    elif abs(d2 - s2['r']) < EPSILON:
        result['x'], result['y'] = round(intersection_point_2_x, 1), round(intersection_point_2_y, 1)
        return result
    
    return None
