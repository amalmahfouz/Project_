# Project_
Cloud-Based Distributed Data Processing Service
Mahmoud Mahfouz 120212332,       
Student2 name (ID

A Requirement for the Course: Cloud and Distributed Systems (SICT 4313)
Instructor: Dr. Rebhi S. Baraka

Abstract
Our project explores the potential of distributed computing for processing, analyzing, and scaling large datasets using the Databricks cloud platform. We also utilized data from UCI Machine Learning and employed Apache Spark to handle the required tasks.
Two strategies were employed for data processing:
First, descriptive data analysis to obtain descriptive information about the file uploaded to the Databricks platform, such as the number of rows and columns, and to identify the data type, displaying the Mean, Stddev, Min, and Max values for all data.
Second, machine learning was implemented using the Spark MLlib library, employing concepts such as KMeans, LinearRegression, DecisionTreeClassifier, and LogisticRegression.

This program is designed to be intuitive and user-friendly within the Databricks environment. To operate the service, follow these steps:
1. Open the Databricks workspace and ensure that a Spark Cluster (Standard or Serverless) is running.
2. The dataset bank-full.csv is pre-loaded into the DBFS. The first cell of the notebook handles the ingestion automatically.
3.  The user can interact with the program using the built-in widgets. 
4. Click on 'Run cell' to execute the pipeline, which includes descriptive statistics and the four machine learning algorithms. 
The Cloud Program Link (Databricks): 


Service Requirements 
•	User Stories
1.	As a data analyst, I want to upload large CSV files to the cloud for efficient processing.
2.	As a user, I want to view a statistical summary (mean, minimum, maximum, standard deviation) of the data to understand it.
3.	As a business manager, I want to use machine learning to predict potential behavior based on historical data.
4.	As a system administrator, I want to run the software on a distributed network to handle increasing data volumes without performance degradation.



As a conclusion from our work and experience on the Databricks platform using Apache Spark, we were able to process a file consisting of thousands of rows and obtain descriptive data analysis, in addition to implementing machine learning algorithms that help predict data behavior.
Challenges and Problems: One of the most challenges was the initial data ingestion due to the use of non-standard separators (semicolons) in the CSV file. This problem was solved by adjusting the Spark Data Frame reader. Furthermore, working in a serverless environment required a different approach to performance measurement, since node management is handled separately by the platform.


