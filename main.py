"""
Main code
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read the dataset from either CSV or Excel
def read_dataset(dataset_file):
    try:
        if dataset_file.endswith(".csv"):
            return pd.read_csv(dataset_file)
        elif dataset_file.endswith(".xlsx"):
            return pd.read_excel(dataset_file)
        else:
            raise ValueError(
                "Unsupported file format. Please provide a CSV or Excel file."
            )
    except FileNotFoundError as e:
        print(f"Error: File '{dataset_file}' not found. {e}")
        return None


# Function to generate summary statistics and create a data visualization
def generate_summary_and_visualization(df, column_name, output_image, output_file):
    if df is not None:
        summary_stats = df.describe()
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column_name], kde=True)
        plt.title(f"{column_name} Distribution")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.savefig(output_image, bbox_inches="tight")
        plt.close()

        with open(output_file, "w", encoding="utf-8") as markdown_file:
            markdown_file.write(summary_stats.to_markdown())
            markdown_file.write(f"\n![Histogram]({output_image})\n")
        print(f"Summary report saved to {output_file}")
    else:
        print("Error: DataFrame is None. Make sure to read the dataset first.")


if __name__ == "__main__":
    data_file = "bmi.csv"
    output_summary_report = "summary_report.md"
    histogram_image_path = "histogram.png"  # Path to save the histogram image

    # Read the dataset
    data = read_dataset(data_file)

    # Generate summary statistics and create a data visualization
    generate_summary_and_visualization(
        data, "Age", histogram_image_path, output_summary_report
    )
