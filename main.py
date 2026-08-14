#!/usr/bin/env python3

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please enter a numeric value.")


def main():
    nums = []
    for i in range(1, 4):
        n = read_number(f"Enter number {i}: ")
        nums.append(n)

    print("\nYou entered:", nums)
    print(f"Sum: {sum(nums)}")
    print(f"Average: {sum(nums) / len(nums)}")


if __name__ == "__main__":
    main()
