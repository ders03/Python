import math
import sys

def make_restaurant(name, lon, lat):
    dic = {}
    dic[name] = lat, lon
    return(dic)

def get_name(restaurant):
    for key in restaurant:
        return(key)

def get_longitude(restaurant):
    for x in restaurant:
        values = restaurant[x]
        longitude = values[1]
        return(longitude)

def get_latitude(restaurant):
    for x in restaurant:
        values = restaurant[x]
        latitude = values[0]
        return(latitude)

def distance(a, b):
    lon_a = get_longitude(a)
    lat_a = get_latitude(a)
    lon_b = get_longitude(b)
    lat_b = get_latitude(b)
    return(math.sqrt((lon_a - lon_b)**2 + (lat_a - lat_b)**2))

def closer(lon, lat, a, b):
    diff_a = math.sqrt((lon - get_longitude(a))**2 + (lat - get_latitude(a))**2)
    diff_b = math.sqrt((lon - get_longitude(b))**2 + (lat - get_latitude(b))**2)
    if diff_a <= diff_b:
        return(a)
    else:
        return(b)

def greedy_path(lon, lat, restaurants):
    a = closer(lon, lat, restaurants[0], restaurants[1])
    b = closer(lon, lat, restaurants[0], restaurants[2])
    c = closer(lon, lat, restaurants[1], restaurants[2])
    p0 = closer(lon, lat, a, b)
    restaurants.remove(p0)
    p1 = closer(get_longitude(p0), get_latitude(p0), restaurants[0], restaurants[1])
    restaurants.remove(p1)
    return[p0, p1, restaurants[0]]


def main():

    closer(lon, lat, a, b)
    greedy_path(lon, lat, restaurants)


    if __name__ == "__main__":
        main()
