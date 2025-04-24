class House:
    def __init__(self,location, house_Type, deal_Type, price, completion_year):
        self.location = location
        self.house_Type = house_Type
        self.deal_Type = deal_Type
        self.price = price
        self.completion_year = completion_year

    def show_Detail(self):
        print(f"{self.location} {self.house_Type} {self.deal_Type} {self.price}")

house = []

house1 = House("강남","아파트","매매","21억 4000만원","2017년")
house2 = House("마포","오피스텔","전세","5억 1000만원","2021년")
house.append(house1)
house.append(house2)

for info in house:
    info.show_Detail()