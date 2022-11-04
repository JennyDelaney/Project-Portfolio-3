# Jessies Bakery Ordering System
🖥️ [LIVE SITE](https://pp3-python-project-jennyd.herokuapp.com/)

[Google Spreadsheet](https://docs.google.com/spreadsheets/d/1IozhzTB6fqk72Od6aukyqtRx9t3MKGp7EV4Our-_9ek/edit?usp=sharing "Google Spreadsheet")

![Opening Image](/readme_images/opening_screen.jpg)

This project is based on a simple ordering system for a local bakery to capture cake orders from their customers, allowing people to order their cakes from anywhere.  It takes the Customers order and puts it into a spreadsheet for the baker to know what they need to bake.

## UX

### First Time User Goals
As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.
As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

### Returning User Goals
As a returning user, I want to be able to continue ordering my cakes from anywhere.

## Flowchart

![Flowchart](/readme_images/flowchart.jpg)

### Design

Being an ordering system it is simple to follow.  It is set up to allow the Customer to input the number of tiers they would like the cake to be, the flavour of sponge that they would like, the size of the cake and the filling they would like in the cake.

The terminal keeps the black background and the text has been left white.

### Features

The terminal displayed is the default from the CI template.  It captures the order and inputs the information into a google spreadsheet for the baker to know what orders are required.

![spreadsheet image](/readme_images/spreadsheet.jpg)

### Features to implement in future
More options to the cakes could be added to it, to increase and extend the varieties available for the cake. This will encourage the users to return.

## Technologies Used

- Python
- GitHub
- GitPod
- Heroku
- Google Spreadsheet

## Testing

The site had been tested in Chrome, Firefox and Edge without noticable trouble. Safari won't run the app but it shows it, after checking various sources it was confirmed that the terminal won't run on OS or Mobile so it should be expected and to mention it.

### Testing User Stories from User Experience (UX) Section
#### First Time Visitor Goals
**As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation**.

Upon entering the site, users are automatically greeted with a clean and easily readable notification that they are in Jessies Bakery Ordering System.

The main points are made immediately with the introduction text.

**As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.**

The site has been designed to be fluid and never to entrap the user. It clearly displays the answers that are required from the Customer in order to be able to proceed to the next step.

#### Returning Visitor Goals
**As a returning user, I want to be able to continue ordering my cakes from anywhere.**

The site allows for the user to run the program again to order more than one cake.

## Validation
At the moment of concluding the project the site pep8 is still down, I used the pycodestyle built in my workspace in gitpod, and I got the  following results as shown in the screenshot below.

![GitPod Validation](/readme_images/gitpod_validation_results.jpg)

It shows three warnings related to ms-toolsai.jupyter extension and .gitpod.yml but these are not part of the code, or anything that interferes with the app so they had been left alone as confirmed with Tutor Assistance.

It shows no errors for the run.py. However, it does show 3 warnings and 7 information tags. The warnings are relating to the use of global statements.  After searching on this it was confirmed that this is not an issue to be concerned about and does not interfere with the program.

There are also the following information tags - Missing docstring : this relates to the template used from Code Institute and therefore we were advised not to be concerned about it.  Chosen name doesn't conform to UPPER_CASE naming style.  Again after discussions with mentor this is not an issue to be concerned about.

## Manual Testing

Friends and family were asked to test the program and it was discovered that when text was entered against any of the questions - number of tiers, cake size, sponge flavour and sponge filling it crashed the program.  I needed to include additional validation code in order to stop this from happening.  The following screenshot shows a sample of the error that they were getting - 

![Error Sample](/readme_images/error_sample.JPG)

After fixing the code by adding a try and except to handle this error it solved the problem.

### Final Testing outcomes - 

![Testing Outcomes](/readme_images/testing_outcome.jpg)

## Deployment

The site had been deployed through Heroku.
The site had been developed on GitPod, committed and pushed to GitHub. And Heroku once the site is deployed would update automatically.

## Credits

All code was created and manipulated by myself after searching answers in google and having dicussions with my mentor. Websites I used more than once were - Geeks for Geeks, W3Schools and Stack Overflow, as well as Code Institute Course content.

I would like to say a huge thank you to my new mentor Spencer Barriball, who guided me in the project and especially in the different methods available to use when pulling the information from my google spreadsheet.

I would like to thank my family who tested the ordering system for me.