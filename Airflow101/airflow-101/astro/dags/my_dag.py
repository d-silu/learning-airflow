from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain



default_args = {
    'retries':3,
}

def print_a():
    print("Hi\nFrom task a")
    
def print_b():
    print('Hello\nFrom task b')

def print_c():
    print('Chill')
    
def print_d():
    print("Guess who is here")
    
def print_e():
    print("Welcome D!")

with DAG('my_dag', start_date=datetime(2024,2,11,21,47,00),
         description='A simple tutorial DAG', default_args=default_args,
         tags=['data_science'], schedule='@daily', catchup=False) as dag:
    
    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b)
    task_c = PythonOperator(task_id='task_c', python_callable=print_c)
    task_d = PythonOperator(task_id='task_d', python_callable=print_d)
    task_e = PythonOperator(task_id='task_e', python_callable=print_e)
    
    
    chain(task_a, [task_b,task_c],[task_d, task_e])
    