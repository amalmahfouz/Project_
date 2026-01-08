from pyspark.ml.regression import LinearRegression


assembler_lr = VectorAssembler(inputCols=["age", "duration"], outputCol="features_lr")
lr_data = assembler_lr.transform(df)


lr = LinearRegression(featuresCol="features_lr", labelCol="balance")
lr_model = lr.fit(lr_data)


print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")
