<div align="center">

# 🚨 Narcotics Data Analysis
### Big Data Processing using Hadoop MapReduce

![Hadoop](https://img.shields.io/badge/Hadoop-MapReduce-66CCFF?style=for-the-badge&logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hive](https://img.shields.io/badge/Apache-Hive-FDEE21?style=for-the-badge&logo=apache&logoColor=black)
![Linux](https://img.shields.io/badge/Linux-Cloudera-FCC624?style=for-the-badge&logo=linux&logoColor=black)

*Babu Banarasi Das University — Big Data Fundamentals*

</div>

---

## 📌 Problem Statement

Drug trafficking is a major law enforcement challenge in India. Traditional databases cannot efficiently process large-scale narcotics seizure records. This project uses **Hadoop MapReduce** to analyze seizure data across Indian states — identifying the most prevalent drug types and highest-risk regions.

---

## 📂 Repository Structure

```
📦 1240258024-Narcotics-Data-Analysis-Big-Data-Project
 ┣ 📄 Project-Report.pdf
 ┣ 🐍 Mapper.py
 ┣ 🐍 Reducer.py
 ┣ 📊 dataset.csv
 ┗ 📘 README.md
```

---

## 📊 Dataset Description

| Column | Description |
|---|---|
| `Year` | Year of the narcotics case (2018–2023) |
| `State` | Indian state where case was registered |
| `Drug_Type` | Type of narcotic (Heroin, Cocaine, Opium, Cannabis, Methamphetamine) |
| `Cases` | Number of cases registered |
| `Quantity_kg` | Quantity seized in kilograms |
| `Arrests` | Number of arrests made |

> 30 records · 5 states · 5 drug types · 6 years (2018–2023)

---

## ⚙️ How It Works

```
dataset.csv  ──▶  HDFS  ──▶  Mapper.py  ──▶  Reducer.py  ──▶  Hive  ──▶  Insights
```

- **Mapper** reads each CSV row and emits two key-value pairs: `Drug_Type → Cases` and `State → Cases`
- **Reducer** aggregates total cases per key across all rows
- **Hive** enables SQL-style querying on the final output

---

## 🚀 Steps to Run

**1. Start Hadoop**
```bash
start-dfs.sh
start-yarn.sh
```

**2. Upload dataset to HDFS**
```bash
hdfs dfs -mkdir /narcotics
hdfs dfs -put dataset.csv /narcotics/
```

**3. Run MapReduce job**
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /narcotics/dataset.csv \
  -output /narcotics/output \
  -mapper Mapper.py \
  -reducer Reducer.py \
  -file Mapper.py \
  -file Reducer.py
```

**4. View results**
```bash
hdfs dfs -cat /narcotics/output/part-00000
```

---

## 📈 Sample Output

```
Cannabis          2680
Cocaine            905
Delhi             1985
Heroin            1955
Maharashtra       2010
Methamphetamine   1260
Opium             3130
Punjab            2645
Rajasthan         2710
Uttar Pradesh     2275
```

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Hadoop HDFS | Distributed storage |
| MapReduce | Data processing |
| Apache Hive | Query & analysis |
| Python 3 | Mapper & Reducer scripts |
| Cloudera | Hadoop distribution |
| Linux | Execution environment |

---

<div align="center">

**Abhishek Ray** · `1240258024` · Big Data Fundamentals · BBDU Lucknow

</div>
