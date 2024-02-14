**CRON expressoins**

    - None : Don’t schedule, use for exclusively “externally triggered” DAGs
    - @once : Schedule once and only once
    - @hourly : Run once an hour at the end of the hour
    - @daily : Run once a day at midnight (24:00)
    - @weekly : Run once a week at midnight (24:00) on Sunday
    - @monthly : Run once a month at midnight (24:00) of the first day of the month
    - @quarterly : Run once a quarter at midnight (24:00) on the first day
    - @yearly : Run once a year at midnight (24:00) of January 1


**Best Practices**


- Passing datetime in UTC is a recommended practice even if you are running Airflow in a single time zone. The rationale behind this is that several countries observe Daylight Saving Time (DST), wherein clocks are adjusted forward in spring and backward in autumn. If you store data in local time, you may encounter errors twice a year during these transitions.


--

**Summary**
- We learnt about the states of a DAGRun which initially is Queued, and changes to Running as soon as the first task runs. Once all tasks are completed, the final state of the DAGRun is determined by the state of the leaf tasks, which could be Success or Failure.
- The start date and scheduling interval are two important parameters to consider when scheduling a DAG. DAGRuns are created based on these parameters and have a data interval start and end corresponding to the time frame for which the DAG was executed.
- The start date parameter defines the timestamp from which the scheduler will attempt to backfill, and the scheduling interval determines how often a DAG runs.
- The catchup mechanism in Airflow allows running all non-triggered DAGRuns between the start date and the last time the DAG was triggered. The backfilling mechanism allows running historical DAGRuns or rerun already existing DAGRuns.
- We also explored the Airflow CLI commands to backfill our DAG for any data intervals, regardless of the start date of our data pipeline.
- Users can define the scheduling interval using CRON expressions or timedelta object, and can use a timetable to schedule a DAG more precisely.
- It is important to set the start date parameter properly to avoid confusion with Airflow, and use a static date.



-- 
**Reference**

- [Crontab](https://crontab.guru/)