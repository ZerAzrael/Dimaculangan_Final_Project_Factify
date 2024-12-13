import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import mysql.connector
from mysql.connector import Error
import hashlib


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Factify")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Database Connection
        self.connection = None
        self.cursor = None
        self.connect_to_database()

        # Dark mode state
        self.is_dark_mode = True

        # Current user tracking
        self.current_user_id = None

        # Initialize UI
        self.create_toggle_button()
        self.create_login_screen()
        self.apply_theme()

    def create_toggle_button(self):
        self.toggle_button = tk.Button(
            self.root, text="🌙", font=("Arial", 12), width=3, command=self.toggle_theme
        )
        self.toggle_button.place(x=10, y=10)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            self.root.configure(bg="black")
            text_color = "white"
            button_color = "purple"
            entry_bg = "black"
            entry_fg = "white"
            self.toggle_button.configure(text="☀️", bg="black", fg="white")
        else:
            self.root.configure(bg="white")
            text_color = "black"
            button_color = "light blue"
            entry_bg = "white"
            entry_fg = "black"
            self.toggle_button.configure(text="🌙", bg="white", fg="black")

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=self.root["bg"], fg=text_color)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=button_color, fg=text_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=entry_bg, fg=entry_fg)
    
    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Welcome To FACTIFY!", font=("Arial", 30, "bold")).pack(pady=40)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        def login():
            self.login()

        tk.Button(self.root, text="Login", font=("Arial", 12), command=login).pack(pady=15)
        tk.Button(self.root, text="Register", font=("Arial", 12), command=self.create_register_screen).pack(pady=5)
        tk.Button(self.root, text="Forgot Password?", font=("Arial", 12), command=self.create_forgot_password_screen).pack(pady=5)
        tk.Button(self.root, text="Delete Account?", font=("Arial", 12), command=self.create_delete_account_screen).pack(pady=5)


    def clear_screen(self):
        for widget in self.root.winfo_children():
            if widget != self.toggle_button:
                widget.destroy()
        self.create_toggle_button()

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='factify',
                user='root',  # adjust if different
                password=''   # adjust if you have a password
            )
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Successfully connected to the database")
        except Error as e:
            messagebox.showerror("Database Connection Error", str(e))
            print(f"Error: {e}")

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Hash the password for comparison
        hashed_password = self.hash_password(password)

        try:
            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM users WHERE Username = %s AND PasswordHash = %s"
            self.cursor.execute(query, (username, hashed_password))
            user = self.cursor.fetchone()

            if user:
                # Store current user's ID for later use
                self.current_user_id = user['UserID']
                self.create_dashboard()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Error as e:
            messagebox.showerror("Database Error", str(e))

    def create_register_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Register", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            password = password_entry.get()
            
            try:
                # Check if username already exists
                check_query = "SELECT * FROM users WHERE Username = %s"
                self.cursor.execute(check_query, (username,))
                existing_user = self.cursor.fetchone()

                if existing_user:
                    messagebox.showerror("Error", "Username already exists.")
                    return

                # Hash the password
                hashed_password = self.hash_password(password)

                # Insert new user
                insert_query = "INSERT INTO users (Username, PasswordHash) VALUES (%s, %s)"
                self.cursor.execute(insert_query, (username, hashed_password))
                self.connection.commit()

                messagebox.showinfo("Success", "Registration successful!")
                self.create_login_screen()

            except Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Button(self.root, text="Submit", font=("Arial", 12), command=submit).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def __del__(self):
        # Ensure database connection is closed when object is deleted
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    def create_forgot_password_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Forgot Password", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        def send_verification_code():
            username = username_entry.get()
            try:
                # Check if username exists
                query = "SELECT UserID FROM users WHERE Username = %s"
                self.cursor.execute(query, (username,))
                user = self.cursor.fetchone()

                if not user:
                    messagebox.showerror("Error", "Username not found.")
                    return

                # Generate verification code
                code = f"{random.randint(000, 999):03d}"
                
                # Update user's verification code in database
                update_query = "UPDATE users SET VerificationCode = %s WHERE Username = %s"
                self.cursor.execute(update_query, (code, username))
                self.connection.commit()

                messagebox.showinfo("Verification Code", f"Your verification code is: {code}")
                self.show_code_and_reset_screen(username)

            except Error as e:
                messagebox.showerror("Database Error", str(e))

        def submit():
            username = username_entry.get()
            code = code_entry.get()
            new_password = new_password_entry.get()
            
            try:
                # Verify code and update password
                query = "SELECT * FROM users WHERE Username = %s AND VerificationCode = %s"
                self.cursor.execute(query, (username, code))
                user = self.cursor.fetchone()

                if not user:
                    messagebox.showerror("Error", "Incorrect verification code.")
                    return

                # Hash new password
                hashed_password = self.hash_password(new_password)

                # Update password
                update_query = "UPDATE users SET PasswordHash = %s, VerificationCode = NULL WHERE Username = %s"
                self.cursor.execute(update_query, (hashed_password, username))
                self.connection.commit()

                messagebox.showinfo("Success", "Password updated successfully!")
                self.create_login_screen()

            except Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Label(self.root, text="Verification Code:", font=("Arial", 12)).pack(pady=5)
        code_entry = tk.Entry(self.root, font=("Arial", 12))
        code_entry.pack(pady=5)

        tk.Label(self.root, text="New Password:", font=("Arial", 12)).pack(pady=5)
        new_password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        new_password_entry.pack(pady=5)

        tk.Button(self.root, text="Send Verification Code", font=("Arial", 12), command=send_verification_code).pack(pady=15)
        tk.Button(self.root, text="Submit", font=("Arial", 12), command=submit).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def create_delete_account_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Delete Account", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        def send_verification_code():
            username = username_entry.get()
            try:
                # Check if username exists
                query = "SELECT UserID FROM users WHERE Username = %s"
                self.cursor.execute(query, (username,))
                user = self.cursor.fetchone()

                if not user:
                    messagebox.showerror("Error", "Username not found.")
                    return

                # Generate verification code
                code = f"{random.randint(100, 999):03d}"
                
                # Update user's verification code in database
                update_query = "UPDATE users SET VerificationCode = %s WHERE Username = %s"
                self.cursor.execute(update_query, (code, username))
                self.connection.commit()

                messagebox.showinfo("Verification Code", f"Your verification code is: {code}")
                self.show_delete_confirm_screen(username)

            except Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Label(self.root, text="Verification Code:", font=("Arial", 12)).pack(pady=5)
        code_entry = tk.Entry(self.root, font=("Arial", 12))
        code_entry.pack(pady=5)

        tk.Button(self.root, text="Send Verification Code", font=("Arial", 12), command=send_verification_code).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def show_delete_confirm_screen(self, username):
        self.clear_screen()

        tk.Label(self.root, text=f"Do you confirm to delete the '{username}' account?", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=5)

        def confirm():
            password = password_entry.get()
            
            try:
                # Verify password
                query = "SELECT * FROM users WHERE Username = %s AND PasswordHash = %s"
                self.cursor.execute(query, (username, self.hash_password(password)))
                user = self.cursor.fetchone()

                if not user:
                    messagebox.showerror("Error", "Incorrect password.")
                    return

                # Delete user account
                delete_query = "DELETE FROM users WHERE Username = %s"
                self.cursor.execute(delete_query, (username,))
                self.connection.commit()

                messagebox.showinfo("Success", "Account deleted successfully!")
                self.create_login_screen()

            except Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Button(self.root, text="Confirm", font=("Arial", 12), command=confirm).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def create_dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text="WELCOME TO FACTIFY!", font=("Arial", 30, "bold")).pack(pady=25)

        tk.Button(self.root, text="Generate a Fact", font=("Arial", 18), command=self.generate_fact).pack(pady=15)
        tk.Button(self.root, text="Add a Fact", font=("Arial", 18), command=self.create_add_fact_screen).pack(pady=15)
        tk.Button(self.root, text="View Favorites", font=("Arial", 18), command=self.view_favorites).pack(pady=15)
        tk.Button(self.root, text="Logout", font=("Arial", 18), command=self.create_login_screen).pack(pady=15)

    def create_add_fact_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Add a Fact", font=("Arial", 24, "bold")).pack(pady=20)

        fact_entry = tk.Entry(self.root, font=("Arial", 12), width=50)
        fact_entry.pack(pady=10)

        def add_fact():
            fact = fact_entry.get()
            if fact:
                try:
                    # Insert fact into database
                    query = "INSERT INTO facts (FactText, CreatedBy) VALUES (%s, %s)"
                    self.cursor.execute(query, (fact, self.current_user_id))
                    self.connection.commit()

                    messagebox.showinfo("Success", "Fact added successfully!")
                    fact_entry.delete(0, tk.END)
                except Error as e:
                    messagebox.showerror("Database Error", str(e))

        tk.Button(self.root, text="Add Fact", font=("Arial", 12), command=add_fact).pack(pady=10)
        tk.Button(self.root, text="HOME", font=("Arial", 12), command=self.create_dashboard).pack(pady=10)

    def generate_fact(self):
        try:
            # Fetch facts from database
            query = "SELECT FactID, FactText FROM facts"
            self.cursor.execute(query)
            facts = self.cursor.fetchall()

            if not facts:
                messagebox.showinfo("Info", "No facts available. Add some facts first!")
                return

            # Randomly select a fact
            fact = random.choice(facts)
            self.show_fact_screen(fact)

        except Error as e:
            messagebox.showerror("Database Error", str(e))

    def show_fact_screen(self, fact):
        self.clear_screen()

        tk.Label(self.root, text="Fact", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text=fact['FactText'], font=("Arial", 14), wraplength=600, justify="center").pack(pady=20)

        tk.Label(self.root, text="How high do you rate this FACT?", font=("Arial", 12)).pack(pady=10)

        stars_frame = tk.Frame(self.root)
        stars_frame.pack(pady=10)

        def rate(star):
            try:
                # Insert or update rating
                query = "INSERT INTO ratings (UserID, FactID, RatingValue) VALUES (%s, %s, %s) " \
                        "ON DUPLICATE KEY UPDATE RatingValue = %s"
                self.cursor.execute(query, (self.current_user_id, fact['FactID'], star, star))
                self.connection.commit()
                messagebox.showinfo("Rating", f"You rated this fact {star} star(s)")
            except Error as e:
                messagebox.showerror("Database Error", str(e))

        for i in range(1, 6):
            star_button = tk.Button(stars_frame, text="★", font=("Arial", 16), command=lambda i=i: rate(i))
            star_button.grid(row=0, column=i - 1, padx=5)

        def add_to_favorites():
            try:
                # Check if already in favorites
                check_query = "SELECT * FROM favorites WHERE UserID = %s AND FactID = %s"
                self.cursor.execute(check_query, (self.current_user_id, fact['FactID']))
                existing = self.cursor.fetchone()

                if existing:
                    messagebox.showinfo("Info", "This fact is already in your favorites.")
                    return

                # Add to favorites
                query = "INSERT INTO favorites (UserID, FactID) VALUES (%s, %s)"
                self.cursor.execute(query, (self.current_user_id, fact['FactID']))
                self.connection.commit()
                messagebox.showinfo("Success", "Fact added to favorites!")
            except Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Button(self.root, text="Add to Favorites", font=("Arial", 12), command=add_to_favorites).pack(pady=15)
        tk.Button(self.root, text="HOME", font=("Arial", 12), command=self.create_dashboard).pack(pady=20)

    def view_favorites(self):
        self.clear_screen()

        try:
            # Fetch user's favorite facts
            query = """
            SELECT f.FactText 
            FROM favorites fav 
            JOIN facts f ON fav.FactID = f.FactID 
            WHERE fav.UserID = %s
            """
            self.cursor.execute(query, (self.current_user_id,))
            favorites = self.cursor.fetchall()

            tk.Label(self.root, text="My Favorites", font=("Arial", 24, "bold")).pack(pady=20)

            if not favorites:
                tk.Label(self.root, text="No favorite facts yet!", font=("Arial", 14)).pack(pady=20)
            else:
                # Create a frame with scrollbar for favorites
                frame = tk.Frame(self.root)
                frame.pack(pady=20, expand=True, fill=tk.BOTH)

                scrollbar = tk.Scrollbar(frame)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 12), width=50)
                listbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

                scrollbar.config(command=listbox.yview)

                for fact in favorites:
                    listbox.insert(tk.END, fact['FactText'])

            tk.Button(self.root, text="HOME", font=("Arial", 12), command=self.create_dashboard).pack(pady=20)

        except Error as e:
            messagebox.showerror("Database Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
