the file to complete is users.py

It is about users in a shopping website

There are different types of users: ModeratorUser, CustomerUser, AdminUser

* All users have a name and internal id
  * id should be incrementing with each new user created 
* Moderators are responsible for some forums, which are given as a string set in their parameters
* AdminUsers are admins to the site, they don't show any particular behaviour within the scope of this workshop
* CustomerUsers have a balance, to buy products.
  * they can buy a given product if they have the balance to afford it


The workshop tasks are:
* Construct a hierarchy of class to represent different types of users
* extract common behaviours into a parent class
* implement the relevant methods (can_buy, __str__)
* users must have an internal id that increments with each new user