

class Restaurant:
    def __init__(self, name, long, lat):
        self.name = name
        self.longitude = long
        self.latitude = lat

    def get_name(self):
        return self.name

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

def main():
    r = Restaurant("Black Sheep", -122, 48.3)

    print(r.get_name())
    print(r.get_longitude())
    print(r.get_latitude())

if __name__ == "__main__":
    main()
