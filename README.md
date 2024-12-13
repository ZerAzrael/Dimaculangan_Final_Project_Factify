# Dimaculangan_Final_Project_Factify

I. PROJECT OVERVIEW 
 
Factify is a web application designed to provide users with accurate and reliable information in a quick and engaging format, catering to the modern need for fast learning. In an era where attention spans are shorter, Factify aims to deliver bite-sized facts that users can easily absorb in a short amount of time, making it ideal for busy individuals who want to learn something new without overwhelming themselves. 
The app allows users to log in and register for an account, ensuring secure and personalized access. With both dark mode and light mode options, users can customize their viewing experience for comfort. The interface is user-friendly, designed to provide a smooth and intuitive navigation experience. 
The core feature of Factify is the presentation of various facts that users can browse through quickly. The app encourages engagement by allowing users to rate the facts and save their favorites. This interactivity helps users better retain the information they encounter. 
Factify's back-end is powered by a well-structured database, consisting of four core tables: User Table, Fact Table, Rating Table, and Favorite Table. These tables are connected through a Database Management System (DBMS), ensuring secure, fast, and organized access to the data. The system enables efficient handling of user accounts, factual content, ratings, and favorites, making the app reliable and scalable. 
By offering quick, digestible information, Factify seeks to enhance learning while respecting the time constraints of today's fast-paced world. It caters to individuals who want to stay informed without committing large amounts of time, making learning both fun and efficient. 
 
 
CITAITON: 
Using Technology to Enhance Learning Experiences. 
Edutopia. (2024). Using technology to enhance learning experiences. Available at Edutopia. https://www.edutopia.org  
These 3 charts show how online learning is growing globally 
World Economic Forum. (2024). These 3 charts show how online learning is growing globally. 
Available at World Economic Forum. https://www.weforum.org/agenda/2020/04/coronavirus-education-global-covid19-onlinedigital-learning/

II. PYTHON CONCEPTS AND LIBRARIES 
1. Object-Oriented Programming (OOP) 
Object-Oriented Programming (OOP) is a core concept in this application, where the program is structured around objects and classes. The LoginApp class in the code encapsulates the main functionality of the app. This class contains methods to handle different operations such as user login, registration, and displaying facts. By using OOP, the application can be organized into manageable components that can be reused and extended. For instance, creating methods within the LoginApp class ensures that the logic for each action (like logging in, registering, etc.) is neatly packaged, making the code easier to maintain and update. 
2. Tkinter GUI 
Tkinter is the standard GUI toolkit for Python, and it’s used in this code to create a user interface for the application. The app uses various Tkinter widgets like Label, Entry, Button, and Frame to build the user interface. The LoginApp class contains methods that create different windows and dialogs for user interaction. For example, when a user logs in or registers, the interface is updated with new widgets to allow for interaction, such as entering a username, password, or selecting a theme. The app dynamically changes the UI components based on the user's actions, providing a smooth and intuitive experience. 
3. Database Interaction (MySQL) 
The application connects to a MySQL database using the mysql.connector module. This connection is established through the connect_to_database method, which allows the application to interact with the database, execute queries, and manage user data. For instance, when a user logs in, the app queries the users table to verify the provided username and password. Similarly, when a user adds a new fact or updates their profile, those actions are reflected in the database. The database is integral to the app’s functionality, storing critical information such as user credentials, facts, ratings, and favorites. 
4. PASSWORD Hashing 
To ensure the security of user data, the application employs password hashing. Instead of storing plain text passwords, the code uses the SHA-256 algorithm from the hashlib module to convert the password into a fixed-length string of characters. This hashed password is stored in the database, making it difficult for anyone who gains unauthorized access to retrieve the original password. When a user logs in, the entered password is hashed again and compared to the stored hash to verify authenticity. This method provides an added layer of protection for sensitive user data. 
 
5. Switching Themes (Dark/Light Mode) 
The application offers a feature to toggle between dark and light modes, which is increasingly popular in modern applications to reduce eye strain. The theme switching functionality is implemented through a button in the GUI that allows the user to switch between the two modes. When the button is clicked, the background color, text color, and widget styles are updated accordingly to fit the chosen theme. This enhances the user experience by allowing them to customize the appearance of the app according to their preferences, whether they are in a well-lit environment or using the app in a dark room. 
6. Parameterized SQL Queries 
To prevent security risks such as SQL injection, the application uses parameterized SQL queries. In these queries, user input is not directly inserted into the SQL statement. Instead, placeholders are used, and the input values are bound to these placeholders separately. This technique ensures that user input is treated as data, not executable code, thereby protecting the application from malicious attacks that could compromise the database. This approach is critical for maintaining the integrity and security of the app's database interactions. 
7. Error Handling 
The app includes error handling to manage potential issues, such as database connection errors or incorrect login credentials. Try-except blocks catch these exceptions and display helpful error messages, preventing crashes and improving the app's stability. 
8. Rating and Favoriting Features 
The app lets users rate and favorite facts, stored in separate ratings and favorites tables. Ratings are integers (1-5), and favorites track the facts users like most. This creates a personalized experience, allowing users to save and revisit their favorite content, with the data securely stored in the database for easy retrieval or updates. 
9. Fact Generation and Display 
One core feature of the app is generating and displaying random facts fetched from the database. Logged-in users can view these facts, and those with the right permissions can add new ones, ensuring a dynamic and engaging collection of information that encourages user interaction. 
10. User Dashboard 
Upon successful login, users are taken to a dashboard where they can view their personalized content and interact with the app. The dashboard is the central hub for managing facts, ratings, and favorites. It provides options for users to explore different features such as adding new facts, viewing their rated and favorite facts, and adjusting account settings. The dashboard serves as the main interface for users to interact with the app, providing easy access to all of the app's core functions in one place. 

