# Py_make

`Py_Make` is a simple script that generates a simple python project file structure with the necessary files. 



## Installation

    $ pip install py_make

## Usage

After proper installation type, `py_make init` in your terminal to initialize your setting 

    $ py_make init

This will then prompt you to enter your username or name and email

    $ py_make init
    [Username]  <your username or name>
    [User@email.com] <your email>

- `init` is not mandatory, you will still be able to edit information in setup.py

Once py_maker is properly initialized, you will be able to generate a new package by inputting `py_make new`

    $py_make new  <project name>  <version>

- version is optional argument, if nothing is given `0.0.1` will be used instead

