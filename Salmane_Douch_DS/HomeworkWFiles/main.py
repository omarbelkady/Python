import homework2
def main():
    data=[]
    cleaned_filename="cleaned_data.txt"
    while True:
        print("\nMenu: ")
        print("1. Start the program (Clean Data)")
        print("2. Print the content of the clean file ")
        print("3. Update Revenue")
        print("4. Sort Companies Alphabetically")
        print("5. Sort Companies By number of Employees")
        print("6. Get information about a company")
        print("7. Quit")
        choice= input("Please enter your choice: ")

        if(choice=="1"):
            homework2.clean_data("true.txt", cleaned_filename)
            print("Data Cleaned and successful")
            data=homework2.load_data(cleaned_filename)
        elif(choice == "2"):
            if not data:
                print("Please launch the program")
            else:
                homework2.print_clean_data(data)
        elif(choice=="3"):
            if not data:
                print("Please launch the program")
            else:
                company=input("Enter company name")
                revenue=float(input("Enter new revenue in billions USD: "))
                homework2.update_revenue(data,company, revenue)
        elif(choice=="4"):
            if not data:
                print("Please launch the program first")
            else:
                homework2.bubble_sort(data)
                print("Companies sorted in alphabetical order")
        elif(choice=="5"):
            if not data:
                print("Please launch the program first")
            else:
                homework2.selection_sort(data)
                print("Companies sorted by employees")
        elif(choice=="6"):
            if not data:
                print("Please launch the program first")
            else:
                company=input("Enter the company name")
                result=homework2.search_for_company(data,company)
                if(result):
                    print(result)
                else:
                    print("Company not found")
        elif(choice=="7"):
            if data:
                homework2.top_3_companies(data)
            print("exit program")
            break
        else:
            print("Invalid choice ")

if __name__=="__main__":
    main()


