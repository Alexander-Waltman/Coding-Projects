def read_filedata(filename):
    """
    Reads in the grade categories, weight, and actual grade from a CSV file in the following format:
    Category Name, Category Weight (as a decimal 0-1), Category Grade (decimal 0-1)

    Parameters:
    filename (type: string) - name of the file to read the data from

    Returns:
    (type: dictionary) - {str: (float, float)} representing {category: (weight, grade)}
    """
    grade_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            line_chunk = line.split(',')
            
            category = line_chunk[0]
            weight = float(line_chunk[1])
            grade = float(eval(line_chunk[2]))

            grade_dict[category] = (weight, grade)
    
    return grade_dict

def get_final_grade(grade_dict):
    """
    Calculates the final grade based on a grade dictionary in the following format
    key: category name as a string
    value: tuple of category weight and grade

    Parameters:
    grade_dict (type: dictionary) - dictionary of grade categories

    Returns:
    (type: float) - final grade as a decimal 0-1
    """
    final_grade = 0
    for weight, grade in grade_dict.values():
        final_grade += (weight * grade)
    
    return final_grade

def main():
    filename = input("Input filname: ")
    current_grade = get_final_grade(read_filedata(filename))
    print(f"Withought completing any other assignements, your final grade would be {(current_grade * 100):.2f}%")

    final_weight = float(input("How much is your final worth? (0-1)? "))
    target_grade = float(input("What final grade do you want in the class? (0-1) "))

    grade_needed = (target_grade - current_grade)/final_weight

    print(f"You need {(grade_needed * 100):.2f}% on the final to get a {target_grade * 100}% in the class.")

if __name__ == "__main__":
    main()