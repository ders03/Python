import datetime


class Date:
    def __init__(self, date):
        self.year = date.strftime("%Y")
        self.month = date.strftime("%B")
        self.day = date.strftime("%A")

    def get_date(self):
        return(self.year + " " + self.month + " " + self.day)

def main():
    d = Date(datetime.datetime.now())
    print(d.get_date())

if __name__ == "__main__":
    main()
