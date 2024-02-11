- Use tags to categorize or organize your data pipelines.
- "Runs" shows the status of the past and most recent DAG runs. Whereas "Recent Tasks" shows only the status of the task instances for the active or most recent DAG runs.
- "Last run" is the data interval start of the last DAG run
- "Next run" is the data interval start of the next DAG run
- The "Delete DAG" button doesn't delete the DAG file, only the metadata related to the DAG.
- Don't forget to remove any applied filters or you may wonder why a DAG doesn't show up on the UI. It's an easy mistake.

**Monitor DAG RUns and Task Instances**

- The grid view shows previous and current DAG runs with their task instances and states.
- The top bars are the DAG runs. The squares are the task instances.
The longer a top bar is, the longer it took to complete that specific DAG run.
- You get a DAG runs summary when you land on the Grid view. Mean run duration helps define the DAG's timeout.
- Share information with the rest of your team using notes. That applies to DAG runs and task instances.
- Clear restarts the selected DAG run or task instance.
- When you want to clear a task instance, not including Downstream means downstream tasks to the selected task won't be rerun.
- Use `Shift+ /` to see some shortcuts.

__Task Dependencies__

- The Graph view is perfect for checking dependencies between tasks of a DAG.
- A rectangle is a task with information such as the operator and the state.
- Use the mini-map for navigating a large data pipeline with many tasks.

**Detecting Trends and Patterns**

- The Calendar view overviews your entire DAG's history over months or even years.
- The Calendar view is perfect to spot breaking patterns or trends.
- A square is a day, and the color of that square depends on the ratio between successful and failed DAG runs.
- Squares with dots indicate that DAG runs are planned for these days.


**Optimize Tasks**

- Landing times are calculated from the task scheduled time to the time the task finishes (end_time - scheduled_time)
- Landing times correspond to the actual execution time of your tasks.
- Task durations (the other view) show the total task durations (scheduled time included)
- This view is perfect for evaluating the effectiveness of your changes.


**FInd Bottlenecks in DAG runs**

- The Gantt chart is perfect for identifying task bottlenecks and overlaps.
- A rectangle is a task. The longer the rectangle, the longer it took to complete the task.
- A rectangle is divided into two parts. The first part (grey) is the queued time. The second is the execution time.
- The queued time corresponds to the time spent waiting for a worker to pick your task. A worker executes tasks.
- Two rectangles side by side mean tasks have been executed in parallel and this is an overlap.


----

##### Reference

- [DAGs](https://docs.astronomer.io/learn/airflow-ui#dags)

- [DAGs Grid View apache-airflow document](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#grid-view)
- [DAGs Grid View Astronomer Document](https://docs.astronomer.io/learn/airflow-ui#grid-view)

- [Graph View-Astronomer](https://docs.astronomer.io/learn/airflow-ui#graph)
- [Graph View-Apache-airflow Document](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#graph-view)

- [Calender View](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#calendar-view)

- [Landing time](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#landing-times)

- [Task Instances](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#task-instances)

- [Gantt Chart](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#gantt-chart)