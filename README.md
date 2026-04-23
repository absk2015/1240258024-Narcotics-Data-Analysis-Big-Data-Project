# 📊 Narcotics Data Analysis using Hadoop Big Data Project

![Hadoop](https://img.shields.io/badge/Big%20Data-Hadoop-yellow)
![Python](https://img.shields.io/badge/Language-Python-blue)
![Hive](https://img.shields.io/badge/Query-Hive-orange)
![Status](https://img.shields.io/badge/Project-Academic-success)

## Problem Statement
Drug trafficking is a major law enforcement challenge in India. This project processes narcotics seizure data across Indian states using Hadoop MapReduce to identify the most prevalent drug types and highest-risk states.

## Dataset Description
File: dataset.csv  
Format: CSV  
Columns: Year, State, Drug_Type, Cases, Quantity_kg, Arrests  
Records: 30 rows covering 5 states and 5 drug types from 2018 to 2023.

## Steps to Run

1. Start Hadoop services:
```
start-dfs.sh
start-yarn.sh
```

2. Upload dataset to HDFS:
```
hdfs dfs -mkdir /narcotics
hdfs dfs -put dataset.csv /narcotics/
```

3. Run MapReduce job:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /narcotics/dataset.csv \
  -output /narcotics/output \
  -mapper Mapper.py \
  -reducer Reducer.py \
  -file Mapper.py \
  -file Reducer.py
```

4. View output:
```
hdfs dfs -cat /narcotics/output/part-00000
```

## Sample Output
```
Cannabis        2680
Cocaine          905
Delhi           1985
Heroin          1955
Maharashtra     2010
Methamphetamine 1260
Opium           3130
Punjab          2645
Rajasthan       2710
Uttar Pradesh   2275
```

## Technologies Used
- Hadoop (HDFS, MapReduce)
- Hive
- Python
- Linux
- Cloudera
