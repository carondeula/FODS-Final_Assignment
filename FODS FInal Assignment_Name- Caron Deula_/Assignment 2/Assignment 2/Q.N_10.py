def get_daily_temps():

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temp_dict = {}

    for day in days_of_week:
        temp = float(input(f"Enter the average temperature for {day}: "))
        temp_dict[day] = temp  # Store the temperature with the day as the key

    return temp_dict

# Example usage:
daily_temps = get_daily_temps()
print("Weekly temperatures:", daily_temps)
