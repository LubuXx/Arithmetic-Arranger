def arithmetic_arranger(problems, show_answer = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_section = []
    bottom_section = []
    line_section = []
    answer_section = []

    for problem in problems:
        parts = problem.split()
        first = parts[0]
        operator = parts[1]
        second = parts[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not(first.isdigit() and second.isdigit()):
            return "Error: The numbers must only contain digits."
        
        if len(first) > 4 or len(second) > 4:
            return "Error: The numbers can not more than four digits."
        
        if operator == "+":
            answer = str(int(first) + int(second))

        else:
            answer = str(int(first) - int(second))

        max_length = max(len(first), len(second)) + 2
        top_section.append(first.rjust(max_length))
        bottom_section.append(operator + " " + second.rjust(max_length - 2))
        line_section.append("-" * max_length)
        answer_section.append(answer.rjust(max_length))

    arranged_problems = ""

    if top_section:
        arranged_problems += "    ".join(top_section) + "\n"

    if bottom_section:
        arranged_problems += "    ".join(bottom_section) + "\n"

    if line_section:
        arranged_problems += "    ".join(line_section)

    if show_answer:
        if answer_section:
            arranged_problems += "\n" + "    ".join(answer_section)

    return arranged_problems

# Examples:
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
