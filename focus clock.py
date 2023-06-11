import time

def focus_timer(minutes):

    """

    专注时钟计时器

    :param minutes: 计时时间（以分钟为单位）

    """

    seconds = minutes * 60

    start_time = time.time()

    while True:

        current_time = time.time()

        elapsed_time = current_time - start_time

        remaining_time = seconds - elapsed_time

        if remaining_time <= 0:

            print("时间到!")

            break

        minutes, seconds = divmod(remaining_time, 60)

        time_str = "{:02d}:{:02d}".format(int(minutes), int(seconds))

        print("剩余时间: " + time_str, end="\r")

        time.sleep(1)

# 20分钟的专注时钟

focus_timer(20)
