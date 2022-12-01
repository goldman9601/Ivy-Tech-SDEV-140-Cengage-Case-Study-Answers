def value(string):    
    count = 0
    for num in str(string)[0:]:
        if num.isdigit() and int(num) in range(10):
            count += int(num)

    return count


def main():
    user_input_string = input('Enter a string of single digit numbers with no separation: ')

    print('That string has a total value of: ' + str(value(user_input_string)) + '.')


main()
