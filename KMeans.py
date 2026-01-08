from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler 


assembler = VectorAssembler(inputCols=["age", "balance"], outputCol="features")
training_data = assembler.transform(df)


kmeans = KMeans().setK(3).setSeed(1)
model = kmeans.fit(training_data)

centers = model.clusterCenters()
print("(Cluster Centers):")
for center in centers:
    print(center)


display(df.select("age", "balance").describe())
