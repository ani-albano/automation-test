# automation-testing

This repository also includes a file with Test Cases and another file with the issues found on the application.

Execution details:
The tests are created in pytest / selenium / python. They can be runned via terminal using the py.test command.
This will automatically execute the test using Chrome as webDriver. In order to use other browser, the command should be the following:

pytest --driver <Selected Browser>


To Run:

docker-compose up --build
