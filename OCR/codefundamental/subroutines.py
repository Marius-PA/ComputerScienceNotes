from guizero import App, Box, PushButton, Text

app = App(title="Sleep calculator")

def calcsleep():
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    total = 0
    for i in range(0, 7):
        question = int(input("How many hours of sleep you get on " + days[i] + "? : "))
        total += question

    if (total / 7) >= 8:
        print("You sleep for 8 or more hours per night on average, nice work ! continue that way")
    else:
        print("You sleep less then 8 hours a night, you need more sleep")

button = PushButton(app, text="Start", command=calcsleep)

app.display()