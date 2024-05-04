# write your code here
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

        # Print the dictionary containing friends' names with their initial bill share set to 0.
        print(dict_list)


if __name__ == '__main__':
    main()
