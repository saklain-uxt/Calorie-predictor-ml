from setuptools import setup, find_packages


HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->list[str]:
      requirements=[]

      with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]


      if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

      print(requirements)
      return requirements







setup(
      name='ML-calories',
      version='0.1',
      description='A package for predicting calories burned based on various features',
      author='saklain khna',
      author_email='saklainkhan728@gmial.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
)