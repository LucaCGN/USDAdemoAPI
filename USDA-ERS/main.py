# main.py
import sys
from modules import state, year, surveydata, category, report, variable, farmtype
from utils.endpoint_interaction_handler import handle_endpoint_interaction

# Import for loading variable details and getting options
from modules.variable import load_variable_details, fetch_variable_options
from modules.year import get_year_options
from modules.state import get_state_options
from modules.category import get_category_options
from modules.farmtype import get_farmtype_options

def main_menu():
    """
    Displays the main menu of the application.
    """
    print("\nARMS Data API Tester & Explorer")
    print("--------------------------------")
    print("1: Test /arms/state Endpoint")
    print("2: Test /arms/year Endpoint")
    print("3: Test /arms/surveydata Endpoint with Parameters")
    print("4: Test /arms/category Endpoint")
    print("5: Test /arms/report Endpoint")
    print("6: Test /arms/variable Endpoint with Parameters")
    print("7: Test /arms/farmtype Endpoint")
    print("8: Advanced Query Builder")
    print("0: Exit")
    print("--------------------------------")

    choice = input("Enter your choice: ")
    return choice

def execute_choice(choice, variables_info):
    """
    Executes the selected choice from the main menu.
    """
    if choice == "1":
        handle_endpoint_interaction(get_state_options, state.test_state_endpoint)
    elif choice == "2":
        handle_endpoint_interaction(get_year_options, year.test_year_endpoint)
    elif choice == "3":
        surveydata.handle_surveydata_interaction(variables_info)
    elif choice == "4":
        handle_endpoint_interaction(get_category_options, category.test_category_endpoint)
    elif choice == "5":
        report.test_report_endpoint()
    elif choice == "6":
        handle_endpoint_interaction(fetch_variable_options, variable.test_variable_endpoint)
    elif choice == "7":
        handle_endpoint_interaction(get_farmtype_options, farmtype.test_farmtype_endpoint)
    elif choice == "8":
        print("Advanced Query Builder coming soon...")
    elif choice == "0":
        sys.exit("Exiting the application. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

def main():
    variables_info = load_variable_details("data/arms-all-variables-december-2023.csv")
    while True:
        choice = main_menu()
        execute_choice(choice, variables_info)

if __name__ == "__main__":
    main()
