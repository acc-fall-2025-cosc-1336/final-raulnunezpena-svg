def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    length = len(dna_string2)

    for i in range(len(dna_string1) - length + 1):
        if dna_string1[i:i + length] == dna_string2:
            positions.append(i + 1)

    return tuple(positions)


def is_valid_dna(s):
    for ch in s:
        if ch not in "ACGT":
            return False
    return True


def main():
    while True:
        while True:
            dna1 = input("Enter a DNA string (>8 and <=16 characters): ").strip().upper()
            if 8 < len(dna1) <= 16 and is_valid_dna(dna1):
                break
            print("Invalid input.")

        while True:
            dna2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
            if len(dna2) == 4 and is_valid_dna(dna2):
                break
            print("Invalid input.")

        result = get_most_likely_ancestor_consensus(dna1, dna2)

        if len(result) == 0:
            print("No occurrences found.")
        else:
            print(*result)

        if input("Run again? (y/n): ").lower() != "y":
            break


main()
