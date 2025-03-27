import time
from datetime import datetime

print(f"Seconds since January 1, 1970: {time.time():,.4f} or {time.time():.2e} in scientific notation")

current_date = datetime.now()
formatted_date = current_date.strftime("%b %d %Y")
print(formatted_date)