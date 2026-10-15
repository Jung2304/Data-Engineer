# Data Engineering Learning Journey 

A hands-on collection of **notebooks, SQL scripts, Python exercises, and mini-projects** documenting my journey in Data Engineering — from Python and SQL fundamentals to distributed data processing, cloud data warehousing, Databricks Lakehouse engineering, and analytics engineering with dbt.

The goal of this repository is to **learn by building**: understand the underlying concepts, implement them in code, and gradually connect them to real-world data engineering patterns.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
  <img alt="SQL" src="https://img.shields.io/badge/SQL-336791?logo=postgresql&logoColor=white" />
  <img alt="Apache Spark" src="https://img.shields.io/badge/Apache_Spark-E25A1C?logo=apachespark&logoColor=white" />
  <img alt="Azure" src="https://img.shields.io/badge/Microsoft_Azure-0078D4?logo=microsoftazure&logoColor=white" />
  <img alt="Databricks" src="https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white" />
  <img alt="Delta Lake" src="https://img.shields.io/badge/Delta_Lake-0A84FF?logo=delta&logoColor=white" />
  <img alt="dbt" src="https://img.shields.io/badge/dbt-FF694B?logo=dbt&logoColor=white" />
  <img alt="Apache Airflow" src="https://img.shields.io/badge/Apache_Airflow-017CEE?logo=apacheairflow&logoColor=white" />
</p>

> **About this repository:** These are learning materials and hands-on implementations. Some exercises require an Azure/Databricks workspace, sample datasets, or environment-specific configuration.

## Learning Roadmap

```text
Python & SQL Fundamentals
           ↓
Data Modeling & Dimensional Warehousing
           ↓
Apache Spark, PySpark & Workflow Orchestration
           ↓
Azure Synapse Analytics & Cloud Warehousing
           ↓
Databricks, Delta Lake & Lakeflow Pipelines
           ↓
dbt & Analytics Engineering
```

## Modules 

| Module | Focus | Main concepts |
|---|---|---|
| [**Module 1**](./Module1/) | Python & SQL Fundamentals | Python, OOP, testing, joins, CTEs, window functions |
| [**Module 2**](./Module2/) | Data Modeling & Warehousing | Medallion Architecture, dimensional models, SCD Type 1 & 2 |
| [**Module 3**](./Module3/) | Apache Spark, PySpark & Airflow | Spark internals, distributed transformations, streaming, orchestration |
| [**Module 5**](./Module5/) | Azure Synapse Analytics | Serverless/dedicated SQL pools, external tables, CETAS, data distribution |
| [**Module 6**](./Module6/) | Databricks & Delta Lake | Unity Catalog, Auto Loader, Delta Lake, Lakeflow DLT, Asset Bundles |
| [**Module 8**](./Module8/) | dbt & Analytics Engineering | SQL models, `ref()`/`source()`, tests, Jinja, macros, snapshots |

---

## Module 1 — Python & SQL Fundamentals

**Objective:** Build a foundation in programming, relational databases, and analytical SQL.

**Python** — [`Module1/Python`](./Module1/Python/)
- Core Python syntax, functions, collections, and control flow.
- Object-oriented programming, decorators, asynchronous programming, and multithreading.
- API requests, Pydantic validation, and testing with `pytest`.
- Small practice programs such as a calculator, timer, and input validator.

**MySQL** — [`Module1/MySQL`](./Module1/MySQL/)
- DDL/DML operations, constraints, filtering, and aggregation.
- Joins, subqueries, and common table expressions (CTEs).
- Window functions, ranking, running totals, and practical SQL problem-solving.

**Key takeaway:** Writing maintainable Python code and using SQL to retrieve, transform, and analyze structured data.

## Module 2 — Data Modeling & Warehousing

**Objective:** Understand how raw transactional data becomes structured, analytics-ready data.

- **Bronze:** Explore source ingestion and incremental-load logic based on a date watermark.
- **Silver:** Clean and enrich records, then practice incremental upserts with Delta `MERGE`.
- **Gold:** Build customer, product, and other dimension tables and a sales fact table using surrogate keys.
- **Slowly Changing Dimensions:** Implement **SCD Type 1** for overwriting values and **SCD Type 2** for retaining change history.

