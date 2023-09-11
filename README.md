[![CI/CD Workflow](https://github.com/nogibjj/IDS706_miniproject2_xk10/actions/workflows/cicd.yml/badge.svg)](https://github.com/cassiekang/IDS706_miniproject2_xk10/actions/workflows/cicd.yml)


## Pandas Descriptive Statistics Script
# Purpose
This project aims to perform EDA on the 'bmi.csv' dataset from Kaggle (https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis), which comprises 741 individual records. Here are the concise goals:
1. Dataset loading: create a codespaces environment to automatically load the 'bmi.csv' dataset using Pandas.
2. Descriptive statistics: generate basic descriptive statistics, including mean, median, standard deviation for the columns (age, height, weight, bmi).
3. data visualization: create one example visualization for age distribution.

# Preparation
1. This project was generated from the previous miniproject IDS706-template, which includes a 'Makefile', 'requirements.txt', '.devcontainer', '.gitignore', 'GithubActions' and 'README'.
2. The project incorporates an automated workflow managed through a Makefile, which efficiently handles various tasks. These tasks encompass installation (via "make install"), testing (via "make test"), code formatting (via "make format"), and code quality checks (via "make lint"). 
3. main.py:
* Reads dataset from a CSV file.
* Generates summary statistics and a histogram for the 'Age' column.
* Saves summary statistics and a histogram as Markdown and image files.
4. test_main.py:
*Tests the generate_summary_and_visualization function.
* Loads a test dataset.
* Calls the function to create a test summary report and histogram.

# Summary statistics
The dataset contains 741 records with the following key statistics:
Age: Average age is 31.6 years, ranging from 15 to 61 years.
Height: Average height is 1.709 meters, ranging from 1.46 to 2.07 meters.
Weight: Average weight is 78.4 kilograms, ranging from 25.9 to 270 kilograms.
BMI: Average BMI is 26.4, ranging from 12.15 to 66.30.
These statistics summarize the dataset's age, height, weight, and BMI attributes.

# Data visualization:
For this project, I created a histogram for age distribution

# Summary report
I used pandas' describe() function to compute statistics (count, mean, std, min, 25%, 50%, 75%, max) for all numeric columns. Then employed seaborn to create create a histogram with a KDE for the 'Age' column, visualizing its distribution. After generating statistics, I saved them in Markdown format using to_markdown(). 






