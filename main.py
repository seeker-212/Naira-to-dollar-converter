def main():
    print("This program convert Naira dollars to dollars")
    print()


    dollars = eval(input("Enter amount in Dollars: "))


    Naira = convert_to_Naira(dollars)

    print("That is", Naira, "Naira.")


convert_to_Naira = lambda dollars: dollars * 1000

main()