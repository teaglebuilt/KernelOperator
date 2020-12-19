from setuptools import setup, find_namespace_packages

setup(
    name='KernelOperator',
    entry_points = {
        'airflow.plugins': [
            'my_plugin = src.operators:KernelPlugin'
        ]
    }
)