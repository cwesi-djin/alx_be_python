from datetime import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(number_of_days):
    today = datetime.date.today()

    future_date = today + datetime.timedelta(days= number_of_days)
    print(f"Future date:", future_date)

calculate_future_date(number_of_days)