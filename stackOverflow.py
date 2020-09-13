from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'owner',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['owner@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('stackOverflow', default_args=default_args)

# t1, t2, t3 and t4 are examples of tasks created using operators

t1 = BashOperator(
    task_id='set_conf_variable',
    bash_command='echo "Task 1"',
    dag=dag)

t2 = BashOperator(
    task_id='create_conf_file',
    bash_command='echo "Task 2"',
    dag=dag)

t3 = BashOperator(
    task_id='check_running_stat_job',
    bash_command='echo "Task 3"',
    dag=dag)
	
t4 = BashOperator(
    task_id='spark_etl',
    bash_command='exit 123"',
    dag=dag)
	
t5 = BashOperator(
    task_id='update_orc_file_variable',
    bash_command='echo "Task 5"',
    dag=dag)
	
t6 = BashOperator(
    task_id='remove_conf_file',
    bash_command='echo "Task 6"',
    dag=dag,
	trigger_rule='all_done')

t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)
t6.set_upstream(t2)
t6.set_upstream(t3)
t6.set_upstream(t4)
t6.set_upstream(t5)