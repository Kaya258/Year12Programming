def accounts(stored_userID, stored_pin):
    attempts = 3
    while attempts > 0:
        input_stored_userID = input("Please enter your user ID: ")
        if input_stored_userID == 10:
            print("Correct user ID: ")
        else:
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left. ")
            else:
                print("Incorrect, please try again")
        attempts = 0
        max_attempts = 1
        while attempts < max_attempts:
            input_stored_pin = int(input("Pleas enter your 4 digit pin. "))
            if input_stored_pin == stored_pin:
                print("Correct. ")
            return
            
            else:
                print("Incorrect pin")
            