III. SUSTAINABLE DEVELOPMENT GOALS 

1. Quality Education (SDG 4) 
Factify aims to provide users with access to reliable information and learning opportunities through facts, which can support education and knowledge sharing. 
2. Decent Work and Economic Growth (SDG 8) 
By offering users a platform to contribute facts, Factify can potentially promote economic opportunities, as users might gain exposure and recognition for their contributions. 
3. Responsible Consumption and Production (SDG 12) 
Through the process of fact-checking and responsible information sharing, Factify supports the responsible production and consumption of knowledge. 
4. Reduced Inequalities (SDG 10) 
By offering a platform for users from diverse backgrounds to contribute facts, Factify helps promote inclusivity and ensures that people from all walks of life have a voice in sharing knowledge. 
5. Peace, Justice, and Strong Institutions (SDG 16) 
Factify’s focus on fact-checking and accurate information supports transparency, accountability, and informed decision-making, which aligns with the goal of promoting justice and strong institutions. 

IV. PROGRAM/SYSTEM INSTRUCTIONS

Step 1: Run the Program
First, make sure you have all the necessary dependencies installed (e.g., tkinter for the GUI and mysql-connector-python for the MySQL database connection).
Run the Python script. This will open a window titled "Factify" with a login screen.

Step 2: Logging In
Enter your username in the Username field.
Enter your password in the Password field.
Click the Login button to log in.
If the username and password are correct (after being hashed and stored in the database), you will be redirected to the dashboard screen.
If the credentials are incorrect, an error message will pop up.

Step 3: Registering a New Account
If you don’t have an account, click the Register button on the login screen.
You will be directed to the Register screen where you need to:
Enter a Username.
Enter a Password.
After filling in the fields, click the Submit button.
If the username is already taken, an error message will appear.
If registration is successful, you will be redirected back to the login screen.

Step 4: Forgot Password
On the login screen, click the Forgot Password? button.
Enter your Username and click the Send Verification Code button.
A verification code will be generated and shown to you. Enter this code along with your New Password and click Submit to reset your password.
If the code is correct, your password will be updated, and you will be able to log in with the new password.

Step 5: Deleting Your Account
On the login screen, click the Delete Account? button.
Enter your Username and click Send Verification Code.
After receiving the verification code, confirm your deletion by entering your password.
Once confirmed, your account will be deleted from the database, and you will be redirected back to the login screen.

Step 6: Using the Dashboard (Once Logged In)
After logging in, you will be redirected to the Dashboard.
On the dashboard, you will see several buttons:
Generate a Fact: This will show a randomly selected fact from the database.
Add a Fact: This will take you to the screen where you can add a new fact.
View Favorites: This will display all the facts you have added to your favorites.
Logout: This will log you out of the app and take you back to the login screen.

Step 7: Adding a Fact
On the Add a Fact screen, enter a Fact in the text field.
After typing the fact, click the Add Fact button.
The fact will be stored in the database, and a success message will appear.
If you want to go back to the dashboard, click the HOME button.

Step 8: Generating a Random Fact
On the Dashboard, click the Generate a Fact button.
A randomly selected fact from the database will appear on the screen.
You will be asked to rate the fact from 1 to 5 stars. Choose the star button to submit your rating.
You can also Add to Favorites by clicking the "Add to Favorites" button. If the fact is already in your favorites, you will be notified.
To go back to the dashboard, click the HOME button.

Step 9: Viewing Favorite Facts
On the Dashboard, click the View Favorites button.
This will show you a list of facts you have added to your favorites.
If you have no favorite facts, you will be informed.
If you have favorite facts, they will be displayed in a scrollable list.

Step 10: Theme Toggle (Dark/Light Mode)
On any screen, click the 🌙 button (located in the top-left corner) to toggle between dark and light mode.
Dark mode will change the background to black and text to white.
Light mode will change the background to white and text to black.
