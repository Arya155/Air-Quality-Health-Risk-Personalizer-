import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Air Quality Health Risk Personalizer")
root.geometry("700x650")
root.configure(bg="#dff6ff")

# Title
heading = tk.Label(
    root,
    text="Air Quality Health Risk Personalizer",
    font=("Arial", 20, "bold"),
    bg="#dff6ff",
    fg="#003566"
)
heading.pack(pady=20)

# Name
name_label = tk.Label(root, text="Enter Your Name", font=("Arial", 12), bg="#dff6ff")
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Age
age_label = tk.Label(root, text="Enter Your Age", font=("Arial", 12), bg="#dff6ff")
age_label.pack()
age_entry = tk.Entry(root, width=40)
age_entry.pack(pady=5)

# Health Condition
health_label = tk.Label(root, text="Health Condition", font=("Arial", 12), bg="#dff6ff")
health_label.pack()

health_var = tk.StringVar()
health_var.set("Normal")

health_menu = tk.OptionMenu(
    root,
    health_var,
    "Normal",
    "Asthma",
    "Heart Problem",
    "Allergy",
    "Respiratory Disease"
)
health_menu.pack(pady=5)

# AQI Input
AQI_label = tk.Label(root, text="Enter AQI Value", font=("Arial", 12), bg="#dff6ff")
AQI_label.pack()

AQI_entry = tk.Entry(root, width=40)
AQI_entry.pack(pady=5)

# Result Box
result_box = tk.Text(root, height=15, width=70, font=("Arial", 11))
result_box.pack(pady=20)

# Function

def analyze_air_quality():
    result_box.delete("1.0", tk.END)

    name = name_entry.get()
    age = age_entry.get()
    health = health_var.get()

    try:
        aqi = int(AQI_entry.get())
    except:
        messagebox.showerror("Error", "Please enter a valid AQI value")
        return

    # AQI Category
    if aqi <= 50:
        category = "Good"
        risk = "Low"
        advice = "Air quality is satisfactory. Enjoy outdoor activities."

    elif aqi <= 100:
        category = "Moderate"
        risk = "Medium"
        advice = "Sensitive people should reduce prolonged outdoor activity."

    elif aqi <= 150:
        category = "Unhealthy for Sensitive Groups"
        risk = "High"
        advice = "Children and elderly people should avoid outdoor exercise."

    elif aqi <= 200:
        category = "Unhealthy"
        risk = "Very High"
        advice = "Wear masks and avoid outdoor activities."

    elif aqi <= 300:
        category = "Very Unhealthy"
        risk = "Severe"
        advice = "Stay indoors as much as possible."

    else:
        category = "Hazardous"
        risk = "Extreme"
        advice = "Emergency conditions. Avoid going outside."

    # Personalized Suggestions
    extra_advice = ""

    if health == "Asthma":
        extra_advice = "\nAsthma Alert: Carry inhaler and avoid polluted areas."

    elif health == "Heart Problem":
        extra_advice = "\nHeart Care: Avoid stress and outdoor exercise."

    elif health == "Allergy":
        extra_advice = "\nAllergy Alert: Use masks and keep windows closed."

    elif health == "Respiratory Disease":
        extra_advice = "\nRespiratory Care: Use air purifier if available."

    # Age Based Advice
    age_advice = ""

    try:
        age = int(age)

        if age < 12:
            age_advice = "\nChildren are highly sensitive to polluted air."

        elif age > 60:
            age_advice = "\nSenior citizens should avoid outdoor exposure."

    except:
        age_advice = ""

    # Final Output
    output = f"""
Hello, {name}

AQI Value: {aqi}
Air Quality Category: {category}
Health Risk Level: {risk}

General Advice:
{advice}

Health Recommendation:
{extra_advice}

Age Based Recommendation:
{age_advice}

Stay Safe and Breathe Clean Air!
"""

    result_box.insert(tk.END, output)

# Analyze Button
analyze_button = tk.Button(
    root,
    text="Analyze Health Risk",
    font=("Arial", 14, "bold"),
    bg="#0077b6",
    fg="white",
    command=analyze_air_quality
)

analyze_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=root.quit
)

exit_button.pack(pady=10)

# Main Loop
root.mainloop()


