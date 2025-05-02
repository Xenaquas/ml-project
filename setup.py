from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] 

setup(
name='ml-project',
version='0.0.1',
author='Hamza',
author_email='hmsk.tech@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)