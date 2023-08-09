class WeekDayError(Exception):
    pass
	

class Weeker:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day.capitalize() in self.days:
            self.day = day.capitalize()
        else:
            raise WeekDayError
        self.day_index = self.days.index(day)

    def __str__(self):
        return self.day

    def add_days(self, n):
        self.day_index = (self.day_index + n) % 7 
        self.day = self.days[self.day_index]

    def subtract_days(self, n):
        self.day_index = (self.day_index - n) % 7
        self.day = self.days[self.day_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