**Explore the notebooks:**
- [Medallion Architecture: Source → Bronze → Silver → Gold](./Module2/Data_Modeling_Databricks/Medallion_Architecture/)
- [Slowly Changing Dimensions](./Module2/Data_Modeling_Databricks/SCDs/)

**Key takeaway:** Dimensional modeling, incremental transformations, and historical change tracking in a Lakehouse-style warehouse.

## Module 3 — Apache Spark, PySpark & Apache Airflow

**Objective:** Process data at scale and understand how to orchestrate processing tasks.

### Apache Spark Internals
[`Apache_Spark`](./Module3/Apache_Spark/)

- Jobs, stages, tasks, and lazy evaluation.
- Narrow and wide transformations, caching, and partition pruning.
- Join strategies, including broadcast and sort-merge joins.

### PySpark Data Engineering
[`PySpark`](./Module3/PySpark/)

- DataFrame reading/writing, explicit schemas, and Parquet.
- Column transformations, missing-value handling, aggregations, and joins.
- Window functions, UDFs, arrays, `explode`, and Spark SQL.

### Practical ETL Scenarios
[`PySpark_Real_Scenarios`](./Module3/PySpark_Real_Scenarios/)

- Latest-record deduplication and Delta Lake upserts.
- Incremental file processing with Structured Streaming and checkpoints.
- Parsing and flattening nested JSON records.
- Reusable data validation logic and an SCD Type 2 exercise.

### Apache Airflow & Docker
[`airflow-demo`](./Module3/airflow-demo/)

- Set up an Airflow environment with Docker Compose.
- Explore DAG definitions, task dependencies, and scheduled workflow execution.
- Implement a small three-task workflow using Airflow TaskFlow decorators.

**Key takeaway:** Spark execution fundamentals, reusable PySpark transformations, streaming patterns, and workflow orchestration.

## Module 5 — Azure Synapse Analytics

**Objective:** Explore cloud data warehousing and different ways to query and store data in Azure.

**Serverless SQL Pool** — [`severless_pool`](./Module5/Azure_Synapse_Analytics/severless_pool/)
- Query files in Azure Data Lake Storage Gen2 with `OPENROWSET`.
- Define external data sources and external tables.
- Export query results using **CETAS** (Create External Table As Select).

**Dedicated SQL Pool** — [`dedicated_sql_pool`](./Module5/Azure_Synapse_Analytics/dedicated_sql_pool/)
- Load data using `COPY INTO` and explore PolyBase/CTAS patterns.
- Compare internal and external tables and distributed query execution.

**Distribution Strategies** — [`3_types_of_distribution`](./Module5/Azure_Synapse_Analytics/3_types_of_distribution/)
- **HASH:** Partition records by a distribution key.
- **ROUND_ROBIN:** Spread records without a key-based distribution strategy.
- **REPLICATE:** Copy smaller tables across compute nodes to reduce data movement.

**Key takeaway:** Choosing between querying data directly in the lake and loading it into a distributed cloud data warehouse.

## Module 6 — Databricks, Delta Lake & Lakeflow

**Objective:** Develop practical Lakehouse engineering skills, from ingestion and storage management to incremental pipelines and deployment.

### Databricks Fundamentals
[`Databricks Fundamentals`](./Module6/Databricks%20Fundamentals/)

- Work with `dbutils.fs`, widgets, notebook execution, and secrets.
- Explore Azure storage access with a service principal versus managed identity and Unity Catalog.
- Use **Auto Loader** for incremental ingestion, schema tracking, and checkpointing.
- Build a basic multi-step Databricks Job: generate → transform → validate.

### Delta Lake Deep Dive
[`Delta Lake`](./Module6/Delta%20Lake/)

| Area | Topics explored |
|---|---|
| Delta tables | SQL API, Delta API, generated/identity columns |
| Transaction log | Delta writes, reads, and `_delta_log` concepts |
| Schemas | Enforcement, evolution, and schema overwrite |
| Data changes | DML, `MERGE` upserts, and Change Data Feed (CDF) |
| Table maintenance | `DESCRIBE`, cloning, `RESTORE`, `VACUUM`, table properties |
| Interoperability | Delta UniForm concepts |
| Performance | `OPTIMIZE`, ZORDER, and liquid clustering |

