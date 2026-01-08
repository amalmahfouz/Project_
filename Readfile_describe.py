
table_name = "spark_project_2026.default.bank_full2"

df = spark.read.table("spark_project_2026.default.bank_full2")


row_count = df.count()
print(f"Number of Rows : {row_count}")


col_count = len(df.columns)
print(f"Number of Columns:  {col_count}")

print("Data Types")
df.printSchema()

print("result :")
display(df.describe())
