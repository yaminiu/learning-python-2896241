#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 10

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is smaller than y, giving me emotional damage!"
    elif x == y:
        result = "x is equal to y"
    else:
        result = "x is greater than y"

    print(result)

    # conditional statements let you use "a if C else b"
    result = "x is greater than y" if x > y else "x is smaller than or equal to y"
    print(result)
    # match-case makes it easy to compare multiple values
    value = "1000000"
    match value:
        case "one" | "two":
            result = (1, 2)
        case "three" | "four":
            result = (3, 4)
        case "five" | "six":
            result = (5, 6)
        case "seven" | "eight" | "nine" | "ten" | "eleven" | "twelve" | "thirteen":
            result = (7, 8, 9, 10, 11, 12, 13)
        case _:
            result = -1
    print(result)

if __name__ == "__main__":
        main()
