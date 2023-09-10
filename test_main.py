"""
Test goes here

"""
import os
import main


def test_read_dataset():
    # Check if the dataset file exists
    dataset_file = "bmi.csv"  # Update with your dataset file name
    assert os.path.exists(dataset_file)


def test_generate_summary_and_visualization():
    # Read the dataset
    dataset_file = "bmi.csv"  # Update with your dataset file name
    data = main.read_dataset(dataset_file)

    # Check if summary statistics are calculated correctly
    summary_stats = main.generate_summary_and_visualization(
        data, "Age", "histogram.png", "summary_report.md"
    )

    # You can add additional assertions here to check the generated summary statistics or visualization if needed.


if __name__ == "__main__":
    test_read_dataset()
    test_generate_summary_and_visualization()
