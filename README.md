# Py_maker

`Py_Maker` is a simple script that generates a simple python project file structure with the necessary files. 



## Installation

    $ pip install py-maker

## Usage

After proper installation type, `py_maker init` in your terminal to initialize your setting 

    $ py_maker init

This will then prompt you to enter your username or name and email

    $ py_maker init
    [Username]  <your username or name>
    [User@email.com] <your email>

- `init` is not mandatory, you will still be able to edit information in setup.py

Once py_maker is properly initialized, you will be able to generate a new package by inputting `py_maker new`

    $py_maker new  <project name>  <version>

- version is optional argument, if nothing is given `0.0.1` will be used instead

