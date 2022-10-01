# Libraries & Packages Reference

A Python library is a collection of related modules. It contains bundles of code that can be used repeatedly in different programs.
It makes Python Programming simpler and convenient for the programmer. Always better to stay with Zen of Python principles.
```txt
Simple is better than complex.
```
### How to install any library or package for Python
There are a bunch of libraries which is built-in, and you do not need to install but also there are libraries which is stored
in PyPi. The Python Package Index (PyPI) is a repository of software for the Python programming language.
If we want to use 3rd party libraries we can download from this platform with PIP command.
1. If you worked with Linux you should know that always good idea to refresh package information from all configured sources with **sudo apt-get update** command. In Python we must always update our PIP command
```bash
python -m pip install --upgrade pip
```
2. Python 101 the way of downloading any packages from PyPi. Below you can see how to download turkish-validator library from PyPi (my first package on PyPi)
```bash
python -m pip install turkish-validator
```
3. Also if you working with high level IDEs such as PyCharm with their GUI you can easily manage package installation.
```bash
File > Settings > Project : burgerzilla > Python Interpreter > Click + (plus)
```
PyCharm is connected PyPi repository default. You only need to type name of library and click install
## Challenges while work with libraries
While you working on big projects it's normal to have various libraries which you need to install and when you need to deploy it might be hard to manage without structuring.
There are lots of way to do it but let's talk about two common way.
1. **requirements.txt** ; The requirements.txt file is used for specifying what python packages are required to run the project you are looking at.  Typically, the requirements.txt file is located in the root directory of your project.
2. **Poetry** ; 2nd Way

### How I managed dependencies
I decided to use Poetry during my project because of various pros and nice features.
- Poetry comes with an exhaustive dependency resolver, which will always find a solution if it exists.
- Poetry either uses your configured virtual environments or creates its own to always be isolated from your system.
- Poetry's commands are intuitive and easy to use, with sensible defaults while still being configurable.

### Simple Poetry Application
1. Create new Poetry Application
```bash
poetry new burgerzilla
```
The pyproject.toml file is what is the most important here. This will orchestrate your project and its dependencies.
2. This command will automatically find a suitable version constraint and install the package and sub dependencies.
```bash
poetry add turkish-validator
```
3. To install dependencies which is stored in *pyproject.toml* for your project, just run this command.
```bash
poetry install
```
5. Running your script
```bash
poetry run main.py
```

### Libraries used during project
* Microservices Management
  * Flask ; base for everything
  * Flask-login ; base for authentication
  * Requests ; Communication between different microservices
* Database & ORM Integration
  * Flask-Migrate ; Database schema migration support.
  * SQLAlchemy ; ORM Mapping
  * alembic ; A database migration tool for SQLAlchemy.
* API Management
  * flask-restx
  * Flask-JWT-Extended
* General Management
  * poetry ;Dependency Management for Python
  * flake8 ; Style Guide Enforcement
  * black ; Style Guide Automatic Apply
