def format_digits(val):
    if val // 10 == 0:
        val = f'{val:02}'
        return val
    else:
        return val
        
def format_time(hours, minutes, seconds):
    time = f'{format_digits(hours)}:{format_digits(minutes)}:{format_digits(seconds)}'
    return time

class Timer:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        self.__time = format_time(hour, minute, second)
        
    def __str__(self):
        return self.__time

    def next_second(self):
        self.__second = (self.__second + 1) % 60
        if self.__second == 0:
            self.__minute = (self.__minute + 1) % 60
            if self.__minute == 0:
                self.__hour = (self.__hour + 1) % 24
        self.__time = format_time(self.__hour, self.__minute, self.__second)


    def prev_second(self):
        self.__second = (self.__second - 1) % 60
        if self.__second == 59:
            self.__minute = (self.__minute - 1) % 60
            if self.__minute == 59:
                self.__hour = (self.__hour - 1) % 24
        self.__time = format_time(self.__hour, self.__minute, self.__second)
        


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
