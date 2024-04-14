from setuptools import find_packages, setup
from typing import List
import os

HYPHEN_E_SPACE_DOT = '-e .'

def get_req_list(path:str)->list():

    requirments = []

    with open(path) as file_obj:

        requirments = file_obj.readlines()

        requirments = [req.replace('\n', '') if '\n' in req else req for req in requirments]

        requirments = [req for req in requirments if req != HYPHEN_E_SPACE_DOT]

        print(requirments)

        return requirments


setup(
    name='Customer_churn_project',
    version='0.0.1',
    author='sahil',
    author_email='sahil15shinde@gmail.com',
    install_requires=get_req_list('requirements.txt'),
    packages=find_packages()
)