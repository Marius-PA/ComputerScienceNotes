from guizero import App, Text, TextBox, PushButton
 
# Function to calculate total sleep hours and check if it's less than 56
def calculate_total_sleep():
    try:
        sleep_hours = [float(day1.value), float(day2.value), float(day3.value), float(day4.value), float(day5.value), float(day6.value), float(day7.value)]
        total_sleep = sum(sleep_hours)
        if total_sleep < 56:
            result.value = f"Total sleep hours: {total_sleep}. Not enough sleep!"
        else:
            result.value = f"Total sleep hours: {total_sleep}. You are getting enough sleep."
    except ValueError:
        result.value = "Please enter valid numbers for all days."
 
#my widgets
app = App(title="Weekly Sleep Calculator")
 
Text(app, text="Enter the number of hours you slept each day:")
 
Text(app, text="Day 1:")
day1 = TextBox(app)
 
Text(app, text="Day 2:")
day2 = TextBox(app)
 
Text(app, text="Day 3:")
day3 = TextBox(app)
 
Text(app, text="Day 4:")
day4 = TextBox(app)
 
Text(app, text="Day 5:")
day5 = TextBox(app)
 
Text(app, text="Day 6:")
day6 = TextBox(app)
 
Text(app, text="Day 7:")
day7 = TextBox(app)
 
PushButton(app, text="Calculate Total Sleep", command=calculate_total_sleep)
 
result = Text(app, text="")
 
app.display()