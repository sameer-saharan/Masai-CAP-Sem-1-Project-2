import tkinter as tk
from tkcalendar import Calendar
from datetime import date

def SelectDate(event):
    selectedDate = cal.get_date()    # Get selected date
    dateButton.config(text=selectedDate)    # Update dateButton text

root = tk.Tk()  # Main window
root.title("Calendar")

cal = Calendar(root, selectmode='day', date_pattern='mm-dd-yyyy')  # Calendar widget
cal.pack(pady=25)

dateButton = tk.Button(root, text="Select Date", command=lambda: cal.selection_set(date.today()))   # Button to select date
dateButton.pack(pady=15)

cal.bind("<<CalendarSelected>>", SelectDate)
root.mainloop()
