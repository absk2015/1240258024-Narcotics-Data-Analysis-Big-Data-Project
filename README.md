# Narcotics Data Analysis using Hadoop Big Data Project

## 📌 Problem Statement

The objective of this project is to analyze narcotics-related crime data across different states and drug types using Hadoop MapReduce. The goal is to identify patterns, high-risk regions, and frequently occurring drug cases.

---

## 📊 Dataset Description

The dataset contains narcotics crime records with the following attributes:

* Year
* State
* Drug Type
* Number of Cases
* Quantity Seized (kg)
* Number of Arrests

The dataset is provided in CSV format and is processed using Hadoop.

---

## ⚙️ Technologies Used

* Hadoop (HDFS, MapReduce)
* Hive
* Python
* Linux

---

## 🚀 Steps to Run

1. Start Hadoop services
2. Upload dataset to HDFS
3. Run Mapper script
4. Run Reducer script
5. Retrieve output from HDFS

---

## 📈 Sample Output

Drug-wise aggregation:
Cannabis 2680
Cocaine 905
Heroin 1230

State-wise aggregation:
Uttar Pradesh 2100
Maharashtra 1850

---

## 🧠 Hive Queries (For Analysis)

```sql
SELECT drug_type, SUM(cases)
FROM narcotics
GROUP BY drug_type;

SELECT state, SUM(cases)
FROM narcotics
GROUP BY state;
```

---

## 📁 Project Structure

```
├── Project-Report.pdf
├── Mapper.py
├── Reducer.py
├── dataset.csv
├── README.md
```

---

## ✅ Key Features

* Distributed data processing using Hadoop
* Drug-wise and state-wise aggregation
* Scalable and efficient analysis of large datasets

---

## ⚠️ Note

This project is developed for academic purposes. The implementation is based on Hadoop MapReduce and requires understanding of the underlying logic for proper execution and evaluation.
