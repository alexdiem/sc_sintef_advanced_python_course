# README

Welcome to the course material for _Advanced Python3: Object oriented programming, databases and visualisation_. This course is developed with Simula Consulting and covers three main topics: Object-oriented programming, databases, and advanced visualisation. Each lecture is designed interactively, and each sub-lecture is concluded by a set of practical exercises.

### Day 1

09:00-15:00 L01 Object-oriented programming (OOP) in Python

- Intro to OOP principles in Python
- Objects, functions, methods, classes
- Inheritance and polymorphism
- Packaging modules

15:00-16:00 L02 Databases, part I

- Intro to databases: what and how

### Day 2

09:00-11:30 L02 Databases, part II

- Intro to Django
- Intro to Sqlalchemy
- Intro to Psycopg

12:30-16:00 L03 Visualisation

- Intro to Matplotlib and Plotly
- Hands-on and practice
- Intro to Bokeh


## Requirements and installation instructions

The course is based on Python 3 and covers django, sqlalchemy, psycopg, Matplotlib, Plotly, and Bokeh libraries. The course material is provided as Jupyter Notebooks.

We strongly recommend using [Anaconda](https://www.anaconda.com/distribution/) to set up a dedicated virtual environment for the course material. This avoids potential conflicts between the libraries required for the practical parts of the course and any previously installed Python libraries. To set up a new conda environment and activate it run
```
conda create --name python-course
conda activate python-course
```

To exit a conda environment run
```
conda deactivate
```

Once the environment is activated you can install all required packages:

```
conda install -c conda-forge jupyterlab
```

To install the visualisation tools:

```
conda install -c conda-forge matplotlib
conda install -c plotly plotly
conda install -c bokeh bokeh
```

The database tools require their own environments to avoid conflicts:

```
conda create --name python-course-db
conda activate python-course-db
conda install -c anaconda django
conda install -c anaconda sqlalchemy
conda install -c anaconda psycopg2
```


## Getting started

The course material is provided as Jupyter Notebooks and is best accessed via [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) (available in conda). To start a JupyterLab session run

```
jupyter lab
```

This should automatically open a window in your browser. If not, copy the URL from the commands output. It should be of the format http://localhost:8888/?token=xxxxx or http://127.0.0.1:8888/?token=xxxxx.