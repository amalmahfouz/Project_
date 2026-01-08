from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer


indexer = StringIndexer(inputCol="y", outputCol="label")
df_indexed = indexer.fit(df).transform(df)


assembler_dt = VectorAssembler(inputCols=["age", "balance", "duration"], outputCol="features_dt")
dt_data = assembler_dt.transform(df_indexed)


dt = DecisionTreeClassifier(labelCol="label", featuresCol="features_dt")
dt_model = dt.fit(dt_data)


print(f"Decision Tree Nodes: {dt_model.numNodes}")
print(f"Tree Depth: {dt_model.depth}")