### Lakeflow Declarative Pipelines (DLT)
[`Lakeflow Declarative Pipelines`](./Module6/Lakeflow%20Declarative%20Pipelines%20-%20DLT/)

Practice a **Bronze → Silver → Gold** sales pipeline using declarative Python definitions:

```text
Bronze                       Silver                      Gold
------                       ------                      ----
Customers  ───────────────►  Customer transformations ─► Customer dimension
Products   ───────────────►  Product transformations  ─► Product dimension
Sales E/W  ─► Append Flow ─► Sales transformations    ─► Sales fact
                                                          │
                                                          ▼
                                                  Business sales view
```

- Declare streaming tables and materialized views with `pyspark.pipelines` (`dp`).
- Enforce data quality using expectations.
- Combine East/West sales streams with Append Flows.
- Explore **Auto CDC**, SCD Type 1, and SCD Type 2.
- Create a business-facing sales aggregation by region and product category.

### Databricks Jobs & Asset Bundles
- [`Jobs and Workflows`](./Module6/Jobs%20and%20Workflows/) — practice parameter passing and workflow-driven ingestion.
- [`Databricks Asset Bundle tutorial`](./Module6/Databricks%20Asset%20Bundle/Asset_Bundles/dab_tutorial/) — configure Databricks resources using YAML and explore development/production deployment targets.

**Key takeaway:** Building blocks for incremental and governed Lakehouse pipelines, including Delta table management, declarative ETL, CDC, and deployment-as-code.

## Module 8 — dbt & Analytics Engineering

**Objective:** Build modular, testable SQL transformations and manage analytical data models with dbt Core and Databricks.

**Main project:** [`jung_dbt`](./Module8/DBT%20-%20Data%20Build%20Tool/jung_dbt/)

- **Bronze models:** Source-backed models for sales, customers, products, stores, dates, and returns.
- **Silver models:** Join related datasets and calculate sales and return metrics.
- **Gold exercise:** Prepare item records for history tracking.
- **Model dependencies:** Use `source()` and `ref()` to connect datasets and downstream models.
- **Data testing:** Built-in `unique`, `not_null`, `accepted_values` tests, plus custom generic and singular tests.
- **Jinja & macros:** Reuse SQL expressions and customize schema naming.
- **Snapshots & seeds:** Explore timestamp-based snapshots and CSV reference data.
- **Environments:** Configure development and production targets for Databricks.

**Key takeaway:** Applying analytics engineering practices to make SQL transformations modular, reusable, traceable, and testable.

---

## Technologies & Skills

| Category | Technologies / Concepts |
|---|---|
| Programming | Python, SQL, PySpark |
| Distributed processing | Apache Spark, Spark SQL, Structured Streaming |
| Storage & modeling | Delta Lake, Parquet, Medallion Architecture, Star Schema, SCD |
| Cloud platforms | Microsoft Azure, ADLS Gen2, Azure Synapse Analytics, Azure Databricks |
| Governance & ingestion | Unity Catalog, Auto Loader, Change Data Feed, Auto CDC |
| Orchestration & deployment | Apache Airflow, Docker, Databricks Jobs, Databricks Asset Bundles |
| Analytics engineering | dbt Core, Jinja, macros, tests, seeds, snapshots |
| Version control | Git, GitHub |

## Repository Structure

```text
Data-Engineer/
├── Module1/           # Python & MySQL fundamentals
├── Module2/           # Data modeling, Medallion Architecture, SCDs
├── Module3/           # Apache Spark, PySpark, Airflow & Docker
├── Module5/           # Azure Synapse Analytics
├── Module6/           # Databricks, Delta Lake, Lakeflow & Asset Bundles
├── Module8/           # dbt Core & analytics engineering
└── README.md
```

---

### 🎯 Learning Goal

To become a Data Engineer capable of designing **reliable, scalable, and maintainable data pipelines** — from ingestion and transformation to data modeling, quality assurance, orchestration, and deployment.

*Continuously learning, experimenting, and improving through hands-on implementation.*
