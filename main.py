# main.py
# Main file for the ARMS Data API Tester & Explorer application

import sys
from modules import state, year, surveydata, category, report, variable, farmtype

def main_menu():
    """
    Displays the main menu of the application.
    """
    print("\nARMS Data API Tester & Explorer")
    print("--------------------------------")
    print("1: Test /arms/state Endpoint")
    print("2: Test /arms/year Endpoint")
    print("3: Test /arms/surveydata Endpoint")
    print("4: Test /arms/category Endpoint")
    print("5: Test /arms/report Endpoint")
    print("6: Test /arms/variable Endpoint")
    print("7: Test /arms/farmtype Endpoint")
    print("0: Exit")
    print("--------------------------------")
    
    choice = input("Enter your choice: ")
    return choice

def execute_choice(choice):
    """
    Executes the selected choice from the main menu.
    """
    if choice == "1":
        state.test_state_endpoint()
    elif choice == "2":
        year.test_year_endpoint()
    elif choice == "3":
        surveydata.test_surveydata_endpoint()
    elif choice == "4":
        category.test_category_endpoint()
    elif choice == "5":
        report.test_report_endpoint()
    elif choice == "6":
        variable.test_variable_endpoint()
    elif choice == "7":
        farmtype.test_farmtype_endpoint()
    elif choice == "0":
        sys.exit("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        choice = main_menu()
        execute_choice(choice)

if __name__ == "__main__":
    main()