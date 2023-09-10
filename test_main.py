"""
Test goes here

"""

import main  # Import your main module
import pandas as pd  # Import pandas


def test_generate_summary_and_visualization():
    """Test the generate_summary_and_visualization function in main.py"""
    input_file_path = "bmi.csv"  
    output_summary_report = "test_summary_report.md"
    histogram_image_path = "test_age_histogram.png"

    # Read the dataset using pandas
    data = pd.read_csv(input_file_path)

    # Call the function from main.py with the DataFrame
    main.generate_summary_and_visualization(
        data, output_summary_report, histogram_image_path
    )


if __name__ == "__main__":
    test_generate_summary_and_visualization()
