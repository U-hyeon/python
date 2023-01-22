# 퀴즈) 주어진 코드를 활용하여 부동산 프로그램을작성하시오

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    #매물 정보 표시 
    def show_detail(self):
        pass

class House_sell(House):
    def __init__(self, location, house_type, price, completion_year):
        House.__init__(self, location, house_type, "매매", price, completion_year)
    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

class House_lent(House):
    def __init__(self, location, house_type, price, completion_year):
        House.__init__(self, location, house_type, "전세", price, completion_year)
    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

class House_lent_month(House):
    def __init__(self, location, house_type, deposit, price, completion_year):
        House.__init__(self, location, house_type, "월세", price, completion_year)
        self.deposit = deposit
    def show_detail(self):
        print("{0} {1} {2} {3}/{4} {5}"\
            .format(self.location, self.house_type, self.deal_type, self.deposit, self.price, self.completion_year))

h1 = House_sell("강남", "아파트", "10억", "2010년")
h2 = House_lent("마포", "오피스텔", "5억", "2007년")
h3 = House_lent_month("송파", "빌라", 500, 50, "2010년")

house_list = []
house_list.append(h1)
house_list.append(h2)
house_list.append(h3)

print("총 {0}대의 매물이 있습니다.".format(len(house_list)))
for house in house_list:
    house.show_detail()