# Employee REST API ETL Pipeline

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python.

The pipeline extracts employee data from a REST API, transforms the JSON data into a structured format using Pandas, and loads the processed data into a PostgreSQL database.

---

## Project Architecture

```text
REST API
    ↓
Extract
    ↓
JSON Data
    ↓
Transform (Pandas)
    ↓
Data Validation
    ↓
Load
    ↓
PostgreSQL
```

---

## Features

- Extract employee data from a REST API
- Process JSON responses
- Transform nested data using Pandas
- Load data into PostgreSQL
- Logging for monitoring pipeline execution
- Exception handling for reliability
- Modular ETL architecture

---

## Tech Stack

- Python
- REST API
- Requests
- Pandas
- PostgreSQL
- SQLAlchemy
- Logging

---

## Project Structure

```text
employee-api-etl/
│
├── main.py
├── extract.py
├── transform.py
├── load.py
├── config.py
├── logger.py
├── requirements.txt
├── README.md
└── logs/
    └── etl.log
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd employee-api-etl
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE employee_db;
```

Update database details in `config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "employee_db",
    "user": "postgres",
    "password": "your_password"
}
```

---

## API Configuration

The project uses the DummyJSON Users API:

```text
https://dummyjson.com/users
```

Update the API URL in `config.py` if needed.

---

## Running the Pipeline

Execute:

```bash
python main.py
```

Successful execution:

```text
ETL Pipeline Completed Successfully
```

---

## Verify Loaded Data

Connect to PostgreSQL and run:

```sql
SELECT * FROM employees;
```

---

## Logging

Pipeline execution logs are stored in:

```text
logs/etl.log
```

Example:

```text
2026-06-14 10:00:01 - INFO - Extraction started
2026-06-14 10:00:02 - INFO - Transformation completed
2026-06-14 10:00:03 - INFO - Load completed
```

---

## ETL Workflow

### Extract

- Connect to REST API
- Retrieve employee data
- Parse JSON response

### Transform

- Flatten nested JSON
- Select required fields
- Rename columns
- Validate data

### Load

- Connect to PostgreSQL
- Insert processed data into employees table

---

## Skills Demonstrated

- REST API Integration
- Python Programming
- JSON Processing
- Pandas Data Transformation
- PostgreSQL Database Management
- SQLAlchemy
- ETL Development
- Logging and Monitoring
- Error Handling

---

## Future Enhancements

- API Authentication
- Incremental Data Loading
- Pagination Support
- Docker Containerization
- Airflow Scheduling
- AWS Deployment
- Data Quality Checks

---
## Repository

GitHub Repository:

https://github.com/mounivelaga/employee-api-etl

## Sample Output

### Employees Table

![Employees Table](screenshots/employees_table.png)


## Author

Mouni Yelisetty

DATA Engineer | Python | SQL | PostgreSQL | REST API 