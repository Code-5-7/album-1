import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversion App")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Cache for exchange rates
        self.exchange_rates = {}
        self.last_fetched = None

        # Title
        tk.Label(root, text="Conversion App", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Result Label (created early to avoid AttributeError)
        self.result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
        self.result_label.pack(pady=10)

        # Conversion Type Dropdown
        tk.Label(root, text="Select Conversion Type:", bg="#f0f0f0").pack()
        self.conversion_type = ttk.Combobox(root, values=["Currency", "Temperature", "Distance"], state="readonly")
        self.conversion_type.current(0)
        self.conversion_type.pack(pady=5)
        self.conversion_type.bind("<<ComboboxSelected>>", self.update_options)

        # Conversion Options Dropdown
        self.options_label = tk.Label(root, text="Select Conversion:", bg="#f0f0f0")
        self.options_label.pack()
        self.conversion_options = ttk.Combobox(root, state="readonly")
        self.conversion_options.pack(pady=5)

        # Amount Input
        tk.Label(root, text="Enter Amount:", bg="#f0f0f0").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        # Convert Button
        tk.Button(root, text="Convert", command=self.convert, bg="#3b82f6", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

        # Fetch exchange rates after initializing result_label
        self.fetch_exchange_rates()

        # Initialize options
        self.update_options()

    def fetch_exchange_rates(self):

        try:
            response = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
            response.raise_for_status()
            data = response.json()
            self.exchange_rates = data["usd"]
            self.last_fetched = datetime.now()
            # Update result_label only if it exists
            if hasattr(self, 'result_label'):
                self.result_label.config(text="Exchange rates fetched successfully!", fg="green")
        except requests.RequestException as e:
            # Use fallback rates without updating result_label if not initialized
            self.exchange_rates = {
                "kes": 129,  # USD to KES
                "eur": 1/170,  # USD to EUR (inverse of EUR to KES)
                "gbp": 1/100,  # USD to GBP (inverse of GBP to KES)
                "ugx": 25 * 129  # USD to UGX (via KES)
            }
            if hasattr(self, 'result_label'):
                self.result_label.config(text=f"Error fetching rates: {e}. Using fallback rates.", fg="red")

    def update_options(self, event=None):
        """Update conversion options based on selected conversion type."""
        if hasattr(self, 'result_label'):
            self.result_label.config(text="")
        conversion_type = self.conversion_type.get()
        if conversion_type == "Currency":
            self.options_label.config(text="Select Currency Conversion:")
            self.conversion_options.config(values=["USD to KES", "EUR to KES", "GBP to KES", "KES to UGX"])
        elif conversion_type == "Temperature":
            self.options_label.config(text="Select Temperature Conversion:")
            self.conversion_options.config(values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        elif conversion_type == "Distance":
            self.options_label.config(text="Select Distance Conversion:")
            self.conversion_options.config(values=["Kilometers to Miles", "Miles to Kilometers"])
        self.conversion_options.current(0)

    def convert(self):
        """Perform the conversion based on user input."""
        try:
            amount = float(self.amount_entry.get())
            if amount < 0:
                self.result_label.config(text="Amount cannot be negative!", fg="red")
                return
        except ValueError:
            self.result_label.config(text="Please enter a valid number!", fg="red")
            return

        conversion_type = self.conversion_type.get()
        option = self.conversion_options.get()
        result = None

        if conversion_type == "Currency":
            # Check if rates need refreshing (e.g., after 24 hours)
            if not self.exchange_rates or (self.last_fetched and (datetime.now() - self.last_fetched).days >= 1):
                self.fetch_exchange_rates()

            try:
                if option == "USD to KES":
                    rate = self.exchange_rates.get("kes", 129)
                    result = f"{amount} USD = {amount * rate:.2f} KES"
                elif option == "EUR to KES":
                    rate = self.exchange_rates.get("kes", 129) / self.exchange_rates.get("eur", 1/170)
                    result = f"{amount} EUR = {amount * rate:.2f} KES"
                elif option == "GBP to KES":
                    rate = self.exchange_rates.get("kes", 129) / self.exchange_rates.get("gbp", 1/100)
                    result = f"{amount} GBP = {amount * rate:.2f} KES"
                elif option == "KES to UGX":
                    rate = self.exchange_rates.get("ugx", 25 * 129) / self.exchange_rates.get("kes", 129)
                    result = f"{amount} KES = {amount * rate:.2f} UGX"
            except KeyError:
                self.result_label.config(text="Currency rate unavailable!", fg="red")
                return
        elif conversion_type == "Temperature":
            if option == "Celsius to Fahrenheit":
                result = f"{amount}°C = {(amount * 9/5) + 32:.2f}°F"
            elif option == "Fahrenheit to Celsius":
                result = f"{amount}°F = {(amount - 32) * 5/9:.2f}°C"
        elif conversion_type == "Distance":
            if option == "Kilometers to Miles":
                result = f"{amount} km = {amount * 0.621371:.2f} miles"
            elif option == "Miles to Kilometers":
                result = f"{amount} miles = {amount * 1.60934:.2f} km"

        self.result_label.config(text=result, fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()