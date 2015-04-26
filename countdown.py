from datetime import datetime
from time import sleep


def countdown():
    """Take a date/time, and print a countdown of time remaining."""
    while True:
        target_date = input("Please enter a date (YYYY-MM-DD): ")
        target_time = input("Please enter a time (HH:MM:SS): ")
        target = target_date + ' ' + target_time
        now = datetime.now()

        target = datetime.strptime(target, '%Y-%m-%d %H:%M:%S')
        if target > now:
            break
        print("Please enter a date/time in the future")
    while target > now:
        diff = target - now
        remaining_minutes = diff.seconds / 60
        print("{:.2f} minutes remaining".format(remaining_minutes))
        sleep(5)
        if target != datetime.now():
            now = datetime.now()
        else:
            break
    print("Target reached")

if __name__ == '__main__':
    countdown()
