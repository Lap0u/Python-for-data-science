import time
from datetime import datetime

current_time_seconds = time.time()
current_time_formatted = "{:,.4f}".format(current_time_seconds)

scientific_notation = "{:.2e}".format(current_time_seconds)

current_date_formatted = datetime.now().strftime("%b %d %Y")

script_output = f"""Seconds since January 1, 1970: {current_time_formatted} or {scientific_notation} in scientific notation
{current_date_formatted}"""

print(script_output)
