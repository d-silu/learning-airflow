### Aiflow Introduction

-----

- Apache Airflow is an open source platform to programmatically author, schedule and monitor workflows.


- Airflow is an orchestrator.

**Benefits of Airflow**
- Extensible
- Dynamic (Supports Python)
- Scalable
- UI

**Core Components of Airflow**

1. **Web server**: Allows the user to access web UI.
2. **Scheduler**: Schedules data pipelines. Production environment should have at least 2 schedulers running.
3. **Metastore**: A database where metadata info will be stored.
4. **Triggerer**: Allows dealing with special kind of tasks.
5. **Executor**: Defines how and which system will execute the task.
6. **Queue**: Allows tasks to execute on order.
7. **Worker**: Executes the task.

**Aiflow Core Concepts**

- DAG: Direct Acyclic Graph.
    - It should not be cyclic
- Operators
    - An object that encapsulate actions.
    - Three types: 
        - **Action Operators**: To execute an action.
        - **Transfer Operators**: Transfers data from source to destination.
        - **Sensor Operators**: Waits for something to happen and it triggers another action.
    - Task Instance:
        - An instance of the task at a given time.
        - When an operator runs, it becomes a task instances.
    
    - Workflow: Combination of all becomes an workflow.


- Airflow is truly Modular: Any providers can be attached to it to get additional functionality. 

- Airflow is neither a data streaming solution nor a data processing framework.

Airflow can

- ETL/ELT batch pipelines
- Machine Learning model training.
- Automated generation of reports.
- Automatically organize, execute and monitor data flow.

**How Airflow Works in a Node**

1. When a dag (a .py) file is added to the DAGs Folder, the scheduler parses it.
2. The parsing takes approximately 5 minutes before the .py file appears as a DAG.
3. The Scheduler then creates a DagRun object and stores into the metastore DB. DagRun is an instance of a DAG.
4. The scheduler creates a TaskInstance object.
5. Scheduler sends the TaskInstance to Que for execution.
6. The Executor sends the task to worker for execution.
7. Scheduler checks the status of the DagRun object.
8. The Executor updates the DagRun periodically.
9. Finally the status of the DAG is shown over the web server.


----

#### SUMMARY

1. We have learnt that Airflow is an open-source tool that allows users to author, schedule, and monitor workflows in data pipelines.
2. It is coded in Python and is scalable with a user-friendly interface.
3. We explored the several core components, including the web server, scheduler, meta database, triggerer, executor, queue, and worker.
4. We also learnt about the Directed Acyclic Graph (DAG), which is the most crucial concept, and it represents a data pipeline with nodes as tasks and directed edges as dependencies.
5. Moreover, the Operators are objects that encapsulate tasks, and there are three types of operators: action, transfer, and sensor operators. Providers are packages that contain operators for interacting with specific tools.
6. Airflow works by triggering data pipelines through the scheduler, which creates a DAGRun object and a task instance object for the first task. The task instance is then pushed into a queue and executed by the executor.
7. To create a DAG in Airflow, create a file in the "dags/" folder, instantiate the DAG object with parameters such as the unique DAG ID, start date, scheduling interval, and catchup parameter. Once these parameters are defined, tasks can be implemented within the DAG.
8. To create a task, look up the appropriate operator in the registry.astronomer.io and define the task ID and parameters needed for the operator.
9. Airflow is useful for scheduling batch jobs, training machine learning models, and building ETL or ELT pipelines. It saves time by better scheduling and monitoring data pipelines. However, it is not a data streaming solution or a data processing framework, but an orchestrator for batch processing jobs.
10. We also learnt how to define dependencies in Airflow is simple using the right and left bitshift operators, which can be seen in the Airflow UI. Dependencies can be defined between tasks, such as "start >> end" meaning "end" is executed after "start".

--- 

#### Reference

- [Scheduling](https://academy.astronomer.io/astro-runtime-scheduling)