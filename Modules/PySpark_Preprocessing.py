#fonctions courantes de Python_Spark
from pyspark.sql.dataframe import DataFrame

def spark_shape(self):
    return (self.count(), len(self.columns))
pyspark.sql.dataframe.DataFrame.shape = spark_shape

