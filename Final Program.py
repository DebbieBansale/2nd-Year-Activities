import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from scipy import stats

user_name=input("Type your name: ")
time.sleep(1)
def main():
    print("\n\t\t\t\t\t \U0001f600CORRELATION AND REGRESSION PLOTTER SYSTEM \U0001f600 ")
    print(f"\nWelcome {user_name}, this system is design to COMPUTE, PLOT, AND ASSESS your given or exported data values \n")
    choice_1=input("Type what Analysis do you want to use (C for Correlation or R for Regression): ")
    if choice_1 == "C" or choice_1 == "c":
        time.sleep(1)
        def main_menu():
            print("You have chosen PEARSON Correlation Analysis\n")
            print("Correlation Analysis system is where it measure the strength and direction of the relationship between independent and dependent variable" )
            print("\nPlease choose from the given choices below: ")
            print("(1) Insert Data in this system")
            print("(2) Insert an Excel file on this system ")
            choice_1_a =int(input("type your choice: "))
            if choice_1_a == 1:
                decison_1_a()
            elif choice_1_a == 2:
                decison_1_b()
            else:
                main_menu()
        def decison_1_a():
            print("\n\t\t\tNOTICE!")
            print("\tDo you want to continue? ")
            print("\t\t1. Yes")
            print("\t\t2. Return")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("INSTRUCTION: Please input the ask values.\U0001F609\n")
                x_val_1 = input("Enter the x values (Use comma to seperate the x values): ").split(",")
                y_val_1 = input("Enter the y values (Use comma to seperate the y values): ").split(",")
                x_val_1 = [float(x) for x in x_val_1]
                y_val_1 = [float(y) for y in y_val_1]
                x_square_1 = [x**2 for x in x_val_1]
                y_square_1 = [y**2 for y in y_val_1]
                prod_xy = [x_val_1[i] * y_val_1[i] for i in range(len(x_val_1))]
                table = PrettyTable()
                table.add_column("X", x_val_1)
                table.add_column("Y", y_val_1)
                table.add_column("X^2", x_square_1)
                table.add_column("Y^2", y_square_1)
                table.add_column("XY", prod_xy)
                print(table)
                XS=sum(x_val_1)
                YS=sum(y_val_1)
                YSQR= sum(y_square_1)
                XSQR=sum(x_square_1)
                XYS=sum(prod_xy)
                print(f"Sum of x: {XS}")
                print(f"Sum of y: {YS}")
                print(f"Sum of x^2: {XSQR}")
                print(f"Sum of xy: {XYS}")
                x_value_1= np.array(x_val_1, dtype=float)
                y_value_1= np.array(y_val_1, dtype=float)
                
                corr_coeff_1 = np.corrcoef(x_val_1,y_val_1)[0,1]
                print(f"the Correlation Coefficient(r) is: {corr_coeff_1:.2f} ")
                plt.scatter(x_val_1,y_val_1)
                x_label_1=input("Name of your X-Axis: ")
                y_label_1=input("Name of your Y-Axis: ")
                print("\n\t THE PLOTTED GRAPH: ")
                plt.xlabel(x_label_1)
                plt.ylabel(y_label_1)
                plt.title("Correlational Analysis Graph")
                plt.show()
                
                print("\n\t\t RESULTS: ")
                if corr_coeff_1 > 0:
                    
                    if corr_coeff_1 <= 0.2:
                        print(f"\nThere are No positive Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 <= 0.4:
                        print(f"\nThere is a Low positive Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 <= 0.6:
                        print(f"\nThere is a moderate positive Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 <= 0.89:
                        print(f"\nThere is a High positive Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 <= 0.99:
                        print(f"\nThere is a Very High positive Relationship between the {x_label_1} and {y_label_1}")
                    else:
                        print(f"\nThere is a Perfect positive Relationship between the {x_label_1} and {y_label_1}")
                elif corr_coeff_1 < 0:
                    if corr_coeff_1 >= -0.2:
                        print(f"\nThere are No Negative Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 >= -0.4:
                        print(f"\nThere is a Low Negative Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 >= -0.6:
                        print(f"\nThere is a moderate Negative Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 >= -0.89:
                        print(f"\nThere is a High Negative Relationship between the {x_label_1} and {y_label_1}")
                    elif corr_coeff_1 >= -0.99:
                        print(f"\nThere is a Very High Negative Relationship between the {x_label_1} and {y_label_1}")
                    else:
                        print(f"\nThere is a Perfect Negative Relationship between the {x_label_1} and {y_label_1}")
                else:
                    print(f"\nStrictly No Relationship between the {x_label_1} and {y_label_1}")
            
            elif choice == "2":
                main_menu()
        
        def decison_1_b():
            print("\n\t\t\t\tNOTICE!")
            print("\tDo you want to continue? ")
            print("\t\t1. Yes")
            print("\t\t2. Return")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("INSTRUCTIONS: Please be reminded that your excel file must include the x and y values to make sure that it will read it properly.\U0001F609\n\n ")
                print("Follow this format: ('X VALUES' and 'Y VALUES') in seperated column")
                print(r"EXAMPLE: C:\Users\Matthew\Documents\practice\sample_excel.xlsx")
                excel_input=input("Put the file link: ")
                data_2 = pd.read_excel(excel_input)
                print(data_2)
                
                x_val_2= data_2['X VALUES']
                y_val_2= data_2['Y VALUES']
                x_square_2 = [x**2 for x in x_val_2]
                y_square_2 = [y**2 for y in y_val_2]
                prod_xy = [x_val_2[i] * y_val_2[i] for i in range(len(x_val_2))]
                table = PrettyTable()
                table.add_column("X", x_val_2)
                table.add_column("Y", y_val_2)
                table.add_column("X^2", x_square_2)
                table.add_column("Y^2", y_square_2)
                table.add_column("XY", prod_xy)
                print(table)
                XS=sum(x_val_2)
                YS=sum(y_val_2)
                YSQR= sum(y_square_2)
                XSQR=sum(x_square_2)
                XYS=sum(prod_xy)
                print(f"Sum of x: {XS}")
                print(f"Sum of y: {YS}")
                print(f"Sum of x^2: {XSQR}")
                print(f"Sum of xy: {XYS}")

                corr_coeff_2 = x_val_2.corr(y_val_2)
                print(f"the Correlation Coefficient(r) is: {corr_coeff_2:.2f} ")

                plt.scatter(x_val_2,y_val_2)
                x_label_2=input("Name of your X-Axis: ")
                y_label_2=input("Name of your Y-Axis: ")
                
                print("\n\t THE PLOTTED GRAPH: ")
                plt.xlabel(x_label_2)
                plt.ylabel(y_label_2)
                plt.title("Correlational Analysis Graph")
                plt.show()
                
                print("\n\t\t RESULTS: ")

                if corr_coeff_2 > 0:
                    
                    if corr_coeff_2 <= 0.2:
                        print(f"\nThere are No positive Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 <= 0.4:
                        print(f"\nThere is a Low positive Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 <= 0.6:
                        print(f"\nThere is a moderate positive Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 <= 0.89:
                        print(f"\nThere is a High positive Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 <= 0.99:
                        print(f"\nThere is a Very High positive Relationship between the {x_label_2} and {y_label_2}")
                    else:
                        print(f"\nThere is a Perfect positive Relationship between the {x_label_2} and {y_label_2}")
                elif corr_coeff_2 < 0:
                    if corr_coeff_2 >= -0.2:
                        print(f"\nThere are No Negative Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 >= -0.4:
                        print(f"\nThere is a Low Negative Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 >= -0.6:
                        print(f"\nThere is a moderate Negative Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 >= -0.89:
                        print(f"\nThere is a High Negative Relationship between the {x_label_2} and {y_label_2}")
                    elif corr_coeff_2 >= -0.99:
                        print(f"\nThere is a Very High Negative Relationship between the {x_label_2} and {y_label_2}")
                    else:
                        print(f"\nThere is a Perfect Negative Relationship between the {x_label_2} and {y_label_2}")
                else:
                    print(f"\nStrictly No Relationship between the {x_label_2} and {y_label_2}")
           
            elif choice == "2":
                main_menu()
        main_menu()
        
    elif choice_1 == "R" or choice_1 =="r":
        time.sleep(1)
        def main_menu():
            print("You have chosen SIMPLE LINEAR Regression Analysis\n")
            print("Simple linear regression is a regression model that estimates the relationship between one independent variable and one dependent variable using a straight line.\n")
            print("\nPlease choose from the given choices below: ")
            print("(1) Insert Data in this system")
            print("(2) Insert an Excel file on this system ")
            choice_1_b =int(input("type your choice: "))
            if choice_1_b == 1:
                decison_1_a()
            elif choice_1_b == 2:
                decison_1_b()
            else:
                main_menu()
        def decison_1_a():
            print("\n\t\t\t\tNOTICE!")
            print("\tDo you want to continue? ")
            print("\t\t1. Yes")
            print("\t\t2. Return")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("INSTRUCTION: Please input the ask values.\U0001F609\n")
                x_val_3 = input("Enter the x values (Use comma to seperate the x values): ").split(",")
                y_val_3 = input("Enter the y values (Use comma to seperate the y values): ").split(",")
                num_ob = np.size(x_val_3)
                x_val_3 = [float(x) for x in x_val_3]
                y_val_3 = [float(y) for y in y_val_3]
                x_square_3 = [x**2 for x in x_val_3]
                y_square_3 = [y**2 for y in y_val_3]
                prod_xy_3 = [x_val_3[i] * y_val_3[i] for i in range(len(x_val_3))]
                table = PrettyTable()
                table.add_column("X", x_val_3)
                table.add_column("Y", y_val_3)
                table.add_column("X^2", x_square_3)
                table.add_column("XY", prod_xy_3)
                print(table)
                XS=sum(x_val_3)
                YS=sum(y_val_3)
                YSQR= sum(y_square_3)
                XSQR=sum(x_square_3)
                XYS=sum(prod_xy_3)
                print(f"Sum of x: {XS}")
                print(f"Sum of y: {YS}")
                print(f"Sum of x^2: {XSQR}")
                print(f"Sum of xy: {XYS}")
                
                a_3=((YS)*(XSQR)-(XS)*(XYS))/((num_ob)*(XSQR)-((XS)**2)) 
                print(f"Intercept: {a_3:.2f}")
                b_3= ((num_ob)*(XYS)-(XS)*(YS))/((num_ob)*(XSQR)-((XS)**2))
                print(f"Slope: {b_3:.2f}")
                corr_coeff_3 = np.corrcoef(x_val_3,y_val_3)[0,1]
                r_squared_3 = (corr_coeff_3)**2
                print(f"The equation of regression: y={b_3:.2f}x + {a_3:.2f}")
                print(f"R-squared value: {r_squared_3:.2f}")
                print("\n\t THE PLOTTED GRAPH: ")
                sns.regplot(x_val_3, y_val_3, ci=None)
                sns.regplot(x_val_3,y_val_3)
                x_label_3=input("Name of your X-Axis: ")
                y_label_3=input("Name of your Y-Axis: ")
                plt.xlabel(x_label_3)
                plt.ylabel(y_label_3)
                plt.show()
                
                print("\n\t\t RESULTS: ")
                
                if b_3 > 0:
                    print(f"\nThere is a positive relationship between X and Y. It means that in every one-unit increase in the independent variable, the dependent variable increases by {b_3:.2f} units ")
                elif b_3 < 0:
                    print(f"\nThere is a negative relationship between X and Y. It means that in every one-unit increase in the independent variable, the dependent variable decreases by {b_3:.2f} units ")
                else:
                    print("\nThere is no relationship between X and Y. It means that in every one-unit there is no movement between the independent and dependent variable ")
            elif choice == "2":
                main_menu()
        def decison_1_b():
            print("\n\t\t\t\tNOTICE!")
            print("\tDo you want to continue? ")
            print("\t1. Yes")
            print("\t2. Return")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("INSTRUCTIONS: Please be reminded that your excel file must include the x and y values to make sure that it will read it properly.\U0001F609\n\n ")
                print("Follow this format: ('X VALUES' and 'Y VALUES') in seperated column")
                print(r"EXAMPLE: C:\Users\Matthew\Documents\practice\sample_excel.xlsx")
                excel_input=input("Put the file link: ")
                data_4 = pd.read_excel(excel_input)
                print(data_4)
                
                x_val_4= data_4['X VALUES']
                y_val_4= data_4['Y VALUES']
                num_ob_4 = np.size(x_val_4)
                x_square_4 = [x**2 for x in x_val_4]
                y_square_4 = [y**2 for y in y_val_4]
                prod_xy_4 = [x_val_4[i] * y_val_4[i] for i in range(len(x_val_4))]
                table = PrettyTable()
                table.add_column("X", x_val_4)
                table.add_column("Y", y_val_4)
                table.add_column("X^2", x_square_4)
                table.add_column("XY", prod_xy_4)
                print(table)
                XS_4=sum(x_val_4)
                YS_4=sum(y_val_4)
                YSQR_4= sum(y_square_4)
                XSQR_4=sum(x_square_4)
                XYS_4=sum(prod_xy_4)
                print(f"Sum of x: {XS_4}")
                print(f"Sum of y: {YS_4}")
                print(f"Sum of x^2: {XSQR_4}")
                print(f"Sum of xy: {XYS_4}")
                
                a_4=((YS_4)*(XSQR_4)-(XS_4)*(XYS_4))/((num_ob_4)*(XSQR_4)-((XS_4)**2)) 
                print(f"Intercept: {a_4:.2f}")
                b_4= ((num_ob_4)*(XYS_4)-(XS_4)*(YS_4))/((num_ob_4)*(XSQR_4)-((XS_4)**2))
                print(f"Slope: {b_4:.2f}")
                corr_coeff_4 = np.corrcoef(x_val_4,y_val_4)[0,1]
                r_squared_4 = (corr_coeff_4)**2
                print(f"The equation of regression: y={b_4:.2f}x + {a_4:.2f}")
                print(f"R-squared value: {r_squared_4:.2f}")
                sns.regplot(x_val_4, y_val_4, ci=None)
                sns.regplot(x_val_4,y_val_4)
                x_label_4=input("Name of your X-Axis: ")
                y_label_4=input("Name of your Y-Axis: ")
                print("\n\t THE PLOTTED GRAPH: ")
                plt.xlabel(x_label_4)
                plt.ylabel(y_label_4)
                plt.show()
                
                print("\n\t\t RESULTS: ")
                
                if b_4 > 0:
                    print(f"\nThere is a positive relationship between X and Y. It means that in every one-unit increase in the independent variable, the dependent variable increases by {b_4:.2f} units ")
                elif b_4 < 0:
                    print(f"\nThere is a negative relationship between X and Y. It means that in every one-unit increase in the independent variable, the dependent variable decreases by {b_4:.2f} units ")
                else:
                    print("\nThere is no relationship between X and Y. It means that in every one-unit there is no movement between the independent and dependent variable ")
            elif choice == "2":
                main_menu()
            

        main_menu()
    
    
    else:
        print("\n\t\t Sorry! You have inputted a wrong Choice. Please try again!")
        main()        
    print("\n\t\t\t\t\tCREDITS:\n")
    print("APOLINAR, JONNA")
    print("BANSALE, DEBBIE")
    print("CORDERO, DIEGO EMMANUEL")
    print("GABRIEL, SHEENALYN")
    print("LOS AÑES, VINCENT JERICHO")
    print("PEREGRINO, EMMANUEL")
    print("TORRALBA, MATTHEW EBENEZER")
main()

while True:
    opt = input('Want to do it again? Type Y/y: ')
    option = opt.upper()
    if option != 'Y':
        print("\t\t\t\t\tThank you for using our system \U0001f600 ")
        break
    else:
        main()
    