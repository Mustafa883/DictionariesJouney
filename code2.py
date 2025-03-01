print("Part2.")
def countwords():
    wordscounted = {

    }
    while True:
        fruits = input("Enter your favorite type of fruits: ")
        if fruits.lower() == 'done':
            break
        words = fruits.lower().split()
        for word in words:
            if word in wordscounted:
                wordscounted[word] += 1
            else:
                wordscounted[word] = 1
    print(wordscounted)