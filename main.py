# Grade Calculator
class ColorCodes:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


TestSum = 0.0
count = 0
average = 0.0
TestIteration = 1
Continue = "y" or "yes"

while True:
    # TestScores = float(input("Enter your {}".format(TestIteration) + " Test Score(s): "))
    try:
        TestScores = float(input("Enter your Test Score (#{}): ".format(TestIteration)))
        if (TestScores < 0):
            print("Please only enter positive numbers!!\n")
            continue
        else:
            count += 1
            TestIteration += 1
            TestSum += TestScores
            while Continue != int:
                Continue = input("Would you like to continue entering more Test Scores? ")
                if (Continue.isnumeric() == True):
                    print("Please enter only letters and no numbers/blank values!!\n")
                elif (Continue == ""):
                    print(
                        "Please enter a response [enter 'y'/'yes' to continue or 'n'/'no' to calculate your average]\n")
                elif (Continue == 'n' or Continue == 'N' or Continue == 'no' or Continue == 'No'):
                    average = TestSum/count
                    roundedAverage = round(average)  # Rounds to the nearest whole number
                    # roundedAverage = round(average, 1)  # Rounds to the tenths decimal place
                    print("\nYour Test Score Total is:", TestSum)
                    print("Your Average is:", average)
                    print("Your Rounded Average is:", roundedAverage)
                    if (roundedAverage > 92):
                        print("\n Your Letter Grade if A")
                        input("\nProgram is completed successfully, press 'Enter' to exit")
                        exit()
                    elif (roundedAverage >= 90 and roundedAverage <= 92):
                            print("\nYour Letter Grade is: A-")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 88 and roundedAverage <= 89):
                            print("\nYour Letter Grade is: B+")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 83 and roundedAverage <= 87):
                            print("\nYour Letter Grade is: B")
                            input("\n\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 80 and roundedAverage <= 82):
                            print("\nYour Letter Grade is: B-")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 78 and roundedAverage <= 79):
                            print("\nYour Letter Grade is: C+")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 73 and roundedAverage <= 77):
                            print("\nYour Letter Grade is: C")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 70 and roundedAverage <= 72):
                            print("\nYour Letter Grade is: C-")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage >= 60 and roundedAverage < 70):
                            print("\nYour Letter Grade is: D")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                    elif (roundedAverage < 60):
                            print("\nYour Letter Grade is: F")
                            input("\nProgram is completed successfully, press 'Enter' to exit")
                            exit()
                elif (Continue == 'y' or Continue == 'Y' or Continue == 'yes' or Continue == 'Yes'):
                    break
                else:
                    # If any other letter/words are entered
                    print("Please enter 'y'/'yes' to continue or 'n'/'no' to calculate your average\n")
    except ValueError:
        print("This is not a valid Test Score! Please enter any positive number\n")
