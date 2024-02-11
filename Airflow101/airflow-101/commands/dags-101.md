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