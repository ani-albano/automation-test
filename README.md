# automation-testing

This repository contains the whole Test Suit including Test Cases and Issues found during the manual execution. 
To run it, clone the repository or download it as a .zip and locate it on a path locally. 
There is a docker-compose.yml file in order to run it, so it is necessary to install Docker on the local machine. To check the installation, run:

`docker --version`

Be aware that, if you are using Windows Home, Docker Desktop will not work so, instead, we must chose Docker Toolbox option that will behave as a terminal to run 
commands.
If all is set, then run the following to start the tests:

`docker-compose up --build`

This command will install all dependencies needed for the test, alongside Chromedriver, so there is no need to install nothing but Docker
on the local machine.

There is another way to run this test suit without using Docker, but it will need the installation of:

`python 3.8`
`pytest`
`Selenium Webdriver`

And we will need an IDE, I recommend PyCharm or Visual Studio Code.
On PyCharm, we will need to set the interpreter once the repository is open so, on the bottom right, there is a button for Python 3.8. By clicking
it we can select the option *Interpreter Settings* and Selenium from the list. Then, on the top right, *Edit Configuration -> Python Test* and set
the path in which the test are installed. Then run it, this can be also done from the console stepping on the path with the following command:

`py.test` or `py.test --<driver>` selecting the driver in which the test will run.

Docker option is easier and faster so it's highly recommended. 

Thank you!
