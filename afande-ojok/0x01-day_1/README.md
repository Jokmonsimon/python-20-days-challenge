# Python - 20 Days Challenge | Day 1 - Python Hello World

## Run Python file

1. Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`

### Code Execution

While inside project directory:

1. Make file execuatble by running `chmod u+x 0-run main.py`
2. Run in terminal `export PYFILE=main.py`
3. Run the Shell script `./0-run`

## Run inline

2. Write a Shell script that runs Python code. The Python code will be saved in the environment variable $PYCODE

### Code Execution

While inside project directory:

1. Make file execuatble by running `chmod u+x 1-run_inline`
2. Run in terminal `export PYCODE='print(f"By 2032, I will be: {2032 - 1993} years old")'`
3. Run the Shell script `./1-run_inline`

## Hello, print

3. Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line. Use the function `print`

## Print integer

4. Complete this [source code](https://github.com/Jokmonsimon/source-codes/blob/main/0x01.py) in order to print the integer stored in the variable `year`, followed by `was the year Yearn AI was founded`, followed by a new line.

- You can find the source code [here](https://github.com/Jokmonsimon/source-codes/blob/main/0x01.py)
- The output of the script should be:
- the `year`, followed by `was the year Yearn AI was founded`,
- followed by a new line
- You are not allowed to cast the variable `year` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)
