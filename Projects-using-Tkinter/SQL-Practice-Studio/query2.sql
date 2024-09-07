-- Create Customer Table
CREATE TABLE Customer (
    cust_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    address VARCHAR(50)
);

-- Create Student Table
CREATE TABLE Student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    faculty VARCHAR(50)
);

-- Create Employee Table
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_name VARCHAR(50),
    salary DECIMAL(2)
);
