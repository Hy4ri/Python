import datetime
import time


def set_alarm(alarm_time):
    print(f"Alarm set to {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%I:%M %p")

        if current_time == alarm_time:
            print("Wake up!!")
            is_running = False
        elif current_time < alarm_time:
            time.sleep(1)
            print(current_time)


if __name__ == "__main__":
    alarm_time = input("Enter Time: ")
    set_alarm(alarm_time)
