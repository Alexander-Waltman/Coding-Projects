def test_function(my_func, test_cases):
    """
    Tests if a function has the expected outputs.
    All outputs are printed to the console.
    
    Parameters:
    my_func (type: function) - name of function you are testing
    test_cases (type: list) - list of tuples; the first object in the tuple should be a list of parameters to pass to the function, and the second object should be the expected output
    
    Returns:
    None
    """
    # state and index variables
    success = True
    i = 0

    for pair in test_cases:
        # get a string of all arguments in a test case
        args_list = pair[0]
        args_str = ""
        for arg in args_list:
            # make sure to include quotations marks if argument is meant to be a string
            if type(arg) == str:
                args_str = args_str + f"\"{arg}\"" + ","
            else:
                args_str = args_str + str(arg) + ","

        if args_str[-1] == ",":
            args_str = args_str[:-1]


        # evaluate function with given arguments and check if it equals the expected value
        output = my_func(eval(args_str))
        expected = pair[1]
        if output != expected:
            print(f"test_cases[{i}] failed. Expected {expected} but got {output}")
            success = False
        
        i+=1
    
    if success:
        print("All test cases passed\n\n")

def square(n):
    """
    Return the square of n

    Parameters:
    n (type: float) - number to be squared

    Returns:
    (type: float) - n^2 or n**2
    """
    return n**2

def power(base, expo):
    """
    Raises base to the power of expo

    Parameters:
    base (type: float) - number to raised to a power
    expo (type: float) - power to raise base to

    Returns:
    (type: float) - base^expo or base**expo
    """
    
    return base**expo

def concat(string1, string2, string3):
    """
    Concatenates 3 strings

    Parameters:
    string1-3 (type: string) - one of the 3 strings to be concatenated

    Returns:
    (type: string) - string1 + string2 + string3
    """
    
    return string1 + string2 + string3

def get_user_test_cases():
    """
    Gets the test cases to use within test_function from the user

    Parameters:
    N/A

    Returns:
    (type: list) - a list of test cases in accordance with test_function requirements
    """

    num_cases = int(input("How many test cases would you like to make?\n"))
    test_cases = [] # accumulator variable
    for i in range(num_cases):
        parameters = eval(input("Type out the parameters you want to test as a list.\neg: If you want to test 1 and 2, type \"[1, 2]\"\n"))
        output = eval(input("Type out the expected output:\n"))
        test_cases.append((parameters, output))
    return test_cases

# declaring the various test cases for if the user decides to use the pre-coded ones
sq_test_case1 = ([2], 4)
sq_test_case2 = ([3], 9)
square_test_cases = [sq_test_case1, sq_test_case2]

pw_test_case1 = ([2, 2], 4)
pw_test_case2 = ([5, 3], 125)
power_test_cases = [pw_test_case1, pw_test_case2]

cc_test_case1 = (["hi ", "123", "   ."], "hi 123   .")
cc_test_case2 = (["this ", "is ", "test case 2"], "this is test case 2")
concat_test_cases = [cc_test_case1, cc_test_case2]


if __name__ == "__main__":
    while(True):
        # get which function is being tested
        input1 = input("Which function would you like to test?\n(1) - square\n(2) - power\n(3) - concat\n")
        if input1 == "1":
            func_to_test = square
            cases = square_test_cases
        elif input1 == "2":
            func_to_test = power
            cases = power_test_cases
        else:
            func_to_test = concat
            cases = concat_test_cases
        
        # get which test cases to use
        input2 = input("Would you like to use the pre-coded test cases or make your own?\n(1) - pre-coded\n(2) - my own\n")
        if input2 == "1":
            test_function(func_to_test, cases)
        else:
            print("Some notes about inputs:")
            print("If you are passing a string, you do need to use quotation marks. Type exactly what you would type if it was real code.")

            cases = get_user_test_cases()
            test_function(func_to_test, cases)


