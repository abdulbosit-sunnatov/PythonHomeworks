#2 

class Date:

    month_names = [
        "", "January", "February","March","April","May","June","July","August","September","November","December"
    ]

    def __init__(self, month, day, year):
        if not (1 <= month <= 12):
            print('Wrong month!')
        if not (1 <= day <= 12):
            print('Wrong month!')
        self.month = month
        self.day = day
        self.year = year
    
    def print_format1(self):
        print(f'{self.month}/{self.day}/{self.year}')
    
    def print_format2(self):
        print(f'{self.month_names[self.month]} {self.day},{self.year}')

    def print_format3(self):
        print(f'{self.day} {self.month_names[self.month]} {self.year}')

    
def main():
        month = 4
        year = 2025
        day = 4

        date = Date(month,day,year)

        date.print_format1
        date.print_format2
        date.print_format3

if __name__ == '__main__':
    main()