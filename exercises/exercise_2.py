


math_input = int(input("Please enter your maths mark:  "))
chemistry_input = int(input("Please enter your chemistry mark:  "))
physics_input = int(input("Please enter your physics mark:  "))


def calculate_grade(math_grade,chem_grade,phy_grade):
    results = ((math_grade +chem_grade +phy_grade) / 3)
    gradestr = ""
    if results > 70:
        gradestr = "A"
    elif results > 60:
        gradestr = "B"
    elif results > 50:
        gradestr = "C"
    elif results > 40:
        gradestr = "D"
    
    else:
        gradestr = "FAIL"

    endstr = "Your Percentage Score is : " + str(results)
    gradestr = "You Scored a grade of : " + gradestr

    print(endstr)
    print(gradestr)


        
calculate_grade(math_input,chemistry_input,physics_input)
