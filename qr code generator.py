# Import required libraries
import qrcode
import tkinter as tk
from tkinter import messagebox

# Function to generate UPI QR code
def generate_qr():
    # Get UPI ID from input field
    upi_id = entry.get()
    # Create UPI payment URL
    data = f"upi://pay?pa={upi_id}"
    # Generate QR code
    img = qrcode.make(data)
    # Save QR code image
    img.save("upi_qrcode.png")
    # Show success message
    messagebox.showinfo("UPI QR", "UPI QR code saved as upi_qrcode.png")

# Create main window
root = tk.Tk()
root.title("UPI QR Generator")
root.geometry("400x300")  # Set window size

# Add label and input field for UPI ID
tk.Label(root,text="Enter UPI ID:",font=("Arial",14)).pack(pady=20)
entry=tk.Entry(root,width=40,font=("Arial",12))
entry.pack(pady=10)

# Add button to generate QR code
tk.Button(root,text="Generate",command=generate_qr,bg="#4CAF50",fg="white",font=("Arial",12)).pack(pady=20)

# Start the GUI event loop
root.mainloop()