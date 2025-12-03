import opendatasets as od
import pandas as pd
import os

# Download the dataset
dataset_url = 'https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud'
od.download(dataset_url)

# The dataset is downloaded into a directory named 'creditcardfraud'
data_dir = 'creditcardfraud'
csv_file = os.path.join(data_dir, 'creditcard.csv')

# Load the dataset
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    print("Dataset loaded successfully!")
    print(df.head())
else:
    print(f"Error: {csv_file} not found.")
