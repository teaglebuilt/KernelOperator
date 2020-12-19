from airflow.models import DAG
from airflow.utils.dates import days_ago
from src.operators import KernelOperator


default_arguments = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

with DAG(
    'testing',
    schedule_interval='@daily',
    catchup=False,
    default_args=default_arguments,
) as dag:
    hello_task = KernelOperator(task_id='task_id_1', dag=dag, name='{{ task_instance.task_id }}')