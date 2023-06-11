import time

def focus_timer(minutes):
    start_time = time.time()
    end_time = start_time + minutes * 60

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        print(f"剩余时间：{minutes:02d}:{seconds:02d}")
        time.sleep(1)

    print("专注时间结束！")
