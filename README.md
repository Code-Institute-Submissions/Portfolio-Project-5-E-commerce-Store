
## **Introduction**
Welcome to my final project, ecommerce applications. This project was inspired by my eldest brothers passion for photography. Which gave me the inspiration to create a website for his photographs so that they can be accessed by different users. This will then enable my brothers photographs to reach a wider audience and enable users to purchase copies of his photography.

In this README I will detail the steps I took to develop and create this project, with the use of  screen photos, images, links, charts and more.

This project is for educational purposes only.

Thank you for viewing my project.

I hope you find the application useful!

---


---

## **Technologies Used**
 - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - This was used for the structure of the web page and it's content.

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
    - This was used to style the HTML document.

- [Bootstrap](https://getbootstrap.com/)
    - This was use to implement help with the mobile first feature of the website.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - This was the main tool used to build this project.

- [PEP8 Python Validator](http://pep8online.com/)
    - This was used to check the python code for any errors or warnings.

- [Heroku](https://heroku.com/)
    - This was used to deploy this application.

- [Heroku Postgres](https://www.heroku.com/postgres)
    - Heroku Postgres is a managed SQL database service provided directly by Heroku.

- [Gitpod](https://gitpod.io/)
    - This was the development environment used to build this project.

- [Git](https://git-scm.com/)
    - This is a version control system which I used to handle my project throughout the development stages, to save and push my work from gitpod to github.

- [Github](http://github.com/)
    - This was used to store my project after it was saved and pushed from gitpod.

- [jQuery](https://jquery.com/)
    - This was used for the interactivity, behaviors of the web.

- [JavaScript](https://www.javascript.com/)
    - This was used for the interactivity, behaviors of the web.

- [Google Fonts](https://fonts.google.com/)
    - The main font of the web site was found on Google Fonts.

- [Font Awesome](https://fontawesome.com/)
    - The icons that was used in this project was found on Font Awesome.

- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - This was one of the most used tool throughout the development of this project, as it can be used for tasks like testing, debugging and showing where elements are positioned on the web page.

- [Balsamiq](https://balsamiq.com/)
    - This was used to design the wireframe created for this project.
---

## **Testing**

For this project, manaual testing was carried out to test the functionalities and components of this website. I almost had great help from the Google developer tool, PEP8 Python validator, JS Hint, The W3C Markup validator and W3C CSS validator.

### **Manual Testing**

**Navigation Bar**

- The nav bar is fully responsive on all resolutions and collapses into a hamburger menu as the resolution is adjusted.
- All links in nav bar is working and navigates to the correct pages.
- Signing in and out work as it should with messages being displayed to users.

**Footer**

- The footer is fully responsive on all resolutions.
- All social media links navigates to correct page. 

**User comments functionality**
This was tested by carrying out the following:
- Creating comments, reading, approving(updating) and deleting comments. Store owners have the ability to carry out full CRUD functionality on the frontend. 
- All buttons are working and navigates to correct pages.
- All buttons are working and performs required tasks.
- Comments page is fully responsive which allows users to post comments on different resolutions.


**Add product page**
- Adding products to the store works as it should with message being displayed to users base on their interactions.
- All buttons are working and navigates to correct pages.
- All buttons are working and performs required tasks.
- Add product page is fully responsive which allows admin/store owners to add products from the fontend on different resoluctions.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.


**Editing product page**
- Editing a product works as it should with message being displayed to users base on their interactions.
- All buttons are working and navigates to correct pages.
- All buttons are working and performs required tasks.
- Editing product page is fully responsive which allows admin/store owners to edit products from the font end on any resolution.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.


**Delete Booking**
- Deleting products works as it should with message being displayed to users base on their interactions.
- All buttons are working and navigates to correct pages.
- All buttons are working and performs required tasks.
- Delete product modal works as it should which challenges users when trying to delete a product.

**Contact-us**
- Contact us page is working as it should with message being displayed to users base on their interactions.
- All buttons are working and navigates to correct page.
- Email get's sent successfully to the database where it's store and displayed on the store inbox page.
- I ran several test submits before the final deployment to ensure the contact us form was working as it should.
- The webpage is fully responsive which allows users to view and fill out the form on any resolution.
- Tested all input fields by intentionally entering invalid data. For example:
    - Entering integers where strings are required and vice versa.
    - Entering special characters where only numbers and letters are required.
    - Entering data that's not specific to inputs fields that requests specific data.
    - Entering the same input numerous times.
    - I asked a few friends to fill out the contact form to monitior if they would encounter any errors which was good for the testing.

**Modals**

- All modal are working base on user interactions
- All modal buttons are working and carrying out required tasks.
- Modal links navigates to correct pages.
- Modal gets toggled on booking page if user is not authenticated.
- Modal works when customers fills out and submit the contact us form.


**Customer(Logged-in) Stories**

- Users have the ability to view their there basket, once they are logged-in.
- When a user is logged-in the nav-bar status changes from Sign in and Sign up to Sign out.



**Validators**

I made made notes of the total amount of errors and warnings I encounter using these validators.

[W3C HTML Validator](https://validator.w3.org/#validate_by_uri)

Total:

-  Error
-  Warnings

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

Total:

- 1 Errors    
- 1 Warnings

[JSHint JavaScript Validator](https://jshint.com/)

Total:

- 4 Errors  
- Undefined variable stripe
    - This varible is being used
    - Unused varible which was rectified after calling the function


#### *Basket App*

I can confirm that I thoroughly went through all the files and folders in basket app, and resolved the errors that could be resolved.


#### *Checkout App*

I can confirm that I thoroughly went through all the files and folders in basket app, and resolved the errors that could be resolved.

During the development of the project, the buildt in python extention in the work space was used to test my python code for Pep8 compliance
- Most of the errors were fixed during the development of the project as I resolved the errors when ever I saw any.
- Alot of the error were related to line spacing and length of characters on each line.
- I can confirm that I thoroughly went through all the pythons files and resolved the errors that could be resolved.



**Testing with Chrome Dev Tools**
I used Chrome developer tools to test the responsiveness of the website. The website was viewed on several different devices such as:

-Desktop

-Laptop

-Iphone SE

-Iphone XR

-Iphone 12 Pro

-Pixel 5

-Samsung Galaxy 8+

-Samsung Galaxy S20 Ultra

-Ipad Air

-Ipad Mini

-Surface Pro 7

-Surface Duo

-Galaxy Fold

-Samsung Galaxy A51/71

-Nest Hub

-Nest Hub Max

-Iphone 6/7/8

-phone 6/7/8 Plus

-Iphone X

-Ipad

-Ipad Pro

**Browser Testing**

The website was tested in different browsers such as:

- Firefox

- Google Chrome

- Safari

- Opera.


---

## **Deployment**

### **Using GitHub and GitPod**
The main branch of this repository has been used for the deployed version of this application.

The following steps were used to create a repository, setup a workspace and use Github and Gipod.

- Click the Use this Template button.

- Give your repository a name, and description is you wish.

- Click the Create repository from template button to create your repository.

- Click the Gitpod button to create a Gitpod workspace, this could take a few minutes.

- When working on the project using Gitpod, it is best to open the workspace from Gitpod as this will open your previous workspace instead of creating a new one.

    - You can commit your work using the following commands:

        1. git add . - adds all updated files to a staging area.

        2. git commit -m " Add short message explaining your commit" - commits all changes to a local repository.

        3. git push - pushes all your commmited changes to your Github repository.

### **Forking the GitHub Repository**
By forking a GitHub repository you can make a copy of the original repository to your own GitHub account to view and make changes without making any changes to the original repository.

1. Log in to GitHub and local the GitHub repository.

2. At the top right of the page, locate "fork button" which is just below the bell icon.

3. You should now have a copy of the original repository in your GitHub account.

### **Deployment to Heroku**

For the project to run on Heroku, there is a list of dependencies that needs to be installed before deploying the project.

First you need to install the support libraries:

- pip3 install 'django<4' gunicorn

- pip3 install dj_database_url==0.5.0 psycopg2

- pip3 install dj3-cloudinary-storage

The list of dependencies goes into the requirements.txt file by using the following:

-  pip3 freeze > requirements.txt

Create your django project using the following:

- django-admin startproject YOURprojectname 

Then create an app using the following:

- python3 manage.py startapp YOURappname

Next add your app to the list of installed app in settings.py

- 'YOURappname'

Then you migrate the changes using the following:

- python3 manage.py migrate

Finally try opening your project in the browser using the following:

- python3 manage.py runserver

- Skeleton of the project should be up and running.

### **Linking to  a Heroku Database**

**Creating a Heroku account and Heroku app**

- Go to [Heroku.com](https://heroku.com/) and create an account.

- From the Heroku dashboard click Create New App button.

- Enter a name for the project and select your region.

- Click the Create App button.

**Creating a Database**

These steps will create a new PostgreSQL database instance for use with your project. If you don't have an ElephantSQL.com account yet, create one [Here](https://www.elephantsql.com/).
- Log in to ElephantSQL.com to access your dashboard.

- Click “Create New Instance”

- Set up your plan

- Give your plan a Name (this is commonly the name of the project)

- Select the Tiny Turtle (Free) plan

- You can leave the Tags field blank

**Create an env.py file**

Keeping things secret!

- In your project workspace, create a file called env.py. It’s a good idea to check that this file is included in the .gitignore file too. If you are using the Code Institute provided GitHub template, then the env.py file is already in the .gitignore file.

- In your env.py file add the following line of code. 
    - import os

- Next we need to set some environment variables. First, add a blank line, then set a DATABASE_URL variable, with the value you just copied from ElephantSQL as follows
    - os.environ["DATABASE_URL"]="<copiedURL>"
    - Replace <copiedURL> with the relevant string from ElephantSQL.
- As this is a Django application it has a SECRET_KEY, which it uses to encrypt session cookies. The secret key can be whatever you like.
We need to include this string in the env.py file. So, just like before, add the variable by pasting in the string as follows.
    - os.environ["SECRET_KEY"]="my_super^secret@key"
    - We don't want to share our secrets either, so this documentation shows you a made up key. Just replace my_super^secret@key with your key
- Make sure you save the file.
This secret file isn’t much good on its own. Carry on to edit your settings.py file on the next page, including connecting up your workspace to the new database.

**Modifying settings.py**

- Now you have created an env.py file, you need to make your Django project aware of it. Open up your settings.py file and add the following code below your Path import
    - import os
    import dj_database_url
    if os.path.isfile('env.py'):
     import env
    - The if statement here acts as a little protection for the application in case you try to run it without an env.py file present. You will use the other import in a moment.
- A little further down, remove the insecure secret key provided by Django. Instead, we will reference the variable in the env.py file, so change your SECRET_KEY variable to the following
    - SECRET_KEY = os.environ.get('SECRET_KEY')

- Now that is taken care of, we need to hook up your database. We are going to use the dj_database_url import for this, so scroll down in your settings file to the database section.Comment out the original DATABASES variable and add the code below, as shown
    - (# DATABASES = {
    (#     'default': {
    (#         'ENGINE': 'django.db.backends.sqlite3',
    (#         'NAME': BASE_DIR / 'db.sqlite3',
    (#     }
    (# }
    
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
The code that has been commented out connects your Django application to the created db.sqlite3 database within your repo. However, as we know, that database is not suitable for production. This line of code separates the database URL stored by your env.py file into the relevant name and password etc.

- With those changes in place, make sure to save your file. Your application will now connect to your remote database hosted on ElephantSQL. Not convinced? Let’s prove it.Run the migration command in your terminal to migrate your database structure to the newly-connected ElephantSQL database
    - python manage.py migrate
Once the migrations have completed, head back over to your ElephantSQL dashboard, select your database instance and then select the “Browser” tab on the left.

Click “Table queries” to reveal a dropdown list, you can see your database structure here. You may not recognise all of the tables in the list, many are generated by the authorisation apps used, the important thing is that this list has been populated from your Django migrations.

- Take a moment to add, commit and push your project to GitHub if you haven’t done so already.

**Heroku Config Vars**
With a new database created and the settings.py file set up to connect to it, we will need to connect our new database to Heroku.

- Go back to the Heroku dashboard open the Settings tab

- Add two config vars:
    - DATABASE_URL, and for the value, copy in your database URL from ElephantSQL, no need to add quotation marks.
    - SECRET_KEY containing your secret key.
So now we have created and connected a remote database, configured our settings.py file (for now…) and created some secrets, we have a few more tasks to complete before we deploy. We’ll go through these in the next:

To improve compatibility with various Python libraries, we have updated the deployment template since this video was made. As a result, you must now add another Config Var in Heroku's Settings.
The key is PORT and the value is 8000



**Final Deployment**

- Make sure DEBUG mode is set to False

- git add . and commit -m changes

Head back over to Heroku and go to Config Vars

- Remove DISABLE_COLLECTSTATIC    1

**Deploy section**
- On the same horizontal nav bar, click the Deploy button.

- Scroll to Deloyment methods and click the GitHub button.

- Go to Connect GitHub and search for your repository name in the search bar.

- Then click the Search button.

- When the repository pop's up below the search bar click the Connect button.

- Scroll down to Automatic and Manual deploys

- Click on the Deploy Branch button to deploy project, which would start building the project, and there is also the Automatic Deploys option which updates the project code everytime
  you push work to the GitHub repository.

- Click on the View button to view app and test to see if it works when the app is successfully deployed.

---

## **Credits**

**Code**

I also found youtube videos that demonstrated and explained how to implement certain functionalities which was really helpful. I refered to online resources where I found code that helped me implement certain functionalities.

- [published by Benignus](https://www.benchatronics.com/detail/how-to-use-slug-and-populate-slug-outsude-django-admin)



These online resources were really helpful when I needed to refamiliarize myself with a specific topic or syntax. They were really education as well.


- [Code Institute](https://codeinstitute.net/)
- [Django documentation](https://docs.djangoproject.com/en/4.1/)
- [Stack Overflow](https://stackoverflow.com/)
- [Freecodecamp](https://www.freecodecamp.org/)
- [programiz](https://www.programiz.com/)
- [PyPI](https://pypi.org/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/)

**Content**



### Acknowledgments 

I want to say thank you to my mentor Harry Dhillon for his time and guidance throughout the development of this project.

Code Institute - I would want to express my gratitude to Code Institute for the help and resources you have given me while I've developed this project. Your support has been really appreciated.

CI Slack Community - I want to say thank you to the Code Institute Slack community which had alot of supportive content at all times.

I want to say thank you to my family and friends who have supported and helped me throughout the development of this project.

Finally, thank you for viewing my final project and I hope you like it!


---




