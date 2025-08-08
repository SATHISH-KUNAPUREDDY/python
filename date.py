from datetime import datetime, date, time, timedelta, timezone

# 1. Current date and time
now = datetime.now()
print("Current datetime:", now)

# 2. Today's date
today = date.today()
print("Today's date:", today)

# 3. Create specific date and time
custom_date = date(2025, 12, 25)
custom_time = time(14, 30, 0)
custom_datetime = datetime(2025, 12, 25, 14, 30)
print("Custom date:", custom_date)
print("Custom time:", custom_time)
print("Custom datetime:", custom_datetime)

# 4. Formatting dates
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("Formatted datetime:", formatted)

# 5. Parsing date string
date_str = "2025-07-29"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime:", parsed)

# 6. Timedelta examples
week_later = now + timedelta(days=7)
month_ago = now - timedelta(days=30)
print("One week later:", week_later)
print("30 days ago:", month_ago)

# 7. Extracting components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

# 8. Combine date and time
combined = datetime.combine(custom_date, custom_time)
print("Combined datetime:", combined)

# 9. Get UTC time
utc_now = datetime.now(timezone.utc)
print("Current UTC time:", utc_now)
