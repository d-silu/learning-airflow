from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator



with DAG('check_dag',start_date=datetime(2024,2,12),
         description='DAG to check data', tags=['data_engineering'],
         schedule='@daily', catchup=False):
    
    create_file = BashOperator(
        task_id='create_file',
        bash_command='echo "Hi there!" > ~/Downloads/learning-airflow/Airflow101/airflow-101/tmp/dummy.txt'
    )
    
    check_file_exists = BashOperator(
        task_id = 'check_file_exists',
        bash_command = 'test -f ~/Downloads/learning-airflow/Airflow101/airflow-101/tmp/dummy.txt'
    )
    
    read_file = PythonOperator(
        task_id = 'read_file',
        python_callable=lambda: print(open('~/Downloads/learning-airflow/Airflow101/airflow-101/tmp/dummy.txt', 'rb').read())
    )
    
    create_file >> check_file_exists >> read_file