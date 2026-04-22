# 💊 Narcotics Data Analysis using Hadoop

**Big Data Fundamentals Project**  
*Implemented using Hadoop Ecosystem (HDFS, MapReduce, Hive)*

---

## 📌 Project Overview

This project demonstrates a **complete Big Data processing pipeline** to analyze narcotics seizure data across Indian states using the Hadoop ecosystem.

Drug trafficking is one of India's most pressing law enforcement challenges. Traditional systems struggle to process and analyze large volumes of narcotics data efficiently.

This project solves that problem using **distributed computing techniques** to extract meaningful insights such as:

* Total cases registered per drug type
* High-risk states with maximum narcotics activity
* Year-wise trends in drug seizures

---

## 🎯 Objectives

* To store large datasets using **HDFS**
* To process data using **MapReduce (Python)**
* To perform analytical queries using **Hive**
* To understand distributed data processing
* To generate insights from raw narcotics data

---

## 🏗️ Architecture

```
Raw CSV Dataset
        ↓
HDFS (Storage Layer)
        ↓
MapReduce (Processing Layer)
        ↓
Processed Output (HDFS)
        ↓
Hive (Analysis Layer)
        ↓
Insights (Top Drug Types & States)
```

---

## ⚙️ Technologies & Tools Used

* HDFS (Storage Layer)
* MapReduce (Data Processing)
* Hive (Data Analysis)
* Python 3
* Linux / Cloudera
* ChatGPT (Generative AI Assistance)

---

## 📊 Dataset Information

The dataset contains narcotics seizure records across 5 Indian states from 2018–2023.

### 📌 Key Attributes:

| Column | Description |
|--------|-------------|
| Year | Year of the narcotics case |
| State | Indian state (UP, Maharashtra, Punjab, Rajasthan, Delhi) |
| Drug_Type | Type of narcotic (Heroin, Cocaine, Opium, Cannabis, Methamphetamine) |
| Cases | Number of cases registered |
| Quantity_kg | Quantity seized (in kilograms) |
| Arrests | Number of arrests made |

---

## 🔄 Workflow Explanation

* The dataset is stored in HDFS for distributed storage
* MAPPER_CODE.py processes each row and emits drug_type and state as keys
* REDUCER_CODE.py aggregates total cases per drug type and per state
* Processed output is stored back in HDFS
* Hive is used to query and analyze the aggregated results

---

## ▶️ Steps to Run

### 1. Start Hadoop Services
```bash
start-dfs.sh
start-yarn.sh
```

### 2. Upload Dataset to HDFS
```bash
hdfs dfs -mkdir /narcotics
hdfs dfs -put NARCOTICS_DATASET.csv /narcotics/
```

### 3. Run MapReduce Job
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /narcotics/NARCOTICS_DATASET.csv \
  -output /narcotics/output \
  -mapper MAPPER_CODE.py \
  -reducer REDUCER_CODE.py \
  -file MAPPER_CODE.py \
  -file REDUCER_CODE.py
```

### 4. View Output
```bash
hdfs dfs -cat /narcotics/output/part-00000
```

---

## 📈 Sample Output

```
Cannabis            2680
Cocaine              905
Delhi               1985
Heroin              1955
Maharashtra         2010
Methamphetamine     1260
Opium               3130
Punjab              2645
Rajasthan           2710
Uttar Pradesh       2275
```

---

## 🤖 Use of Generative AI

Generative AI (ChatGPT) played an important role in this project:

* Code generation (Mapper & Reducer)
* Debugging support
* Hive query assistance
* Concept understanding of Big Data tools

---

## 🔐 Validation

All generated code and outputs were:

* Manually tested
* Verified for correctness
* Successfully executed in the Hadoop environment

---

## 🌟 Key Features

* Scalable Big Data processing
* Efficient handling of large narcotics datasets
* Distributed computing approach
* Dual-key Mapper (drug type + state in one job)
* Integration of AI for enhanced productivity

---

## 🎯 Conclusion

This project successfully demonstrates how the Hadoop ecosystem can be used to process and analyze large-scale narcotics data efficiently.

By combining **HDFS, MapReduce, and Hive**, the system transforms raw seizure data into meaningful insights, enabling better decision-making in law enforcement and policy planning.

---

## 👨‍💻 Author

**Abhishek Ray**  
🏫 Babu Banarasi Das University, Lucknow  

---

## ⭐ Final Note

This project reflects a real-world Big Data solution where distributed computing is essential for handling large-scale law enforcement data efficiently.
