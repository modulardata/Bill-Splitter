import random

print('Enter the number of friends joining (including you):')
how_many = int(input())
dict_list = {}

if how_many < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(how_many):
        name = input()
        dict_list[name] = 0

    print('Enter the total bill value:')
    total_bill = float(input())

    # Ask the user if they want to use the "Who is lucky?" feature
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    use_lucky_feature = input()

    if use_lucky_feature.lower() == 'yes':
        lucky_one = random.choice(list(dict_list.keys()))
        print(f'{lucky_one} is the lucky one!')

        # Calculate the split amount for n-1 people
        if how_many > 1:
            split_amount = round(total_bill / (how_many - 1), 2)
        else:
            split_amount = 0

        # Update the dictionary with the split values and 0 for the lucky person
        for name in dict_list:
            if name == lucky_one:
                dict_list[name] = 0
            else:
                dict_list[name] = split_amount
    else:
        print('No one is going to be lucky')
        # Calculate the split amount and round it to two decimal places
        split_amount = round(total_bill / how_many, 2)

        # Update the dictionary with the split values
        for name in dict_list:
            dict_list[name] = split_amount

    # Print the updated dictionary
    print(dict_list)
