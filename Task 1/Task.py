def calculate_area(length, width):
    if length == width:
        return "This is a sqaure."
    
    else:
        return length * width
    

def main():

    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        result = calculate_area(length, width)
        print(result)
    except ValueError:
        print("Please enter valid numbers")

if __name__ == "__main__":
    main()