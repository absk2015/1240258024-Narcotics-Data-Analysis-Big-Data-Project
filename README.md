# 📊 Narcotics Data Analysis using Hadoop Big Data Project

![Hadoop](https://img.shields.io/badge/Big%20Data-Hadoop-yellow)
![Python](https://img.shields.io/badge/Language-Python-blue)
![Hive](https://img.shields.io/badge/Query-Hive-orange)
![Status](https://img.shields.io/badge/Project-Academic-success)

---

## 📌 Overview

This project analyzes narcotics crime data using the Hadoop MapReduce framework. It processes large-scale datasets to extract meaningful insights such as total cases by drug type and state.

The system uses HDFS for storage and MapReduce for distributed data processing.

---

## 🎯 Objectives

* Analyze narcotics-related crime data
* Identify drug-wise and state-wise trends
* Perform distributed data processing using Hadoop
* Generate aggregated insights from raw data

---

## 📁 Dataset

The dataset contains records of narcotics-related cases with the following attributes:

* Year
* State
* Drug Type
* Number of Cases
* Quantity Seized (kg)
* Number of Arrests

The dataset is stored in CSV format and uploaded to HDFS for processing.

---

## 🏗️ Project Architecture

The project is based on the Hadoop ecosystem:

* **HDFS** – Storage layer
* **MapReduce** – Data processing layer
* **Hive** – Query and analysis layer

---

## 🔄 Data Flow

Raw Data → HDFS → Mapper → Reducer → Output → Hive Analysis

---

## ⚙️ Implementation

### 🧩 Mapper

* Reads input data
* Emits key-value pairs such as:

  * (Drug Type, Cases)
  * (State, Cases)

### 🔗 Reducer

* Receives grouped data from mapper
* Aggregates values to compute totals

---

## 🛠️ Technologies Used

* Hadoop (HDFS, MapReduce)
* Hive
* Python
* Linux

---

## 🚀 Steps to Execute

```bash
# Start Hadoop services
start-dfs.sh
start-yarn.sh

# Upload dataset to HDFS
hdfs dfs -put dataset.csv /input

# Run MapReduce job
hadoop jar your-job.jar Mapper Reducer /input /output

# View output
hdfs dfs -cat /output/part-00000
```

---

## 📈 Sample Output

**Drug-wise Results:**
Cannabis 2680
Cocaine 905
Heroin 1230

**State-wise Results:**
Uttar Pradesh 2100
Maharashtra 1850

---

## 🧠 Hive Queries

```sql
SELECT drug_type, SUM(cases)
FROM narcotics
GROUP BY drug_type;

SELECT state, SUM(cases)
FROM narcotics
GROUP BY state;
```

---

## 📂 Project Structure

```bash
├── Project-Report.pdf
├── Mapper.py
├── Reducer.py
├── dataset.csv
├── README.md
```

---

## 🚀 Future Improvements

* Add real-time data processing using Spark
* Build visualization dashboards
* Integrate machine learning for prediction

---

## 👨‍💻 Author

Abhishek Ray  

---

## ✅ Conclusion

This project demonstrates how Hadoop MapReduce can be used for large-scale data analysis. It efficiently processes narcotics data and generates useful insights using distributed computing.

---

## ⚠️ Note

This project is developed for academic purposes. Understanding the Mapper and Reducer logic is essential, as it may be evaluated during viva.
