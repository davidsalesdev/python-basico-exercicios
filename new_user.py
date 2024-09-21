def new_user():
      confirm = "N"
      while confirm != "Y":
            username = str(input("Enter the name of the user: "))
            print("Use the username '" + username + "'? (Y/N)")
            confirm = str(input("")).upper()
            os.system("sudo adduser " + username)