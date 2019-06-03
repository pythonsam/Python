# To execute python file by pytest 
python -m pytest pytest_example.py 
pytest pytest_example.py 

# To get print function output on console
python -m pytest pytest_example.py -s

# To Run particular testcase
python -m pytest pytest_example.py -s -k test_add

# To Run particular testcases
python -m pytest pytest_example.py -s -k test_

# To skip particular testcase
pytest pytest_example.py -s -k " not test_a"