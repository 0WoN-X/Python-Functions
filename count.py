def count_upper(text):
    count = 0

    for char in text:
        if char.isupper():
            count += 1

    return count

print(count_upper("Hello WORLD"))