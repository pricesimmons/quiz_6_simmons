#Quiz 6
#Price Simmons
#11/29/2023

import tkinter as tk
from tkinter import messagebox
from app.functions import add_numbers, subtract_numbers, divide_numbers, multiply_numbers

def calculate_and_save_numbers(first_name, last_name, num1, num2):
    # Calculate results
    add_result = add_numbers(num1, num2)
    subtract_result = subtract_numbers(num1, num2)
    divide_result = divide_numbers(num1, num2)
    multiply_result = multiply_numbers(num1, num2)

    # Format results
    results_text = (
        f"This is {first_name}'s answer.\n"
        f"{num1} + {num2} = {add_result}\n"
        f"{num1} - {num2} = {subtract_result}\n"
        f"{num1} / {num2} = {divide_result}\n"
        f"{num1} * {num2} = {multiply_result}\n"
    )

    # Save results to a file
    file_name = f"{last_name.lower()}.txt"
    with open(file_name, 'w') as file:
        file.write(results_text)

    messagebox.showinfo("Results Saved", f"Results saved to {file_name}")

def main():
    root = tk.Tk()
    root.title("Calculator App")

    first_name_label = tk.Label(root, text="First Name:")
    first_name_label.pack(pady=5)

    first_name_entry = tk.Entry(root)
    first_name_entry.pack(pady=5)

    last_name_label = tk.Label(root, text="Last Name:")
    last_name_label.pack(pady=5)

    last_name_entry = tk.Entry(root)
    last_name_entry.pack(pady=5)

    num1_label = tk.Label(root, text="Number 1:")
    num1_label.pack(pady=5)

    num1_entry = tk.Entry(root)
    num1_entry.pack(pady=5)

    num2_label = tk.Label(root, text="Number 2:")
    num2_label.pack(pady=5)

    num2_entry = tk.Entry(root)
    num2_entry.pack(pady=5)

    calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_and_save_numbers(
        first_name_entry.get(),
        last_name_entry.get(),
        float(num1_entry.get()),
        float(num2_entry.get())
    ))
    calculate_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
