# This is the main function of the Bill Splitter program.
def main():
    # Prompt the user for the number of friends joining the dinner, including the user.
    print('Enter the number of friends joining (including you):')
    how_many = int(input())  # Capture the number of friends as an integer.
    dict_list = {}  # Initialize an empty dictionary to store friends' names and their bill shares.

    # Check if the number of friends is less than 1 (invalid input).
    if how_many < 1:
        print('No one is joining for the party')  # Print a message for invalid input.
    else:
        # Prompt for the names of each friend joining the dinner.
        print('Enter the name of every friend (including you), each on a new line:')
        for _ in range(how_many):
            name = input()  # Capture each friend's name.
            dict_list[name] = 0  # Initialize their bill share to 0 in the dictionary.

        # Prompt for the total bill value.
        print('Enter the total bill value:')
        total_bill = float(input())  # Capture the total bill value as a float.

        # Calculate the split amount and round it to two decimal places.
        split_amount = round(total_bill / how_many, 2)

        # Update the dictionary with the split values.
        for name in dict_list:
            dict_list[name] = split_amount  # Assign the split amount to each friend.

        # Print the updated dictionary.
        print(dict_list)


if __name__ == '__main__':
    main()
