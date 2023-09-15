def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


should_continue = True
should_continue_values = True


operations = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}


def calc():
    for signs in operations:
        if symbol == signs:
            answer = operations[symbol]
            return answer(f_num, s_num)


while should_continue:
    user_choice2 = input("would you like to use calculator? yes or no").lower()
    if user_choice2 == "yes":
        f_num = int(input("input first number: "))
        symbol = input("which operation would you use (+, - , /,  * ) ")
        s_num = int(input("input next number: "))
        container = calc()
        print(f"{f_num} {symbol} {s_num} = {container}")

        while should_continue_values:
            user_choice = input("would you like to continue with the same values? yes or no  ").lower()
            if user_choice == 'yes':
                f_num = container
                symbol = input("which operation would you use (+, - , /,  * ) ")
                s_num = int(input("input next number: "))
                print(f"{f_num} {symbol} {s_num} = {calc()}")
                container = calc()
            else:
                should_continue_values = False
        should_continue_values = True
    else:
        should_continue = False
