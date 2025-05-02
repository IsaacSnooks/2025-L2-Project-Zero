# Functions go here
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answer=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answer:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answer}")

    # Main routine goes here
    # payment_list = ['cash', 'credit']

    while True:
        want_instructions = string_check("Do you want instructions? ")
        print(f"you chose {want_instructions}")
        print()

    #   pay_method = string_check("Payment Method: ", payment_list, 2)
    #   print(f"You chose {pay_method}")


def instructions():
    make_statement("Instructions", "❕")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), the 
program will display the ticket sales information and write the data to a text file.

It will also coose one lucky ticket holder who wins the draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")


def int_check(question):
    """Checks users enter an integer between 2 values"""

    error = f"Oops - please enter an integer"

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine starts here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialise variables / non-default options for string checker
payment_list = ['cash', 'credit']

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    # ask user for their name (and check it's not blank
    print()
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"Sorry, {name} is too young for this movie")
        continue
    elif age > 120:
        print(f"Sorry, {name} is too old for this movie")
        continue
    else:
        pass

    # ask use for payment method(cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_list, 2)
    print(f"{name} has bought a ticket ({pay_method})")


    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets")
