import time


def greet(current_time: str):
    print(f"Halo Reky, Selamat {current_time}")


def get_current_time():
    current_time = int(time.strftime("%H"))
    if current_time < 12:
        return "Pagi"
    elif current_time < 15:
        return "Siang"
    elif current_time < 18:
        return "Sore"
    else:
        return "Malam"


greet(get_current_time())
