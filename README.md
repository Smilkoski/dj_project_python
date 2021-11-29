# Data parser
Python data parser exersize 

Write a text-based application in the source file called app.py, such that it will process a text (.txt) file named example.txt (provided in the project).

# Background

Console apps are usually are made to support the operating system as services.

Some console apps are used to interact with the user by asking questions (input), popular such apps are: grep, find, python (interpreter), ls...

The purpose of this project is to get familiar with reading/writing buffers, inputs, and outputs.

# Getting Started

Clone the code from https://github.com/qpick/dj_project_python.git to get started

```bash
git clone https://github.com/qpick/dj_project_python.git
```

Create your own repo with name: "dj_project_python", and then change the origin with:
```bash
git remote set-url origin https://github.com/petko/dj_project_python.git 
```

**Note**: if your created a repo with different name, change the the above names

# Specification

Your app must meet the following requirements.

1. Python 3.8 is needed as minimum Python runtime

2. [requirements.txt](https://www.idkrtm.com/what-is-the-python-requirements-txt/) is needed for all needed python packages from [pypi](https://pypi.org).

3. A .gitignore https://github.com/github/gitignore/blob/master/Python.gitignore file is needed, use this sample url for a Python based project, it will ignore all
files considered as junk or temporary. In addition please add these lines as well in the .gitignore file:

```
# Pycharm IDE or any JetBrains related IDEs
.idea/**

# Visual Studio Code
.vscode/**

# Local History for Visual Studio Code
.history/**
```

Reference:

- [Python](https://github.com/github/gitignore/blob/master/Python.gitignore)

- [VisualStudioCode.gitignore](https://github.com/github/gitignore/blob/master/Global/VisualStudioCode.gitignore)


3. PEP-8 standard

All python files must follow [pep-8](https://www.python.org/dev/peps/pep-0008/) (Using PyCharm IDE will help with that)

4. Read file - INPUT

Load a file with plain text aka to learn about INPUT data in app.py

5. Parser

A new module aka parser.py file with class or function that will perform data parsing.
The parser must find how many sentences are in the file.
The parse must return a "list []" of sentences and a list of statistics in a dictionary.

Example:

```python
{ 'sentences': [...], 'stats': { 'total_sentences': 10, 'total_chars': 1000 }
```

6. Printing data - OUTPUT

After parsing the data needs to be printed to console. This will guide you on how to use OUTPUT.

Example output:

```
Found total of {total_sentences} sentences. With total of {total_chars} character in the file.... 
```

5. Extra steps. Print at the bottom total time needed to read and print the file

# Hints

- We use the *open* built-in function in order to read file content.

- Modules are included using the *import* statement usually at the top of the current python module.

- The *print* built-in function puts character data to the stdout buffer and will be rendered on the screen if using a terminal.

- This [PEPS](https://www.python.org/dev/peps/) contains the index of all Python Enhancement Proposals, known as PEPs. They exist to make the codebase more readable and propose new features.

- The functions should be documented at the top using [pep257](https://www.python.org/dev/peps/pep-0257/)


