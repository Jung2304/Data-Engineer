from airflow.sdk import dag, task
"""
- Warning while importing the dag and task decorators because they are not installed in our local env.
- But they will be available inside the Docker container
"""

@dag
def jungdag():

  @task(task_id = "first_task")
  def first_task(): 
    return "Hello, World!"

  @task
  def second_task():
    return 67

  @task
  def third_task():
    return 34.5

  # Designing the task dependencies (DAG workflow)
  first_task() >> second_task() >> third_task()

# To register the DAG, you need to create an instance of the DAG function
jungdag() 
