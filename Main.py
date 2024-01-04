import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

# Define Appointment class
class Appointment:
    def __init__(self, patient_name, date, time, doctor):
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.doctor = doctor

# Create a list to store appointments
appointments = []

# Main window
root = tk.Tk()
root.title("Swathi Dental Clinic - Appointment Management")

# Menu frame
menu_frame = ttk.Frame(root)
menu_frame.pack(pady=10)

# Add buttons for various functions
add_button = ttk.Button(menu_frame, text="Add Appointment", command=show_add_window)
add_button.pack(side="left", padx=10)

view_button = ttk.Button(menu_frame, text="View Appointments", command=show_view_window)
view_button.pack(side="left", padx=10)

# Additional buttons for edit, cancel, and search (implement functionality as needed)

# Add appointment window
def show_add_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Appointment")

    # Add labels and entry fields for patient details
    patient_name_label = ttk.Label(add_window, text="Patient Name:")
    patient_name_entry = ttk.Entry(add_window)

    date_label = ttk.Label(add_window, text="Date:")
    date_entry = ttk.Entry(add_window)

    time_label = ttk.Label(add_window, text="Time:")
    time_entry = ttk.Entry(add_window)

    doctor_label = ttk.Label(add_window, text="Doctor:")
    doctor_combo = ttk.Combobox(add_window)  # Add list of doctors

    # Add a submit button
    submit_button = ttk.Button(add_window, text="Submit", command=submit_appointment)

    # Pack widgets
    patient_name_label.pack()
    patient_name_entry.pack()

    date_label.pack()
    date_entry.pack()

    time_label.pack()
    time_entry.pack()

    doctor_label.pack()
    doctor_combo.pack()

    submit_button.pack()

# View appointments window
def show_view_window():
    view_window = tk.Toplevel(root)
    view_window.title("View Appointments")

    # Add listbox to display appointments
    appointments_list = ttk.Listbox(view_window)
    appointments_list.pack()

    # Fill the listbox with existing appointments
    for appointment in appointments:
        info = f"{appointment.patient_name} - {appointment.date.strftime('%Y-%m-%d')} - {appointment.time.strftime('%H:%M')} - {appointment.doctor}"
        appointments_list.insert(tk.END, info)

# Function to process appointment submission
def submit_appointment():
    pass