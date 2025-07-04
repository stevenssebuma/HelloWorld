def gretings(w):
    w = "Hello " + w
    return w

def main():
    print()
    response = input("Welcome to my Hello World program!, Do you want to proceed? (yes/no): ").lower()


    if response == "yes":
        message = gretings("World!")
        print(message)

    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()