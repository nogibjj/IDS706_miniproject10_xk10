[![CI/CD Workflow](https://github.com/nogibjj/IDS706_miniproject10_xk10/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_miniproject10_xk10/actions/workflows/cicd.yml)

# Miniproject10: Introduction to PySpark and Innovation in Energy and Public Health
## Purpose:
The purpose of this project is to leverage the powerful capabilities of PySpark for processing large datasets, a task essential in the field of data science and analytics. PySpark, being a distributed computing framework, is particularly well-suited for handling voluminous data efficiently. In this project, we focus on applying PySpark to analyze and manipulate a substantial dataset extracted from FiveThirtyEight's public repositories. The dataset in question pertains to birth records in the United States, spanning a decade from 1994 to 2003. This rich dataset offers a plethora of opportunities for insightful analysis and data-driven discoveries.

A key component of this project is the utilization of Spark SQL, an integral part of the Apache Spark ecosystem, which allows for querying data in a highly efficient and scalable manner. By employing Spark SQL, we aim to delve into the dataset to extract meaningful patterns, trends, and statistics. This SQL-like interface seamlessly integrates with PySpark, providing a familiar yet powerful tool for data analysts and scientists.

Furthermore, the project includes a vital aspect of data transformation, a necessary step in preparing the raw data for analysis. This transformation process involves cleaning the data, normalizing it, and implementing various manipulations to make the data more suitable for analysis. Such transformations are crucial in data science workflows to ensure the accuracy and reliability of the results.

## Steps:
1. Update requirements.txt:
Add PySpark and any other necessary dependencies to your requirements.txt. 
2. Organize the my.lib directory:
into meaningful sub-modules for clarity and maintainability. For instance, separate data extraction, transformation, loading, and querying functionalities into distinct files.
Extract.py: Handles downloading a dataset from a URL using the requests library. Implement error handling and possibly caching.
Transform.py: Includes functions to clean and filter the dataset. This may involve normalizing data, handling missing values, and other transformations relevant to your dataset.
Load.py: Responsible for loading the transformed data into an SQLite database. This will involve SQL operations, possibly using a library like SQLite3 or SQLAlchemy.
Query.py: Contains functions to perform SQL queries on the data, including retrieval, updates, and creation of new records.
Edit main.py to Call the Functions:
3. Import and sequentially call the functions from the my.lib modules. 
The main function should flow logically, from extracting data, transforming it, loading it into the database, and then querying or updating the database.
4. Add Test Cases in test_main.py:
Write unit tests for each function in the main.py. Ensure that each function behaves as expected under various conditions.
Mock external dependencies like the network or database to make your tests more reliable and faster.
5. Create an Output File:
Using a markdown file (pyspark_output.md) for logging outputs of different operations. Ensure that your functions in main.py and my.lib write relevant information to this file for auditing and debugging purposes.
## Check format and test:
Use make install, make format, make lint, make test command.


<img width="1149" alt="Screen Shot 2023-11-14 at 01 40 42" src="https://github.com/nogibjj/IDS706_miniproject10_xk10/assets/143849077/0a1a79f3-8a81-491c-9c93-b34542417c2b">


The results can be found in pyspark_output.md
