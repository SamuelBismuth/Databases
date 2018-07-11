import findspark
from pyspark import SparkContext
import os

findspark.init("/home/sam/Hardware/pyspark")
sc = SparkContext("local[*]", "Simple App")

dir_path = os.path.dirname(os.path.realpath(__file__))

text_file = sc.textFile(dir_path + "/../data/data set.txt")

text_file_feature = sc.textFile(dir_path + "/../data/data set adding feature.txt")
