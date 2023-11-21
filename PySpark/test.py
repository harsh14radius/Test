from pyspark.sql import SparkSession
import pandas as pd
import pyspark
import time

spark=SparkSession.builder.appName('start').getOrCreate()
start= time.time()
df1=spark.read.options().parquet(r"D:\Data_Files\data_ingestion\final.parquet",inferSchema=True)
total_rows = df1.count()
print(total_rows)
stop=time.time()
elapsed_time = (stop - start)
print(f"Time taken by my_function: {elapsed_time} seconds")
print('df1 read')
df1.head(4)
start= time.time()
parquet_path=("D:/Data_Files/data_ingestion/final_files/final.parquet",
              "D:/Data_Files/data_ingestion/final_files/final1.parquet",
              "D:/Data_Files/data_ingestion/final_files/final2.parquet",
              "D:/Data_Files/data_ingestion/final_files/final3.parquet",
              "D:/Data_Files/data_ingestion/final_files/final4.parquet")

df=spark.read.options().parquet(*parquet_path)
total_rows = df.count()
print(total_rows)
stop=time.time()
elapsed_time = (stop - start)
print(f"Time taken by my_function: {elapsed_time} seconds")
print('df read')

# print("head",df.head(2))
# print("schema",df.printSchema())
# print("type",type(df))
# print("columns",df.columns)
# print("tail",df.tail(5))
# df.select('location_id').show(3)
# df.select(['location_id','creation_time']).show()

# df.select('location_id')

unique_sensor_values = df.select("location_id").distinct().rdd.map(lambda row: row[0]).collect()
print(unique_sensor_values)




print("end")