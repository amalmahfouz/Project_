# Project_
Cloud-Based Distributed Data Processing Service
Mahmoud Mahfouz 120212332,        Student2 name (ID

Faculty of Information Technology
The Islamic University of Gaza

A Requirement for the Course: Cloud and Distributed Systems (SICT 4313)
Instructor: Dr. Rebhi S. Baraka
Abstract
Our project explores the potential of distributed computing for processing, analyzing, and scaling large datasets using the Databricks cloud platform. We also utilized data from UCI Machine Learning and employed Apache Spark to handle the required tasks.
Two strategies were employed for data processing:
First, descriptive data analysis to obtain descriptive information about the file uploaded to the Databricks platform, such as the number of rows and columns, and to identify the data type, displaying the Mean, Stddev, Min, and Max values for all data.
Second, machine learning was implemented using the Spark MLlib library, employing concepts such as KMeans, LinearRegression, DecisionTreeClassifier, and LogisticRegression.
Introduction
In this project, you will be able to process big data and obtain analysis and predictions for future data.
The main goal is to leverage Apache Spark to analyze the data we want to work with, uncover expected data behavior, and thus facilitate understanding big data and obtaining quick conclusions.
As a team, we have worked on the Databricks platform, but this platform is serverless, with the cloud automatically scaling horizontally and executing at high speed. Therefore, we were unable to work on more than one node (manually) . However, the basic concept is that the platform distributes data across multiple nodes to work in parallel and quickly.




Cloud Program/Service Requirements 
•	User Stories
1.	As a data analyst, I want to upload large CSV files to the cloud for efficient processing.
2.	As a user, I want to view a statistical summary (mean, minimum, maximum, standard deviation) of the data to understand it.
3.	As a business manager, I want to use machine learning to predict potential behavior based on historical data.
4.	As a system administrator, I want to run the software on a distributed network to handle increasing data volumes without performance degradation.
2.	Architecture and Design 
1.	Software Architecture with Spark
The program architecture follows way integrated within the Databricks environment. At 
the core, the Spark Driver coordinates the execution, while the Executor Nodes process 
data in parallel.
Storage Layer: Data is stored in the Databricks File System (DBFS).
Processing Layer: PySpark Data Frames are used for distributed operations.
MLlib Layer: Provides the machine learning pipelines for analysis.

2. Machine Learning Pipeline Design
Data Pre-processing: Reading the CSV with custom delimiters and schema inference.
Model Training: Executing four algorithms:
 [ K-Means, Linear/Logistic Regression, Decision Tree] 

3. Flow Diagram of the System
The system flow starts from :
-	the user interface (Notebook Widgets), 
-	passes through the Spark execution engine, 
-	ends with the visualization of results. 

3.	Implementation
-	Implementation Details & Libraries
The program was implemented using PySpark, Python API for Apache Spark, the following libraries we were used it:
pyspark.sql: Used for data manipulation, handling Data Frames, and performing descriptive statistics: 
as: df = spark.read.table("spark_project_2026.default.bank_full2")
pyspark.ml (MLlib): Used for building the machine learning pipelines, specific algorithms (K-Means, Linear Regression, Decision Tree, and Logistic Regression).
-	Data modeling and processing
When creating a table and loading large amounts of data onto it, we must ensure that it is read correctly. Columns are separated using semicolons (;) to guarantee that each column is read individually and that the data type in each column can be distinguished.

Mapping between Program and Cloud Platform
 The mapping is as follows:
- Storage: The CSV file is hosted on DBFS (Databricks File System).
- Computation: The code is executed on a Serverless Spark Cluster. The Spark Driver converts the Python code into serialized tasks that are distributed across the worker nodes.
- Deployment: The program is deployed as an interactive Notebook, which serves as the interface for both code execution and result visualization.


4.	Experiments and Evaluation
We are evaluating the performance of distributed data processing using Spark on the Databricks cloud platform. We measured the execution time of the K-Means clustering algorithm, which took 11 seconds to process 45,211 records in our distributed environment.
However, the remaining values are assumed because the system is serverless and the platform scales automatically as the data increases.
Cluster Size	Execution Time (sec)	Speedup	Efficiency
1 Machine	44	1	100%
2 Machines	23.2	1.90	95%
4 Machines	12.5	3.52	88%
8 Machines	11	4	50%
      All our values are hypothetical, and all we have concluded is that 11 seconds is the actual time that appeared on the platform, but based on research and inquiry, we have concluded that this value may be based on the operation of more than one device.
5.	User Support
This program is designed to be intuitive and user-friendly within the Databricks environment. To operate the service, follow these steps:
1. Open the Databricks workspace and ensure that a Spark Cluster (Standard or Serverless) is running.
2. The dataset bank-full.csv is pre-loaded into the DBFS. The first cell of the notebook handles the ingestion automatically.
3.  The user can interact with the program using the built-in widgets. 
4. Click on 'Run cell' to execute the pipeline, which includes descriptive statistics and the four machine learning algorithms. 
The Cloud Program Link (Databricks): 
https://dbc-ff2ce86e-fd5b.cloud.databricks.com/editor/notebooks/2019870273259777?o=7474655777324619


the link to the GitHub repository: 
https://github.com/amalmahfouz/Project_.git
the link to the video:


6.	 Conclusion
As a conclusion from our work and experience on the Databricks platform using Apache Spark, we were able to process a file consisting of thousands of rows and obtain descriptive data analysis, in addition to implementing machine learning algorithms that help predict data behavior.
Challenges and Problems: One of the most challenges was the initial data ingestion due to the use of non-standard separators (semicolons) in the CSV file. This problem was solved by adjusting the Spark Data Frame reader. Furthermore, working in a serverless environment required a different approach to performance measurement, since node management is handled separately by the platform.

References
 [1] 
[2] 
…
