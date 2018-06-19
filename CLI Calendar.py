"""we'll build a basic calendar that the user will be able to
interact with from the command line.
The user should be able to choose to:
>View the calendar
>Add an event to the calendar
>Update an existing event
>Delete an existing event"""
from time import sleep, strftime

name = raw_input("Enter your first name: ")

calendar = {}

def welcome():
  print "Hi %s, Welcome to your calendar!"% (name)
  print "The calendar is now opening."
  sleep(1)

  strftime("%A %d, %Y")
  strftime("%H:%M:%S")
  sleep(1)

  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("""Use the following:
    'A' to 'Add'
    'U' to 'Update'
    'V' to 'View'
    'D' to 'Delete'
    'X' to 'Exit'
    """)
    user_choice = user_choice.upper()

    if user_choice == "V":
      if len(calendar.keys()) <1:
        print "The calendar is empty"
      else:
        print calendar

    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Calendar has been successfully updated"
      print calendar

    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date e.g (MM/DD/YYYY): ")
      if len(date) > 10 or  int(date[6:]) < int(strftime('%Y')):
        print "Invalid date entered"
        try_again = raw_input("Try Again? 'Y' for 'Yes', 'N' for 'No': ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The event was successfully added."

    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        event = raw_input("What event? ")
        for date in calendar:
          if event == calendar[date]:
            del calendar[date]
            print "Event was successfully deleted"
            print calendar
          else:
            print "Incorrect event"

    elif user_choice == "X":
      start = False

    else:
      print "Invalid input, program is closing!"
      start = False

start_calendar()
