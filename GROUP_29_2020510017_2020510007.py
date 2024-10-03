import csv  # Import the CSV module to work with CSV files
import tkinter as tk  # Import tkinter for creating graphical user interface

def arrange_messagebox(title, message, buttons):
    
    # Define a function to handle button clicks in the message box
    def on_button_click(button_text):
        print(f"Button '{button_text}' clicked")
        messagebox.destroy()  # Destroy the message box when a button is clicked
    
    messagebox = tk.Toplevel(root)  # Create a new top-level window for the message box
    messagebox.title(title)  # Set the window title with the provided title
    message_label = tk.Label(messagebox, text=message, padx=20, pady=20)  # Create a label with padding for the message
    message_label.pack()  # Pack the label into the message box window
    
    button_frame = tk.Frame(messagebox)  # Create a frame to hold buttons
    button_frame.pack(pady=10)  # Pack the frame with vertical padding
    
    for button_text in buttons:
            # Create a button for each item in the buttons list
            def handle_click(bt=button_text):
                on_button_click(bt)
            
            button = tk.Button(button_frame, text=button_text, command=handle_click, padx=10, pady=5)
            button.pack(side=tk.LEFT, padx=5)  # Pack buttons to the left side with horizontal padding
    
    messagebox.update_idletasks()  # Update the message box to calculate sizes
    width = messagebox.winfo_width()  # Get the calculated width
    height = messagebox.winfo_height()  # Get the calculated height
    x = (messagebox.winfo_screenwidth() // 2) - (width // 2)  # Calculate the x coordinate to center the window
    y = (messagebox.winfo_screenheight() // 2) - (height // 2)  # Calculate the y coordinate to center the window
    messagebox.geometry(f'{width}x{height}+{x}+{y}')  # Set the geometry of the window to center it
    
    messagebox.transient(root)  # Set the message box to be a temporary window of the root
    messagebox.grab_set()  # Set the message box to grab all events from the user
    root.wait_window(messagebox)  # Wait for the message box to be closed before continuing



def read_and_prepare_csv(filename):
    
    dataList = []  # a list to hold the data
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)  # Create a CSV reader
        headers = next(reader)  # Read the headers from the first row
        first_row = next(reader)  # Read the second (data) row
        record = [float(value) for value in first_row[:-1]]  # Convert all values except the last one to float
        record.append(int(first_row[-1]))  # Convert the last value to int and append it to the record
        dataList.append(record)  # Append the first record to the data list
        
        min_values = record[:-1]  # Initialize min values from the first record
        max_values = record[:-1]  # Initialize max values from the first record
        
        for row in reader:
            record = [float(value) for value in row[:-1]]  # Convert all values except the last one to float
            record.append(int(row[-1]))  # Convert the last value to int and append it to the record

            dataList.append(record)  # Append each record to the data list
            for i in range(len(record[:-1])):
                min_values[i] = min(min_values[i], record[i])  # Update the min values
                max_values[i] = max(max_values[i], record[i])  # Update the max values
    
    # Normalize the data using min and max values
    for record in dataList:
        for i in range(len(min_values)):
            record[i] = (record[i] - min_values[i]) / (max_values[i] - min_values[i])  # Normalize each feature
    
    with open('diabetes_preprocessed.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # Write the headers to the new file
        writer.writerows(dataList)  # Write the normalized data to the new file
    
    return dataList, min_values, max_values  # Return the processed data and min/max values



def get_input_data():
    
    input_data = []  # Initialize a list to store input data
    for entry in entries:
        value = entry.get()  # Get the value from each entry widget
        if not value:
            arrange_messagebox("Error", "You should fill all the fields!", ["OK"])  # Display an error if any field is empty
            return None
        input_data.append(float(value))  # Convert the input to float and add to the list
    
    k_value = k_entry.get()  # Get the value of k closest number of datas from the entry
    
    if not k_value.isdigit() or int(k_value) < 1:  # Validate that k is a positive integer
        arrange_messagebox("Error", "Invalid value for k. It must be a positive integer.", ["OK"])  # Error message if k is invalid
        return None
    
    for i, value in enumerate(input_data):
        if value < min_values[i] or value > max_values[i]:  # Check if the input value is within the valid range
            arrange_messagebox("Error", f"{columns[i]} value should be in the range {min_values[i]} - {max_values[i]} !", ["OK"])  # Display error message if out of range
            return None
    
    return input_data, int(k_value)  # Return the validated input data and k value



def calculate_diabetes_probability():
    
    input_data_and_k = get_input_data()  # Get and validate the input data and k value
    if input_data_and_k is None:
        return  # Return if the input data or k value is invalid
    
    input_data, k = input_data_and_k  # Unpack the input data and k value
    standardized_input = [(value - min_values[i]) / (max_values[i] - min_values[i]) for i, value in enumerate(input_data)]  # Standardize the input data
    
    distances = []  # Initialize a list to store distances
    for record in diabetes_data:
        dist = sum((a - b) ** 2 for a, b in zip(standardized_input, record[:-1])) ** 0.5  # Calculate Euclidean distance
        distances.append((dist, record[-1]))  # Append the distance and the outcome
    
    distances.sort(key=lambda x: x[0])  # Sort distances in ascending order
    
    closest_k = distances[:k]  # Select the closest k records
    
    diabetic_count = 0  # Initialize the count of diabetic records to zero
    
    for record in closest_k:
        if record[1] == 1:  # Check if the outcome is diabetic (1)
            diabetic_count += 1  # Increment the diabetic count if the condition is met
            
    probability = (diabetic_count / k) * 100  # Calculate the probability of being diabetic
    
    arrange_messagebox("Result", f"Diabetes probability: %{probability:.2f}", ["OK"])  # Show the calculated probability
    
    for entry in entries:
        entry.delete(0, tk.END)  # Clear all input fields after calculation



root = tk.Tk()  # Create the main window
root.title("Diabetes Control App")  # Set the title of the main window
root.configure(bg="beige")  # Set the background color of the window

columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]  # List of input fields
entries = []  # Initialize a list to store entry widgets



for i, column in enumerate(columns):
    
    label = tk.Label(root, text=column, bg="beige", fg="brown", font=("italic", 10, "bold"))  # Create and configure a label for each input field
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)  # Place the label in the grid
    entry = tk.Entry(root, bg="white", fg="black")  # Create an entry widget for user input
    entry.grid(row=i, column=1, padx=10, pady=5)  # Place the entry widget in the grid
    entries.append(entry)  # Add the entry widget to the list of entries



k_label = tk.Label(root, text="Value of k (Number of Closest Data)", bg="beige", fg="brown", font=("italic", 10, "bold"))  # Create a label for the k input field
k_label.grid(row=len(columns), column=0, padx=10, pady=5, sticky=tk.W)  # Place the k label in the grid
k_entry = tk.Entry(root, bg="white", fg="black")  # Create an entry widget for the k value
k_entry.grid(row=len(columns), column=1, padx=10, pady=5)  # Place the k entry widget in the grid


button = tk.Button(root, text="Calculate", command=calculate_diabetes_probability, bg="darkorange", fg="white", font=("italic", 10, "bold"))  # Create a button to start the calculation
button.grid(row=len(columns) + 1, column=0, columnspan=2, pady=10)  # Place the button in the grid


diabetes_data, min_values, max_values = read_and_prepare_csv('diabetes.csv')  # Read and preprocess the diabetes data from the CSV file


root.mainloop()  # Start the main event loop of the application
