import tkinter as tk
import pickle
import numpy as np

# Load the pretrained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_species():
    try:
        # Get user inputs
        inputs = [
            float(entry_sepal_length.get()),
            float(entry_sepal_width.get()),
            float(entry_petal_length.get()),
            float(entry_petal_width.get())
        ]
        inputs = np.array(inputs).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(inputs)
        result = prediction[0]

        # Display the result in the label
        label_result.config(text=f"The predicted species is: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Iris Flower Predictor")

# Input Fields
tk.Label(root, text="Sepal Length (cm):").grid(row=0, column=0, padx=10, pady=5)
entry_sepal_length = tk.Entry(root)
entry_sepal_length.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sepal Width (cm):").grid(row=1, column=0, padx=10, pady=5)
entry_sepal_width = tk.Entry(root)
entry_sepal_width.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Petal Length (cm):").grid(row=2, column=0, padx=10, pady=5)
entry_petal_length = tk.Entry(root)
entry_petal_length.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Petal Width (cm):").grid(row=3, column=0, padx=10, pady=5)
entry_petal_width = tk.Entry(root)
entry_petal_width.grid(row=3, column=1, padx=10, pady=5)

# Predict Button
predict_button = tk.Button(root, text="Predict Species", command=predict_species)
predict_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label for showing the result
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
