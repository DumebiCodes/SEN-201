# Student Grade Management System – SDLC Documentation

## 1. Requirements Analysis
The purpose of this project is to develop a simple Student Grade Management System.

### Functional Requirements
- The system shall accept a student’s name
- The system shall accept scores for three subjects
- The system shall calculate the average score
- The system shall determine the student’s grade
- The system shall display the result

### Non-Functional Requirements
- The system should be easy to use
- The system should run on any system with Python installed
- The output should be clear and readable

---

## 2. System Design

### Input
- Student name
- Three subject scores

### Processing
- Calculate the average score
- Assign grade based on average

### Output
- Student name
- Average score
- Grade

### Grade Logic
- Average ≥ 70 → Grade A
- Average ≥ 60 → Grade B
- Average ≥ 50 → Grade C
- Average < 50 → Grade F

---

## 3. Implementation
The system was implemented using Python.  
The following functions were used:
- `calculate_average()` to compute the average score
- `determine_grade()` to assign the grade
- `main()` to control program flow

---

## 4. Testing
Manual testing was performed using different score inputs.

### Test Case Example
Input: 80, 70, 90  
Expected Output:
- Average: 80
- Grade: A

---

## 5. Deployment
The program is deployed by running the Python file using:
python student_grade_system.py

---

## 6. Maintenance
Future improvements may include:
- Adding more subjects
- Saving records to a file
- Adding a graphical user interface

