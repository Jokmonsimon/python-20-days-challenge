#!/usr/bin/env python3

# Convert employee to dictionary

import csv

def read_employees(csv_file_location):
	csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
	employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

	employee_list = []
	for dat in employee_file:
		employee_list.append(data)
		return employee_list

	employee_list = read_employees('<file_location')
	print(employee_list)