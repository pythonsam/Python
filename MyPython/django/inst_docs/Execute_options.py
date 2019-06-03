# To know robot version
robot --version

# To get robot help
robot --help > robot_help.txt

# paasing values to variable through command line =>
    robot -v ONE:10 Loop.txt
# create log file             ==> 
    robot -b debug.log test2_list.robot
# validate the test data      ==> 
    robot --dryrun test2_list.robot
# To run particular test case ==> 
    robot -t "Add Two Values" first_test.txt
    robot -t Addition -t "Test Case 3" first_test.txt
    robot -t  Add* first_test.txt
# TO run a test case based on tag => 
    robot -i test2 first_test.txt
# TO run all test cases except given tag => 
    robot -e test2 first_test.txt
# Change logs path ==> 
    robot -d C:\Users\smellamp\Desktop\SRIRAM\INSTITUTION\COURSES\ROBOT_FRAMWEORK\Logs test2_list.robot
