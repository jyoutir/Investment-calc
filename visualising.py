import matplotlib.pyplot as plt
import csv
from tkinter import messagebox

# Function to read data from CSV, plot the growth, and return final value
def plot_and_display_final_value(filename="investment_data.csv"):
    try:
        last_entry = {}
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last_entry = row

        if not last_entry:
            raise ValueError("No data found in the CSV file.")

        initial_investment = float(last_entry["Initial Investment ($)"])
        monthly_contribution = float(last_entry["Monthly Contribution ($)"])
        annual_rate = float(last_entry["Annual Return Rate (%)"])
        years = int(last_entry["Investment Years"])

        months = years * 12
        monthly_rate = (1 + annual_rate / 100) ** (1/12) - 1
        values = [initial_investment]

        for month in range(1, months + 1):
            previous_value = values[-1] * (1 + monthly_rate)
            new_value = previous_value + monthly_contribution
            values.append(new_value)

        plt.figure(figsize=(10, 5))
        plt.plot(range(months + 1), values, marker='o')
        plt.title("Investment Growth Over Time")
        plt.xlabel("Months")
        plt.ylabel("Investment Value ($)")
        plt.grid(True)
        plt.show()

 # Retrieve and output the final value
        final_value = values[-1]
        messagebox.showinfo(
            "Projected Final Value",
            f"Projected Value after {years} years: ${final_value:.2f}"
        )

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error: {e}")
