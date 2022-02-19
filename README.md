# Gradescope Autograder Script

A marking script (autograder code) to mark the submissions using Input/Output in a file format with suitable late 
submission penalty for Python assignments/submissions by <a href="https://arpit-gole.github.io/portfolio/">Arpit Gole</a>.

This marking script makes the setting up of the assignment easy. Just change 4 variables in the `run_autograder` 
script as per your needs. These variables are:
1. `num_of_test_cases` - Specifies the total number of test cases needs to be satisfied.
2. `points_per_test_case` - Marks related to each test case.
3. `student_code_file_name1/student_code_file_name2` - Main files to run the test cases on.
4. `no_of_test_cases_to_run_for_file1` - Number of test cases to run on each submitted file.

Additionally, this marking script can make 2 different files. Ideally, can extend the same 
idea to mark n number of files (slight modifications needed.)

## Running 

1. Gradescope marks the submission based on the marking flow defined in `run_autograder` script. 
Modify to have a custom marking flow.

2. Package management for the submission environment is done through `setup` script. 
Currently, the submission will run in Python 3.6.9 and the `run_autograder` script will run in Python 3.8.0.
Yes, there are 2 different environments:- one submission and another running the marking script.

3. (Optional) Extra level of package management can de done through `requirements.txt`.

4. The `test_case_files` folder houses all the Input and Output on test case basis. 
For each test case 1 Input and 1 Output (correct) is supplied to run the submission.

5. Finally, create a `*.zip` of these 4 files: `run_autograder`, `setup`, `test_case_files` and `requirements.txt` 
to upload it on the Gradescope's Configure Autograder section. A sample is provided.

6. (Optional) Providing python scripts to Test Autograder upon successful built of docker image.

**Happy Marking.**
