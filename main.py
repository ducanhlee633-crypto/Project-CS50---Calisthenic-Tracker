from tabulate import tabulate
import sys
import csv
import re
class Log_workout:
    def __init__ (self, date, name, reps, sets, weight):
        self.name = nam
        self.reps = reps
        self.sets = sets
        self.date = date
        self.weight = weight 
    def __str__ (self):
        return f"saved successfully"
    def save_workout(self):
        headers = ["date","name","reps","sets", "weight"]
        with open ("database.csv", "a", newline ="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = headers)
            writer.writerow({"date":self.date,"name":self.name, "reps": self.reps, "sets":self.sets, "weight":self.weight})
def main():
    while True:
        try:
            print(dashboard())
            function_selected = select_function()
            if function_selected == 1:
                try: 
                    log_workout()
                except EOFError:
                    continue
            elif function_selected == 2:
                try:
                    print(history_view())
                    trigger1 = input("Click ctr d to back: ")
                except EOFError:
                    continue
            elif function_selected == 3:
                try:
                    print(view_analytics())
                    trigger2 = input("Click ctr d to back: ")
                except EOFError:
                    continue
            elif function_selected ==4:
                sys.exit("See U again")
        except KeyboardInterrupt:
            print("")
            sys.exit("Bye bye")
def dashboard():
    data = [
        ["1. Thêm lượt tập mới (Log Workout)"],
        ["2. Xem lịch sử tập luyện (View History)"],
        ["3. Xem thống kê tiến trình (View Analytics & 1RM)"],
        ["4. Thoát & Lưu dữ liệu (Save & Exit)"]
    ]
    return tabulate(data, headers=["Smart Athlete Performance Engine"], tablefmt="grid")
def select_function():
    function = int(input("Choose a function from 1-4: "))
    if function < 1 or function > 4:
        raise ValueError ("Error")
    else:
        return function
def log_workout():
    while True:
        try:    
            date_workout = input("Date: ").strip()
            matches = re.search(r"(\d{2})-(\d{2})-(\d{4})", date_workout)
            if matches:
                if int(matches.group(1))>31:
                    raise ValueError
                elif int(matches.group(2))>12:
                    raise ValueError
            else:
                raise ValueError
            name_exercise = input("Name exercise: ").lower()
            reps_exercise = int(input("Reps: "))
            sets_exercise = int(input("Sets: "))
            weight_exercise = int(input("Weight: "))
            log = Log_workout(date_workout, name_exercise, reps_exercise, sets_exercise, weight_exercise)
            log.save_workout()
            print(log)
        except EOFError:
            raise EOFError
def history_view():
    view = []
    try:
        with open ("database.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                view.append([row["date"],row["name"], row["reps"], row["sets"], f"{row['weight']} Kg"])
    except FileNotFoundError:
        return "No workout history found."
    return tabulate(view, headers=["Date", "Name", "Reps", "Sets", "Weight"], tablefmt="grid")
def view_analytics():
    exercise = input("Exercise: ").strip().lower()
    try:
        with open ("database.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            one_rm = 0
            for row in reader:
                if exercise == row["name"]:
                    one_rm = int(row["weight"])*(1+int(row["reps"])/30)
            if one_rm == 0:
                return "Not found"
            else:
                return f"{round(one_rm)} Kg"
    except FileNotFoundError:
        return "Not found"
if __name__ == "__main__"
    main
