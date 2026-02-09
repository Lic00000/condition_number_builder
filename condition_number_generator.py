# build all combinations of 0s and 1s that are 3 digits long

def build(digits):
    print(digits)

    if len(digits) == 3:
        return

    for d in range(2):
        digits.append(d)
        build(digits)
        digits.pop()

#build([])


# The same thing but the number can't start with 0

def build(digits):
    print(digits)

    if len(digits) == 3:
        return

    for d in range(3):
        if len(digits) == 0 and d == 0:
            continue

        digits.append(d)
        build(digits)
        digits.pop()

#build([])


# Same as first but digits dont appear more than twice, only using digits 0-3

def build(digits, counts):
    print(digits)

    if len(digits) == 3:
        return

    for d in range(4):

        if counts[d] == 2:
            continue

        digits.append(d)
        counts[d] += 1

        build(digits, counts)

        digits.pop()
        counts[d] -= 1


counts = [0,0,0,0]
#build([], counts)

# same as before but now turning lists into actual 3-digit integers with no zero at start

def build(digits, counts):
    if len(digits) == 3:
        n = int("".join(map(str, digits)))
        print(n)
        

    if len(digits) == 3:
        return

    for d in range(4):
        if len(digits) == 0 and d == 0:
            continue

        if counts[d] == 2:
            continue

        digits.append(d)
        counts[d] += 1

        build(digits, counts)

        digits.pop()
        counts[d] -= 1


counts = [0,0,0,0]
#build([], counts)


# same as before but now numbers must be divisible by 18, sum of squared digits is divisible by 9 and reversed number is greater than original, also all digits 0-9 available

results = []

def build(digits, counts, digit_sum):
    if len(digits) > 0:
        if digit_sum % 9 == 0:
            n = int("".join(map(str, digits)))
            if n % 18 == 0:
                reversed_n = int("".join(map(str, digits[::-1])))
                if reversed_n > n:
                    results.append(n)

    if len(digits) == 6:
        return

    for d in range(10):
        if len(digits) == 0 and d == 0:
            continue

        if counts[d] == 2:
            continue

        digits.append(d)
        counts[d] += 1

        build(digits, counts, digit_sum + (d**2))

        digits.pop()
        counts[d] -= 1


counts = [0] * 10
build([], counts, 0)
#print(f"Total numbers found: {len(results)}")
#print("First 20 numbers:", results[:20])


# Builds numbers that are maximum 6 digits long (shorter don't get put into results because they dont pass the conditions), digits appear no more than twice and are greater than their reverse.

results = []

MAX_LENGTH = 6

def build(digits, counts, digit_sum):
    if len(digits) > 0:
        if digit_sum % 9 == 0:
            n = int("".join(map(str, digits)))
            reversed_n = int("".join(map(str, digits[::-1])))
            if n > reversed_n:
                results.append(n)

    if len(digits) == MAX_LENGTH:
        return

    for d in range(10):
        if len(digits) == 0 and d == 0:
            continue
        if counts[d] == 2:
            continue

        counts[d] += 1
        digits.append(d)

        build(digits, counts, digit_sum + d)

        digits.pop()
        counts[d] -= 1


counts = [0] * 10
#build([], counts, 0)

#print(f"Total numbers found: {len(results)}")
#print("First 20 numbers:", results[:20])