#START
def ascending_my(num1: int, num2: int):
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
    print("--------------------")


def details_my(string: str):
    first_char = string[0]
    last_char = string[-1]
    middle_index = len(string) // 2
    middle_char = string[middle_index]

    print(f"The first letter is: {first_char}")
    print(f"The middle letter is: {middle_char}")
    print(f"The last letter is: {last_char}")
    print("--------------------")

def bool_say(bool_text: bool):
    if bool_text is True:
        print("Yes")
    else:
        print("No")
    print("--------------------")


def zugi_print(numbers: list[int]):
    for num in numbers:
        if num % 2 == 0:
            print("even", end=", ")
        else:
            print("odd", end=", ")
    print("--------------------")


def statistics_my(grades: list[int]):
    print(" ")
    print(f"The highest score is: {max(grades)}.")
    print(f"The lowest score is: {min(grades)}")
    print(f"The number of grades is: {len(grades)}")
    print(f"The grade point average is: {sum(grades) / len(grades)}")
    print("--------------------")

if __name__ == '__main__':

    ascending_my(-12, 7)
    details_my("AI is the best")
    bool_say(True)
    bool_say(False)
    zugi_print([14, 14, 15, 10, 2, 3, 5])

    grades: list[int] = []

    while True:
        try:
            grade: int = int(input("Enter a grade( Enter a -99 for stop ):"))

            if grade == -99:
                break

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Invalid score. A enter between 0 and 100.")

        except ValueError:
            print("A valid number must be entered.")

    statistics_my(grades)

#END