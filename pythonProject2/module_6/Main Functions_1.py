# def main():
#     print("Hello World!")
#
# if __name__ == "__main__":
#     main()

# from time import sleep
#
# print("This is my file to demonstrate best practices")
#
# def process_data(data):
#     print("Beginning data processing")
#     modified_data = data + " that has been modified"
#     sleep(3) # simulates a time delay of 3 seconds
#     print("Data processing finished")
#     return modified_data
#
# result = process_data("1,2,3,4,5")
# print("modified_data:", result)
# python3 best_practices.py


from time import sleep

print("This is my file to demonstrate best practices.")
# Step 3
def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data
# Step 2
def main(): # when calling the main function
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data) # this is where process_data is called
    print(modified_data) # Step 4: back to here print the modified_data

# Step 1
if __name__ == "__main__":  # this is calling the main function
    main()
