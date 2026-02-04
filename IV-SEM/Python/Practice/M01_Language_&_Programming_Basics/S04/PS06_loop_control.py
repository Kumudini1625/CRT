#for i in range(1, 11):
    #if i % 2 == 0:
        #continue
   # print(i, end=' ')


    #username and password validation in loop control statement
correct_username = "Kumudini"
correct_password = "kumudini1625"
for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")            
