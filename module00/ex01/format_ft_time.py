import time
try:
    epoch = time.time()
    current = time.localtime()

    print(f"Seconds since January 1, 1970: {epoch:,} or {epoch:e} in\
 scientific notation")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    print(f"{months[current.tm_mon - 1]} {current.tm_mday} {current.tm_year}")
except Exception as e:
    print(f"Error: {e}")
