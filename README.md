## Password Generator Scrypt 

a script for generating passwords using upper-case letters, lower-case letters, numbers and special characters. 

### Features: 
1. **Manual Save Option**: After generating the password, the user is prompted with a yes/no option to decide if they want to save the password to a file.
2. **Custom File Path**: If the user chooses to save, they can enter a custom file path. If no path is entered, it defaults to <code>password.txt</code>.
3. **No Automatic Save**: The password is only saved if the user chooses to do so.
4. **Error Handling**: There's basic error handling for file saving, printing a message if there's an issue with saving.

### Usage Example:
1. Run the script, and it will generate the password and display it.
2. To run use: <code>python3 genPassword.py</code>
3. You'll be asked if you want to save it. If you type "yes," you'll be prompted for a file path. If you type "no," the password won't be saved.
4. You can specify the desired password length as well.
5. <code>password_length = 16  # You can set this to any length</code>
