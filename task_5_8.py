def string_revert(string):
    return ' '.join(string[::-1])


if __name__ == '__main__':
    print(string_revert(input('Enter some words: ').split(' ')))
