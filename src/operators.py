from airflow import kubernetes
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from kubernetes import client, config 



class KernelOperator(BaseOperator):
    """Operator for launching kernels"""

    @apply_defaults
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = "Hello {}".format(self.name)
        print(message)
        return message



class KernelPlugin(AirflowPlugin):
  name = 'kernel_operator'
  operators = [KernelOperator]
