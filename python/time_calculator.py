def add_time(start_time, duration_time, day=None):
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday",
                        "Friday", "Saturday", "Sunday"]
    new_time = ""

    # Check if start_time has hr:min format
    if len(start_time.split(":")) != 2:
        return "Invalid start time format."

    start_list = start_time.split(":")
    start_minutes_list = start_list[1].split(" ")
    period = start_minutes_list[1].upper()

    # Check if hours and minutes only contain numbers
    if not start_list[0].isdigit() or not start_minutes_list[0].isdigit():
        return "Hours and minutes must contain only digits."

    start_hours = int(start_list[0])
    start_minutes = int(start_minutes_list[0])

    if period not in ["AM", "PM"]:
        return "Invalid day period."

    duration_list = duration_time.split(":")

    # Check if duration_time has hr:min format
    if len(duration_time.split(":")) != 2:
        return "Invalid duration time format."

    # Check if hours and minutes only contain numbers
    if not duration_list[0].isdigit() or not duration_list[1].isdigit():
        return "Hours and minutes must contain only digits."

    duration_hours = int(duration_list[0])
    duration_minutes = int(duration_list[1])

    if start_hours not in range(1, 13) or start_minutes not in range(0, 60):
        return "Invalid start time."

    if duration_hours < 0 or duration_minutes not in range(0, 60):
        return "Invalid duration time."

    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes

    # Shift minutes to hour if minutes is over 60
    if end_minutes >= 60:
        end_minutes -= 60
        end_hours += 1

    # Converting minutes to two digit format
    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)

    days_later = 0
    while end_hours >= 24:
        end_hours -= 24
        days_later += 1

    # Inverting time period if hours is over or equal to 12
    if end_hours >= 12:
        end_hours -= 12
        if period == "PM":
            period = "AM"
            days_later += 1
        else:
            period = "PM"

    # Converting to noon or midnight
    end_hours = 12 if end_hours == 0 else end_hours

    end_time = str(end_hours) + ":" + str(end_minutes) + " " + period

    new_time += end_time

    if day:
        formatted_day = day.capitalize().strip()
        if formatted_day not in days_of_the_week:
            return "Invalid day of the week."

        day_week = days_of_the_week.index(formatted_day)

        if days_later:
            day_week += days_later
            if day_week > 7:
                day_week %= 7

        formatted_day = days_of_the_week[day_week]
        new_time += (", " + formatted_day)

    if days_later > 1:
        new_time += (" (" + str(days_later) + " days later)")
    if days_later == 1:
        new_time += " (next day)"

    return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
