#!/usr/bin/env python3
"""Print the Collatz sequence starting at 27, then the number of steps to reach 1."""


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    sequence = collatz(27)
    for value in sequence:
        print(value)
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main()
