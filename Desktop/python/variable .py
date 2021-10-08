number = int(input("Enter a number: "))


def test_range(n):
    if (number % 2) == 0:
     print(" Weird")
    elif(number >20):
     print("Not Weird")

    elif n in range(2,5):
      print( " %s not weird"%str(n))
    elif n in range(6,20):
      print( " %s weird"%str(n))
    
    else:
        print("odd")
test_range(number)






