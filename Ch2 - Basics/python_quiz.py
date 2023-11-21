def check_input():
  name = input("What is your name?")
  age = input("How old are you?")
  try:
    val = int(age)
  except ValueError:
    print("age is not an int!")

def main():  
  check_input()

if __name__ == __main__:
    main()