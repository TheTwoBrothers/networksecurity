from setuptools import  find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
        THis function will return list of requiremnts
    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
           #read  lines from files
           lines=file.readlines()

           for line in lines:
               req=line.strip()
               if req and req!='-e .':
                   requirements_lst.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")  

    return requirements_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Ut",
    author_email="sweetsingh3690@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)                
               
