# Workshop Module 4 - First Python class and instance

In this workshop you will complete the file `module-4/sources/report.py` until the assertions pass
and the script execution outputs "OK !".

You will need to create a `Report` class.
* A report has a `filename` (string) and some `pages` (list of `Page`s).
* On initialization, the reports has 0 pages. 
* Pages must be added one by one through the `add_page` instance method.
* The `number_of_pages` instance method returns the number of pages currently in the report.
* The `with_valid_extension` class method returns a `Report` object only if the filename ends 
with ".pdf" or ".txt", otherwise it returns `None`. 


Tip: have a look at the `main()` function. 




-----


**Bonus**:  
Did you use ".pdf" and ".txt" directly in the comparison inside the `with_valid_extension` method ?  

As you saw in module 3, magic values are best avoided. 

Ideally, create a constant class variable. This makes them reusable, for example if you create a
class method to list valid extensions. 
