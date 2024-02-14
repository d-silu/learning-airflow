import datetime as dt 
from pathlib import Path 
import pandas as pd 
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id = '01_unscheduled',
    start_date = dt.datetime(2024,2,14),
    schedule_interval="@daily",
    end_date=dt.datetime(year=2024,month=3,day=1)
)

fetch_events = BashOperator(
    task_id ="fetch_events",
    bash_command=(
        "mkdir -p /data && "
        "curl -o /data/events.json "
        "https://localhost:5000/events"
    ),
    dag=dag,
)

def _calculate_status(input_path, output_path):
    """Calculates even statistics."""
    events = pd.read_json(input_path)
    stats = events.groupby(['date','user']).size().reset_index()
    Path(output_path).parent.mkdir(exist_ok=True)
    stats.to_csv(output_path, index=False)
    

calculate_status = PythonOperator(
    task_id = "calculate_status",
    python_callable=_calculate_status,
    op_kwargs={
        "input_path": "/data/events.json",
        "output_path": "/data/stats.csv"
    },
    dag=dag,
)

fetch_events >> calculate_status