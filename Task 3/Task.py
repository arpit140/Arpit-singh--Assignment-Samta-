
# We are using recursion here to  generate Fibonacci numbers.

def generate_fibonacci(n):

    if n<= 0:
        return []

    elif n ==1:
        return[0]

    elif n==2:
        return[0,1]
    else:
        seq= generate_fibonacci(n-1)
        seq.append(seq[-1]+ seq[-2])
        return seq    

if __name__ == "__main__":

    try:
        n = int(input("Enter the number of terms: "))
        if n <=0:
            print("Please enter a postive number")
        
        else:
            fibonacci_seq = generate_fibonacci(n)
            print("Fibonacci sequence up to", n, "terms:")
            print(fibonacci_seq)

    except ValueError:
        print("Please enter a valid integer.")