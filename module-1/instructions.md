# Workshop Module 1 - Refresher on git for version control

In this workshop, you will learn how to use the PyCharm IDE to:
* retrieve a GitHub project
* set up a virtual environment
* use the Python Console to run some code snippets
* commit and push some changes


## 1 - Retrieve the GitHub project

* In PyCharm's "Welcome screen", click on "Retrieve from VCS". 
  * Note: if you have other PyCharm projects open, you need to close them first.
* Enter the URL of the repository, indicate your GitHub credentials if asked and continue to the next step. 
* Set the Python Interpreter:
  * select the "new environment" option using Virtualenv
  * leave the other fields as-is


Note: it's recommended to set up a new virtual environment for each project, 
so that you always keep their dependencies separate. 

## 2 - Commit your changes

* Generate a random filename. Open the Python Console (tab on the bottom), copy/paste the following code then click enter.
```python
import random
import string
print(''.join(random.choice(string.ascii_letters) for i in range(20)) + '.txt')
```
* Copy the resulting string. 
* Inside the folder `workshops/module-1/sources/` create a new file with this random string.
* Create a commit with this new change. Open the Terminal (tab on the bottom) and type the following commands:
  * `git add workshops/module-1/<your-random-filename>`
  * Run `git status` and read the output. Was your file staged correctly ? 
  * `git commit -m "new file"`. You can change the commit message as you like.


## 3 - Push to GitHub

Currently, the changes you made are only available in your local workspace. 
To share them with your colleagues, you need to push them to the remote repository.

* Push the commit with `git push`.
  * Did you get an error ? You may need to `git pull` first !


## 4 - Visualise your git log

Make it a habit to regularly check the status of your project (`git status`) and to view the commit history. For this,
go to the "Git" tab at the bottom. Take a look around.
