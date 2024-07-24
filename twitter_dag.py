from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'Zain',
    'depends_on_past': False,
    'start_date': datetime(2001, 10, 7),
    'email': 'zaineel.s.mithani@gmail.com',
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'Twitter_dag',
    default_args=default_args, 
    description='My First ETL code')

run_elt = PythonOperator(
    task_id = 'complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)

run_elt
