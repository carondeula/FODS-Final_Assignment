import pandas as pd
import numpy as np
from datetime import datetime

'''
Description of program:
This program creates a Pandas DataFrame containing employee information and performs
multiple data analysis and manipulation operations on it. The operations include:
- Selecting specific columns (Name, Salary)
- Filtering rows based on conditions (department, age)
- Calculating aggregate statistics (average salary by department)
- Counting employees by department
- Adding calculated columns (Bonus)
- Replacing values (HR to Human Resources)
- Finding employees with longest tenure
- Creating categorical columns (SalaryCategory)
- Checking for and removing duplicates
- Calculating statistical measures (median age)

The program demonstrates a wide range of Pandas DataFrame operations that are
commonly used in data analysis and data manipulation tasks.
'''

def employee_operations():
    """
    Performs various operations on an employee DataFrame to demonstrate Pandas functionality
    
    Returns:
        Results of various DataFrame operations
    """
    # Create the employee DataFrame
    data = {
        'EmployeeID': [101, 102, 103, 104, 105],
        'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
        'Age': [30, 28, 35, 40, 25],
        'Salary': [70000, 60000, 80000, 90000, 55000],
        'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
        'ExperienceYears': [5, 3, 7, 11, 2]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Convert JoinDate to datetime
    df['JoinDate'] = pd.to_datetime(df['JoinDate'])
    
    print("Original DataFrame:")
    print(df)
    print("\n")
    
    # a. Select only Name and Salary columns
    name_salary = df[['Name', 'Salary']]
    print("a. Name and Salary columns:")
    print(name_salary)
    print("\n")
    
    # b. Filter out all employees in the "IT" department
    non_it_employees = df[df['Department'] != 'IT']
    print("b. Employees not in IT department:")
    print(non_it_employees)
    print("\n")
    
    # c. Select employees who are older than 30
    older_employees = df[df['Age'] > 30]
    print("c. Employees older than 30:")
    print(older_employees)
    print("\n")
    
    # d. Average salary by department
    avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
    print("d. Average salary by department:")
    print(avg_salary_by_dept)
    print("\n")
    
    # e. Count employees in each department
    employees_by_dept = df.groupby('Department').size()
    print("e. Number of employees in each department:")
    print(employees_by_dept)
    print("\n")
    
    # f. Add Bonus column (10% of salary)
    df['Bonus'] = df['Salary'] * 0.1
    print("f. DataFrame with Bonus column:")
    print(df)
    print("\n")
    
    # g. Replace "HR" with "Human Resources"
    df['Department'] = df['Department'].replace('HR', 'Human Resources')
    print("g. DataFrame with 'HR' replaced:")
    print(df)
    print("\n")
    
    # h. Find employee(s) with longest tenure
    longest_tenure = df[df['JoinDate'] == df['JoinDate'].min()]
    print("h. Employee(s) with longest tenure:")
    print(longest_tenure)
    print("\n")
    
    # i. Create SalaryCategory column
    df['SalaryCategory'] = np.where(df['Salary'] > 75000, 'High', 'Low')
    print("i. DataFrame with SalaryCategory column:")
    print(df)
    print("\n")
    
    # j. Check for duplicate EmployeeIDs and remove if found
    print("j. Checking for duplicate EmployeeIDs:")
    duplicates = df[df.duplicated('EmployeeID')]
    if len(duplicates) > 0:
        print(f"Found {len(duplicates)} duplicates")
        df = df.drop_duplicates('EmployeeID')
        print("After removing duplicates:")
        print(df)
    else:
        print("No duplicate EmployeeIDs found")
    print("\n")
    
    # k. Calculate median Age
    median_age = df['Age'].median()
    print(f"k. Median Age of all employees: {median_age}")
    
    return df

# Test the function
result_df = employee_operations()