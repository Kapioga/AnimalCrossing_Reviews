import pyspark
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField, IntegerType

import kaggle
import kagglehub
from kaggle.api.kaggle_api_extended import KaggleApi

from streamlit import header

import Unzip
from RemoveFolder import removeFolder

# Prior to downloading any csv file from Kaggle, you must create an account and create a new token
# Pulls and stores Kaggle dataset into project file
api = KaggleApi()
api.authenticate()

mainPath = kaggle.api.dataset_download_files("jessemostipak/animal-crossing", path='.')
metadata = kaggle.api.dataset_metadata("jessemostipak/animal-crossing", path='.')
files = kaggle.api.dataset_list_files('jessemostipak/animal-crossing').files
unzippedDatasetPath = './Dataset'

#Checks if user would like to unzip file if Dataset is unavailable
# Unzips File
Unzip_Prompt = input("Would you like to unzip? [Y/N] ")
if Unzip_Prompt == "y" or Unzip_Prompt == "Y":
    newUnzippedPath = Unzip.Unzip()
    unzippedDatasetPath = newUnzippedPath
    print("File has been created" + newUnzippedPath)
else:
    print("Proceed!")

# Checks user would like to remove a folder
removeFolder()

print("Path to dataset files:", unzippedDatasetPath)

#
# spark = SparkSession.builder.appName("Animal Crossing Dataframe").getOrCreate()
# df = spark.read.load('Dataset/villagers.csv', format='csv', sep=',', header=True, escape='"', inferschema ='true')


