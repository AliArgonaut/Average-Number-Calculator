# Average-Number-Calculator
Given a list of whole number integers by a user, outputs the average of those numbers. 

This is a small project and is actually one of my first. 
it starts by printing the prompt. The prompt is on line one, and it asks the user to input a list of numbers they wish to average. The only request is that individual numbers be separated by spaces, and only whole number integers are used as input. 

It follows up by collecting this input in the form of a string, splitting them up into individual numbers using the .split() function and populating a list with them in line 2. A sum variable is created and set to zero. 

Remember that the list we populated in line 2 was a list of strings, even those these strings are numbers. We don't want a list of strings. We want a list of integers so that the data can be manipulated, so I use a for loop to take the numbers in the first list, convert them into integers, and populate another list. 

A second for loop is set up after this, to run down this list of integers, and add them one by one to our sum variable. This gives us a sum of all the numbers that the user input.

Finally, this sum is divided by the number of items in the list using the len() function. The final value is stored in a variable called avg, and this average is printed out. 
