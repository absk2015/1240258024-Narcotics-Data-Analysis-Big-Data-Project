# 🚨 Narcotics Data Analysis — Big Data Project

![Hadoop](https://img.shields.io/badge/Hadoop-MapReduce-66CCFF?style=for-the-badge&logo=apache&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hive](https://img.shields.io/badge/Apache-Hive-FDEE21?style=for-the-badge&logo=apache&logoColor=black)
![Linux](https://img.shields.io/badge/Linux-Cloudera-FCC624?style=for-the-badge&logo=linux&logoColor=black)

> **Babu Banarasi Das University — Big Data Fundamentals**
> Student ID: `1240258024` | Author: Abhishek Ray

---

## 📌 Problem Statement

Drug trafficking and narcotics abuse are among the most pressing law enforcement challenges in India. Traditional relational databases are ill-equipped to handle the volume, velocity, and variety of large-scale narcotics seizure records collected across multiple states and years.

This project leverages **Apache Hadoop MapReduce** — a distributed big data processing framework — to analyze narcotics crime data across Indian states. The goal is to:

- Identify **which drug types** are most prevalent across the country
- Pinpoint **which states** are highest-risk zones for narcotics activity
- Demonstrate how **big data tools** can uncover patterns that traditional tools cannot efficiently process

---

## 📊 Dataset Description

**File:** `dataset.csv`

The dataset contains narcotics seizure records from Indian states spanning 6 years (2018–2023). It includes 30 records covering 5 states and 5 drug types.

| Column | Type | Description |
|---|---|---|
| `Year` | Integer | Year the narcotics case was registered (2018–2023) |
| `State` | String | Indian state where the case was registered |
| `Drug_Type` | String | Type of narcotic seized (Heroin, Cocaine, Opium, Cannabis, Methamphetamine) |
| `Cases` | Integer | Number of cases registered |
| `Quantity_kg` | Float | Quantity of drug seized in kilograms |
| `Arrests` | Integer | Number of arrests made in connection with the case |

**Coverage:**
- 📅 Years: 2018 – 2023
- 🗺️ States: Delhi, Maharashtra, Punjab, Rajasthan, Uttar Pradesh
- 💊 Drug Types: Cannabis, Cocaine, Heroin, Methamphetamine, Opium
- 📋 Total Records: 30

---

## 📁 Repository Structure

```
📦 1240258024-Narcotics-Data-Analysis-Big-Data-Project
 ┣ 🐍 Mapper.py        — MapReduce Mapper: emits (drug_type, cases) and (state, cases)
 ┣ 🐍 Reducer.py       — MapReduce Reducer: aggregates total cases per key
 ┣ 📊 dataset.csv      — Input narcotics seizure dataset
 ┣ 📄 gg.pdf           — Project report / documentation
 ┗ 📘 README.md        — This file
```

---

## 🚀 Steps to Run

### Prerequisites

Make sure the following are installed and configured:
- Hadoop (2.x or 3.x) with HDFS and YARN
- Python 3.x
- Apache Hive (optional, for querying output)
- Cloudera or equivalent Hadoop distribution

---

### Step 1 — Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
```

Verify services are running:

```bash
jps
```

You should see: `NameNode`, `DataNode`, `ResourceManager`, `NodeManager`.

---

### Step 2 — Upload Dataset to HDFS

```bash
hdfs dfs -mkdir /narcotics
hdfs dfs -put dataset.csv /narcotics/
```

Verify the upload:

```bash
hdfs dfs -ls /narcotics/
```

---

### Step 3 — Run the MapReduce Job

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /narcotics/dataset.csv \
  -output /narcotics/output \
  -mapper Mapper.py \
  -reducer Reducer.py \
  -file Mapper.py \
  -file Reducer.py
```

> ⚠️ Make sure `Mapper.py` and `Reducer.py` are executable:
> ```bash
> chmod +x Mapper.py Reducer.py
> ```

---

### Step 4 — View Output

```bash
hdfs dfs -cat /narcotics/output/part-00000
```

---

### Step 5 — (Optional) Query with Apache Hive

Load the output into Hive for SQL-style analysis:

```sql
CREATE TABLE narcotics_output (category STRING, total_cases INT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';

LOAD DATA INPATH '/narcotics/output/part-00000' INTO TABLE narcotics_output;

SELECT * FROM narcotics_output ORDER BY total_cases DESC;
```

---

## 📈 Sample Output

After the MapReduce job completes, the output will show aggregated case counts by drug type and state:

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

**Key Insights from Output:**
- 🔴 **Opium** is the most prevalent drug type with 3,130 total cases
- 🔴 **Rajasthan** is the highest-risk state with 2,710 cases
- 🟢 **Cocaine** has the fewest cases (905), suggesting lower prevalence

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|---|---|---|
| Apache Hadoop HDFS | 2.x / 3.x | Distributed file storage for large datasets |
| Hadoop MapReduce | 2.x / 3.x | Parallel data processing (Mapper + Reducer) |
| Hadoop Streaming | Built-in | Enables Python scripts as MapReduce jobs |
| Python | 3.x | Implementation of Mapper and Reducer logic |
| Apache Hive | Latest | SQL-style querying on MapReduce output |
| Cloudera | CDH | Hadoop distribution / execution environment |
| Linux | Ubuntu/CentOS | Operating system for running Hadoop cluster |

---

## ⚙️ How MapReduce Works in This Project

```
dataset.csv ──▶ HDFS ──▶ Mapper.py ──▶ Shuffle & Sort ──▶ Reducer.py ──▶ Output ──▶ Hive
```

- **Mapper (`Mapper.py`):** Reads each CSV row and emits two key-value pairs per record:
  - `Drug_Type → Cases`
  - `State → Cases`
- **Shuffle & Sort:** Hadoop automatically groups all values by key
- **Reducer (`Reducer.py`):** Sums up total cases for each drug type and each state
- **Output:** A flat file of `(category, total_cases)` pairs stored back in HDFS

---

*Big Data Fundamentals Project · BBDU Lucknow · 2024*
