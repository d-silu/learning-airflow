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


**Find Bottlenecks in DAG runs**

- The Gantt chart is perfect for identifying task bottlenecks and overlaps.
- A rectangle is a task. The longer the rectangle, the longer it took to complete the task.
- A rectangle is divided into two parts. The first part (grey) is the queued time. The second is the execution time.
- The queued time corresponds to the time spent waiting for a worker to pick your task. A worker executes tasks.
- Two rectangles side by side mean tasks have been executed in parallel and this is an overlap.


**Check DAG Updates**

- The Code view shows the DAG code parsed by the Scheduler.
- The Code view is perfect for checking whether or not DAG updates have been picked up.
- Look at the Parsed at date instead of searching for your modification in the code.
- You can't edit DAG code in the Code view.


**Debugging Tasks**

- A DAG run fails when a task fails in it.
- The first step to debug a task instance is to look into the logs.
- You get different logs for each retry (attempt) to the same task.
- Pause the DAG before fixing the error. Otherwise, your DAG runs will continue to fail.
- Retry multiple DAG Runs and Task instances at once using Browse.

**Browse DAG Runs and Task Instances**

- From "Browse", you can have lists of DAG runs, Task instances, Jobs, and more.
- Use "Browse" to simultaneously take actions on multiple DAG runs or Task instances.
- You can search on specific objects by mixing different filters.
- You can rerun a set of task instances of DAG runs by filtering on the start and end dates. Then select Clear the state.
- "Browse" provides further details on your Task instances or DAG runs, such as, run type, start date, duration, etc.

---

**QnA**

- What's the best view to use to optimize your tasks: _Landing Times View_
- What's the best view to check the historical states of the DAG Runs and Task instances for a given DAG?: _Grid View_
- To Identify bottlenecks in your DAG: _Gantt view_
- What's the best view to spot repetitive patterns over many DAG Runs of a DAG?: _Calender view_
- What does the "Recent Tasks" column on the DAG view show?: _Task's states of the current or latest DAG Run for a given DAG_.

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

- [Code View Airflow](https://airflow.apache.org/docs/apache-airflow/stable/ui.html#code-view)
- [Code View Astronomer](https://docs.astronomer.io/learn/airflow-ui#code)

- [Debug DAGs Airflow](https://academy.astronomer.io/debug-dags)
- [Debug DAGs Astronomer](https://docs.astronomer.io/learn/debugging-dags)

- [Browse DAG Runs and Task Instances](https://docs.astronomer.io/learn/airflow-ui#browse-tab)

- [DAG Scheduling](https://academy.astronomer.io/astro-runtime-scheduling)

- [TaskGroups](https://academy.astronomer.io/astro-runtime-task-groups)