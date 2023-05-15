def find_largest_number(numbers):
    if not numbers:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest


# Example usage
number_list = [12, 45, 67, 89, 23, 9]
largest_number = find_largest_number(number_list)
print("The largest number is:", largest_number)
