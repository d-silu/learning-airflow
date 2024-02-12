**What's DAG?**

- In Airflow, a DAG is a data pipeline defined in Python code.

- Each DAG represents a collection of tasks you want to run and is organized to show relationships between tasks in the Airflow UI.

- Mathematical properties of DAGs:

    - Directed: If multiple tasks exist, each must have at least one defined upstream or downstream task.

    - Acyclic: Tasks cannot have a dependency on themselves. This avoids infinite loops.

    - Graph: All tasks can be visualized in a graph structure, with relationships between tasks defined by nodes and vertices.

- Airflow offers two ways of defining the DAGs and Tasks:

    - The traditional paradigm.

    - The TaskFlow API

- By default, the number of retries for a task before failing is set to 0.


- A DAG must have a unique identifier and a start_date with a datetime object.
- The schedule interval is optional and defines the trigger frequency of the DAG.
- Defining a description, the catchup parameter to avoid running past non-triggered DAG runs, and tags to filter is strongly recommended.
- To create a task, look at the https://registry.astronomer.io/ first.
- A task must have a unique identifier within a DAG.
- You can specify default parameters to all tasks with default_args that expects a dictionary
- Define dependencies with bitshift operators (>> and <<) as well as lists.
- chain helps to define dependencies between task lists.


**Quiz**

1. What's the role of the start date? - _Define when the DAG starts being scheduled._

2. What happens if you don't define a start date? - _That raises an error_

3. What's the role of tags?

    - They allow to better organizing DAGs.
    - They allow filtering DAGs.

4. How can you avoid assigning the dag object to every task you create?

    - `with DAG(...)`

    - `@dag(...)`

5. What happens when two DAG share the same DAG id? - _One DAG randomly shows up on the UI._