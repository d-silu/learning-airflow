import json
import pathlib
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def _get_pictures():
    # ensure directory exists
    pathlib.Path("/home/ashrulochan/tmp/images").mkdir(parents=True, exist_ok=True)
    
    # Download all pictures in launches.json
    with open('/home/ashrulochan/tmp/launches.json') as f:
        launches = json.load(f)
        img_urls = [launch['image'] for launch in launches['results']]
        for image_url in img_urls:
            try:
                response = requests.get(image_url)
                image_file_name = image_url.split('/')[-1]
                target_file = f"/home/ashrulochan/tmp/images/{image_file_name}"
                with open(target_file, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {target_file}")
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}.")
            


def _fetch_api_data():
    res = requests.get('https://ll.thespacedevs.com/2.0.0/launch/upcoming')
    with open('/home/ashrulochan/tmp/launches.json', 'w') as f:
        data = res.json()
        json.dump(data, f)


# initiating DAG object
dag = DAG(
    # Name of the DAG
    dag_id='download_rocket_launches',
    # Date at which the DAG should first start running
    start_date=airflow.utils.dates.days_ago(14),
    # At what interval the DAG should run
    schedule='@daily'   # airflow alias for 0 0 (i.e. midnight)
)

# download_launches = BashOperator(
#     task_id='download_launches',
#     bash_command="curl -o /tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",
#     dag=dag
# )

download_launches = PythonOperator(
    task_id = 'fetch_api_data',
    python_callable=_fetch_api_data,
    dag=dag
)

get_pictures = PythonOperator(
    task_id = 'get_pictures',
    python_callable=_get_pictures,
    dag=dag
)

notify = BashOperator(
    task_id='notify',
    bash_command='echo "There are now $(ls /tmp/images/ | wc -l) images."',
    dag=dag
)

# set the order of execution of tasks
download_launches >> get_pictures >> notify