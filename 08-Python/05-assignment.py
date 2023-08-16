def get_list_of_wagons():
    input_string = input('Enter the wagon IDs separated by space: ')
    print("\n")
    user_list = input_string.split()
    # PRINT LIST
    print('Wagon IDs: ', user_list)

    # CONVERT ITEM TO INT TYPE
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = int(user_list[i])
        
def fix_list_of_wagons():
    input_string = input('Enter the wagon IDs separated by space: ')
    input_string2 = input('Enter the wagon IDs separated by space: ')
    modified_string = input_string.append(input_string2)
    
    print("Original Wagon List: " + str(input_string))
    # print("Modified Wagon List: " + str(input_string2))
    print(modified_string)




fix_list_of_wagons()