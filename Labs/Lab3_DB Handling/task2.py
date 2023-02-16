
class Time:
    def __init__(self,hour,min,sec):
        self.__hours = hour
        self.__minutes = min
        self.__seconds = sec

    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self,hr):
        self.__hours = hr

    @property
    def minutes(self):
        return self.__minutes

    @hours.setter
    def minutes(self, min):
        self.__minutes = min

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def hours(self, sec):
        self.__seconds = sec

    def add_time(self,t):
        hr = (self.__hours + t.__hours)%24
        min = (self.__minutes + t.__minutes)%60
        sec = (self.__seconds + t.__seconds)%60
        print(str(hr) + ':' + str(min) + ':' + str(sec))

    def display_minute(self):
        mint = self.__hours*60 + self.__minutes + self.__seconds*(1/60)
        print("\nNo. of minutes are: " + str(mint))

    def update_time(self):
        min = float(input("Enter minutes to convert it into time: "))
        hr = min // 60
        mint = min % 60
        sec = min % 1
        print (str(hr)+ ' : ' + str(mint) + ' : ' + str(sec))

    def display_time24(self):
        print(str(self.__hours%24) + ' : ' + str(self.__minutes%60) + ' : ' + str(self.__seconds%60))

    def display_time12(self):
        print(str(self.__hours%12) + ' : ' + str(self.__minutes%60) + ' : ' + str(self.__seconds%60))


tt = Time(10,29,38)
t2 = Time(40,60,70)
#tt.display_minute()
#tt.add_time(t2)
#t = Time(15,45,45)
#t.display_time12()
t2.update_time()