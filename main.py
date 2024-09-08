import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from visualising import plot_and_display_final_value



# o store user data in memory
user_data = {}

# return user data
def visualize_data_via_button():
    global user_data  # makes sure user data is collected  first

    if not user_data:
        messagebox.showerror("Error", "No data available to visualize.")
        return

    
def collect_and_save_csv():
    try:
        # retreive values 
        initial_investment = float(entry_initial.get())
        monthly_contribution = float(entry_monthly.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        # make sure they are poisitive
        if initial_investment < 0 or monthly_contribution < 0 or annual_rate < 0 or years < 0:
            raise ValueError("All values must be positive.")

        #stoees data
        global user_data
        user_data = {
            "Initial Investment": initial_investment,
            "Monthly Contribution": monthly_contribution,
            "Annual Return Rate": annual_rate,
            "Investment Years": years
        }

        #makes the csv file
        filename = "investment_data.csv"

        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='') as csvfile:
            fieldnames = ["Initial Investment ($)", "Monthly Contribution ($)", "Annual Return Rate (%)", "Investment Years"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            #writes data into the csv
            writer.writerow({
                "Initial Investment ($)": initial_investment,
                "Monthly Contribution ($)": monthly_contribution,
                "Annual Return Rate (%)": annual_rate,
                "Investment Years": years
            })

#outputs confirmation with the values you put in
        messagebox.showinfo(
            "Data Collected and Saved",
            f"Data has been saved as follows:\n"
            f"Initial Investment: ${initial_investment}\n"
            f"Monthly Contribution: ${monthly_contribution}\n"
            f"Annual Return Rate: {annual_rate}%\n"
            f"Investment Years: {years}"
        )


    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}. Please try again.")


# set up a window
root = tk.Tk()
root.title("Investment Data Input")

#  labels the entry boxes 
labels = [
    "Initial Investment ($):",
    "Monthly Contribution ($):",
    "Annual Return Rate (%):",
    "Investment Duration (Years):"
]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, sticky='w', padx=5, pady=5)
    
    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Assign individual entry widgets to variables
entry_initial, entry_monthly, entry_rate, entry_years = entries

# submit button that saves to `collect_and_save_csv`
ttk.Button(root, text="Submit Data", command=collect_and_save_csv).grid(row=4, column=0, columnspan=2, pady=10)

# Create a Tkinter button to activate visualization and output
ttk.Button(root, text="Visualize Data", command=plot_and_display_final_value).grid(row=6, column=0, columnspan=2, pady=10)


# Set up the main application window
root = tk.Tk()
root.title("Investment Data Input")

# Start the Tkinter main loop
root.mainloop()
