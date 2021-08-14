import json
import urllib.request
import urllib.parse

def get_input():
    want = []
    ingredient1 = input("Enter first ingredient: ")
    ingredient2 = input("Enter second ingredient: ")
    want.append(ingredient1)
    want.append(ingredient2)
    return(",".join(want))

def query():
    dish = input("Enter type of dish: ")
    url = "http://www.recipepuppy.com/api/?i=" + get_input() + "&q=" + dish
    response = urllib.request.urlopen(url)
    raw = response.read()
    data = json.loads(raw)
    want = []
    for obj in data["results"]:
        want.append("Title: " + obj["title"].replace("\n", "") + "\n" + "Link: " +  obj["href"] + "\n")
    return(("\n").join(want))

print(query())
