import os
import pandas as pd

# Set the root directory of the image
dataset_root = "Images"

image_data = pd.DataFrame(columns=["image_path", "label"])

for root, dirs, files, in os.walk(dataset_root):
    # Iterate over each file in the current directory
    for file in files:
        # Combine the root directory and file name to get the complete image path
        image_path = os.path.join(root, file)

        # Extract the label or class name from the directory name
        label = os.path.basename(root)

        # Create a new DataFrame with the image path and label as values
        row = pd.DataFrame({"image_path": [image_path], "label": [label]})

        # Concatenate the new row with the existing image_data DataFrame
        image_data = pd.concat([image_data, row], ignore_index=True)
    
image_data.to_csv("image_dataset.csv", index=False)

file_path = "image_dataset.csv"
os.startfile(file_path)