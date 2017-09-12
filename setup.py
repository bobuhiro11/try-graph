from setuptools import setup, find_packages

with open('requirements.txt') as f:
    req = [p.strip() for p in f.readlines()]

setup(name='try-graph',
      version='1.0',
      description='CLI tool for creating a graph',
      author='bobuhiro11',
      install_requires=req,
      packages=find_packages(),
      entry_points={
          'console_scripts':
          'try-graph = try_graph.main:main'
          },
      zip_safe=False,
      )
