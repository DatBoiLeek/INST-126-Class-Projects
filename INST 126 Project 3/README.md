## Project 3 Group Members 
> Malik Callaham

## General
> This project is based on Python reading & parsing a userlog file. 

## Setup
> This project should be ran on applications that support Python 3. 

## Flow for solving the Project
> The first thing I will address about this project is that I will not be able to 100% complete it in the manner that is expected in the course sample text. 
> With that being said, however, I do expect to be able to deliver results for each of the 4 main components of the project, even if those results are not the most pleasing. 
> Lastly, while there are a great many ways of doing this assignment (which is arguably the hardest part of this project), I am going to work on it the best way I know how. 
>Additionally, I expect there to be quite a few text files that python will be writing that contains information specific for each deliverable. 

## Any other challenges encountered so far? 
> Yes, as of 10/30/2020, I have encountered several challenges so far, the biggest being both the irresponsible log and glitch log. I have focused my efforts on the irresponsible 
> log right now though. I did manage to print out each and every person who did not logout from the userlog file (there are about 2k entries, roughly half of the userlog text file). The challenge is setting the output of each entry to be the same, as only one user has the correct notation (output being closely similar to the class sample output). If all else fails I will gladly move on to work on the glitch report, which has proven to be its' own challenge.  

## 11/1/2020 Update
> As of 11/1/20, I was able to solve quite a bit of the project, especially for the glitch log. The output of the glitch log contains every single user that logged out more than they logged in. The problem, however, is exactly the same as with the irresponsible log. Additionally, I created a domain log function that returns the count of every single email domain that is referenced in the user log. I can safely say that the project is near completition, and I hope to be able to solve the irresponsible log and glitch log. As it stands, the only perfect log output is the suspicious text file I have python writing to. All of the other log files that I have written to indeed solves the problem, but not with a desirable output.  

## 11/3/2020 Update
> As of 11/3/20, I realized that there was another issue with the glitch log I created. Column 2, which is the user log activity (login/logout) is printing "login", which is the incorrect activity for the glitch log. I implement the "logout" string in a new variable called user_Glitch as a placeholder until I hopefully can figure out why "logout" is not printing from the column 2 list. 

## 11/8/20 Final Update 
> As of 11/8/20, I've decided to turn in what I have for this project. Indeed, this project has been deemed to be quite a challenge, as I have worked on it from the week of October 26th to now. Admittedly, learning the logic behind this project was fun, but the implementation proved to be a different kind of beast that I have never worked with in a programming language before (specifcally parsing large text files). There are a few things that I did learn during my time with this project. For starters, I could have benefitted quite nicely from using more than just the domainLog function I created specifically for all of the domains in the userlog text file. I could have actually created a function for all of the log file deliverables (which would have made my code look nicer). Secondly, I could have used a dictionary instead of a set, as using a set list makes all values within that list out of order. Third, I could have tried to work on the "count" variable I created, as that was left to be a bit of a hot mess in the end. From what I gathered from my code, my count variable continues to increase with every user who is deemed to either be suspcious, irresponsible, or a glitch in the userlog. All in all, this project was more difficult than project 2: hangman, but in hindsight it did serve as a lesson that I may not be able to complete every project in the way that I want to (as in perfectly). This was a good experience in tackling difficult challenges in using python though, and I hope to at least master the fundementals used in this project for later classes. 



