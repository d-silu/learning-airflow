## Chapter 2: Anatomy of An Airflow DAG

---------------

- A large job can split into individual tasks in Airflow.

- Multiple tasks can be run in parallel, and tasks can run different technologies.

- To install airflow in linux: 

    1. run `pip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt`
    2. `airflow db init`
    3. Go to `~/airflow` and create a `dags` directory there.
    4. move your dags file to the `~/airflow/dags/` directory. 
    5. `airflow webserver`
    6. `airflow scheduler` in a new terminal tab

- In Airflow, we can use the binary right shift operator (i.e., “rshift” [>>]) to define depen-
dencies between tasks.


- **Operators**: Operators have a single piece of responsibility.

- Role of DAG is to orchestrate the execution of a collection of operators.

- Tasks in Airflow manage the execution of an operator.

- User focuses on the work to be done by using operators, while Airflow ensures correct execution of the work via tasks.

- Workflows in Airflow are represented in DAGs.
- Operators represent a single unit of work.
- Airflow contains an array of operators both for generic and specific types of work.
- The Airflow UI offers a graph view for viewing the DAG structure and tree view for viewing DAG runs over time.
- Failed tasks can be restarted anywhere in the DAG.

**`schedule_interval`**

- If a DAG has start date as January first of 2024 (01-01-2024), and the schedule_interval is set to `@daily`, then the DAG will first executed on second of January. 

- Because the DAG starts executing on midnight.


- Without an `end_date`, Airflow will keep executing the DAG until the end of time.


**Cron-based intervals**

- Cron syntax has 5 components.


```
_____ minute (0 - 59)
| ______ hour (0 - 23)
| | ______ day of the month (1 - 31)
| | | _______ month (1 - 12)
| | | | _______ day of the week (0 - 6) (sun to sat)
| | | | |
| | | | |
* * * * *
```

- Hourly = `0 * * * *`
- Daily = `0 0 * * *`
- Weekly = `0 0 * * 0`
- Midnight on the first of every month = `0 0 1 * *`
- 23:45 every saturday = `45 23 * * SAT`
- every monday, wednesday, friday at midnight = `0 0 * * MON, WED, FRI`
- Every weekday at midnight = `0 0 * * MON-FRI`
- Every day at 00:00 and 12:00 = `0 0,12 * * *`

**Airflow presents for frequently used scheduling intervals**

| Preset | Meaning |
|--------|---------|
| `@once` | Scheduled once and only once.|
| `@hourly` | Run once an hour at the beginning of the hour.|
| `@daily` | Run once a day at midnight.|
| `@weekly` | Run once  a week at midnight on Sunday morning.|
| `@monthly` | Run once a month at midnight on the first day of the month|
| `@yearly` | Run once a year at midnight on January 1.|


- Use [crontab](https://crontab.guru) translator to understand cron syntax.

- _Limitation_: An important limitation of cron expressions is that they are unable to represent certain frequency-based schedules.