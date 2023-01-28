# cs50DjangoDemo

This repository is a playground for learning Django. 
It includes the following small projects that build on each other:

1. "Hello" app that uses routes to greet user by name using string from URL
2. "Is it My Birthday" app that allows users to enter their b-day as input and routes
   (using Django templating language) users to a template that either wishes them Happy Birthday
   or tells them that it's not their Birthday. (Inspired by https://isitchristmas.com/, but different
   in that it accepts user input.)
3. "Tasks" app that allows users to add tasks to a task list. This project incorporated using a 
   layout.html file to avoid duplication, storing tasks in a simple db, and incorporating sessions 
   so each user could have their own task list.
4. "WingCo" - an app that allows for tracking flights. This app used models and migrations to create 
   several tables (sqlite3), connected to each other with primary/foreign keys. Other lessons learned
   from this project include basics of preventing SQL injection attacks and practice using the terminal
   to work with databases and in the Python shell.
   
This code is my own work, but the work was guided by the CS50w course lectures 3 and 4 (2021).
