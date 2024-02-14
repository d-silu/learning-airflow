## Chapter 1 : Meet Apache Airflow

---------

- Airflow is not a data processing tool in itself but orchestrates the different components responsible for processing the data in data pipelines.

- In the graph-based representation of data pipelines, tasks are represented as nodes in the graph, while dependencies between tasks are represented by directed edges between the task nodes.

- The direction of the edge indicates the direction of the dependency.

- This type of graph is generally called a _directed graph_ due to the directions in the graph edges.

- Directed Acyclic Graph (DAG) does not contain any loops or cycles. This is called acyclic property and it prevents from running into circular dependencies between tasks.

- Airflow is developed by Airbnb.

- Airflow is written in python, workflows defined in Python, supports scheduling, backfilling, has a vibrant functional user interface, and can be installed anywhere. 

- Airflow is horizontally scalable.

**Components of Airflow**

1. **Scheduler** - Parses DAGs, checks their schedule interval and starts scheduling the DAG's tasks for execution by passing them to the Airflow workers.

2. **Workers** - Pick up tasks that are scheduled for execution and execute them. The workers are responsible for actually “doing the work.”

3. **Webserver** - Visualizes the DAGs parsed by the scheduler and provides the main interface for users to monitor DAG runs and their results.

- Airflow’s scheduling semantics is that the schedule intervals
not only trigger DAGs at specific time points (similar to, for example, Cron), but also provide details about the last and (expected) next schedule intervals.


**When to Choose Airflow**

- The ability to implement pipelines using Python code allows you to create arbitrarily complex pipelines using anything you can dream up in Python.
- The Python foundation of Airflow makes it easy to extend and add integrations with many different systems. In fact, the Airflow community has already developed a rich collection of extensions that allow Airflow to integrate with many different types of databases, cloud services, and so on.
- Rich scheduling semantics allow you to run your pipelines at regular intervals and build efficient pipelines that use incremental processing to avoid expensive recomputation of existing results.
- Features such as backfilling enable you to easily (re)process historical data, allowing you to recompute any derived data sets after making changes to your code.
- Airflow’s rich web interface provides an easy view for monitoring the results of your pipeline runs and debugging any failures that may have occurred.


**When not to Choose Airflow**

- For streaming pipelines, as airflow is primarily designed to run recurring or batch-oriented tasks, rather than streaming workloads.

- Implementing highly dynamic pipelines, in which tasks are added/removed between every pipeline run.

- Airflow does not maintain data lineage, data versioning, etc.