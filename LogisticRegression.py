from pyspark.ml.classification import LogisticRegression


log_reg = LogisticRegression(labelCol="label", featuresCol="features_dt")
log_model = log_reg.fit(dt_data)

print(f"Logistic Regression Intercept: {log_model.intercept}")
print(f"Logistic Regression Coefficients: {log_model.coefficients}")
