# Workshop Module 1 - Refresher on git for version control

In this workshop, you will learn how to use the PyCharm IDE to:
* use the Python Console to run some code snippets
* commit and push some changes

## 1 - Commit your changes

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


## 2 - Push to GitHub

Currently, the changes you made are only available in your local workspace. 
To share them with your colleagues, you need to push them to the remote repository.

* Push the commit with `git push`.
  * Did you get an error ? You may need to `git pull` first !


## 3 - Visualise your git log

Make it a habit to regularly check the status of your project (`git status`) and to view the commit history. For this,
go to the "Git" tab at the bottom. Take a look around.
