#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = list(word)
    start = 0
    end = -1

    for i in range(len(word)//2):
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

#comment to commit
#YOUR CODE GOES HERE


user_input = input().strip()
user_input = "".join(user_input.split())

if len(user_input) > 0:
    print(palindrome(user_input.lower()))