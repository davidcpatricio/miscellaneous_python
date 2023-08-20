def arithmetic_arranger(problems, show_results=False):
    first_row = ""
    second_row = ""
    lines = ""
    results = ""
    length = 0
    arranged_problems = ""

    if len(problems) > 4:
        return "Error: Too many problems."

    for problem in problems:
        if len(problem.split()) != 3:
            return "Error: Invalid problem."

        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]

        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in "+-" or len(operator) != 1:
            if operator in '*/':
                return "Invalid operator."
            else:
                return "Error: Operator must be '+' or '-'."

        length = (max(len(first_number), len(second_number)) + 2)

        if operator == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)

        first_row += ' ' * (length - len(first_number)) + first_number
        second_row += operator + ' ' * (length - len(second_number) - 1) \
            + second_number
        lines += '-' * length
        results += ' ' * (length - len(str(result))) + str(result)

        if problem != problems[-1]:
            first_row += '    '
            second_row += '    '
            lines += '    '
            results += '    '

    if show_results:
        arranged_problems = first_row + "\n" + second_row + "\n" + lines \
            + "\n" + results
    else:
        arranged_problems = first_row + "\n" + second_row + "\n" + lines

    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],
                          True))
