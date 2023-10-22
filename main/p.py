from __future__ import print_function
import os.path
import pandas as pd
import datetime
import requests
from tkinter import Tk, Button, filedialog,Label,messagebox


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


# ADD YOUR CALENDAR ID HERE
YOUR_CALENDAR_ID = 'primary'
YOUR_TIMEZONE = 'America/Toronto' # find yours here: https://www.timezoneconverter.com/cgi-bin/zonehelp?cc=CA&ccdesc=Canada
file_path = None
root = Tk()
def browse_file():
    global file_path  # Use the global variable
    filename = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if filename:
        file_path = filename
def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # determine which function to run        
    addEvent(creds)

# Function to assign colorId based on the time difference
def assign_color_id(duration):
    # Define the color IDs for red, amber, and blue
    red_color_id = "11"
    amber_color_id = "5"
    blue_color_id = "9"

    if duration < datetime.timedelta(days=2):
        return red_color_id
    elif duration < datetime.timedelta(days=4):
        return amber_color_id
    else:
        return blue_color_id

def show_success_message():
    messagebox.showinfo("Success", "Event created successfully!")

def addEvent(creds):
    df = pd.read_excel(file_path, dtype=str)
    for index, row in df.iterrows():
        current_datetime = datetime.datetime.now()
        summary = row['summary']
        location = row['location']
        description = row['description']
        start_date = row['start']
        end_date = row['end']
        status = row['status']

         # Convert the date strings to datetime objects
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')
        if summary == "Assignment" and status == '1':
            color_id = 10
        else:
            duration = end_date - current_datetime
            color_id = assign_color_id(duration)


        event = []
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_date,
                'timeZone': YOUR_TIMEZONE,
                },
            'end': {
                'dateTime': end_date.isoformat(),
                'timeZone': YOUR_TIMEZONE,
                },
            'colorId': color_id,
            }
        service = build('calendar', 'v3', credentials=creds)
        event = service.events().insert(calendarId=YOUR_CALENDAR_ID, body=event).execute()
    show_success_message()
    
    
    print('Event created')
    exit()


def roots():
    def on_browse_hover(event):
        browse_button.config(bg="#3b5998", fg="white")

    def on_browse_leave(event):
        browse_button.config(bg="#ffffff", fg="black")

    def on_browse_click(event):
        browse_button.config(bg="#1d3f72", fg="white")

    def on_add_event_hover(event):
        add_event_button.config(bg="#3b5998", fg="white")

    def on_add_event_leave(event):
        add_event_button.config(bg="#ffffff", fg="black")

    def on_add_event_click(event):
        add_event_button.config(bg="#1d3f72", fg="white")
    root.title("Event Sync")
    root.geometry("720x560")
    browse_button = Button(root, text="Browse File", command=browse_file, bg="#ffffff", fg="black", relief="ridge",width=25, height=10)
    browse_button.pack(side="left", padx=100, pady=10)

    add_event_button = Button(root, text="Upload", command=main, bg="#ffffff", fg="black", relief="ridge", width=25, height=10)
    add_event_button.pack(side="left", pady=10)

    browse_button.bind("<Enter>", on_browse_hover)
    browse_button.bind("<Leave>", on_browse_leave)
    browse_button.bind("<Button-1>", on_browse_click)

    # Bind events for the "Upload" button
    add_event_button.bind("<Enter>", on_add_event_hover)
    add_event_button.bind("<Leave>", on_add_event_leave)
    add_event_button.bind("<Button-1>", on_add_event_click)

    root.mainloop()

if __name__ == '__main__':
    roots()

