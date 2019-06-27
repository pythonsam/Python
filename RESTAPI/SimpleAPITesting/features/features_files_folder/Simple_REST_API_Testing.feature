Feature: REST API testing framework using Java REST Assured or JayWay Libraries
	Raise request(s) using REST Assured library
	Validate HTTP response code and parse JSON response using REST Assured library
	Make sure to run the intended REST API based web application as pre-condition
Background:
	Given Set basic web application url is "http://localhost:8090/imademethink/restfulapi/account_basic/"
	And Set basic user details as "<particular>" and "<value>" below
		| particular                                      | value                                                  |
		| email                                             | Kuppy01@aaa.com                             |
		| password                                      | k9aPass                                             |
		| first_name                                     | Sheldon                                             |
		| last_name                                     | Cooper                                               |
		| gender                                          | m                                                       |
		| signup_secret_question_1              | What is the brand of your toothpaste   |
		| signup_secret_question_2              | What was the name of your babysitter |
		| signup_secret_question_1_answer | Pune                                                  |
		| signup_secret_question_2_answer | Toystory                                             |
		| session id                                      | empty                                                 |

Scenario:GET request Example
	Given Set GET api endpoint as "signup"
	When Set HEADER param request content type as "application/json"
	And Set HEADER param response accept type as "applications/json"
	And Set Query param as "empty"
	And Raise "GET" HTTP Request
	Then Valid HTTP response should be received
	And Response HTTP code should be 200
	And Response HEADER content type should be "application/json"
	And Response BODY should not be null or empty
	And Response BODY parsing for "GET_signup" should be successful