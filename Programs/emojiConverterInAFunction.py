def emojiConv(message):
    emojiConvDict = {
        ":)": "😊",
        ":(": "😒"
    }
    words = message.split(' ')
    output = ""
    for word in words:
        output += emojiConvDict.get(word, word) + " "
    return output


print(emojiConv("Hi Hello Happy Face :)"))
print(emojiConv("Hi Hello Sad Face :("))
print(emojiConv("Hi Hello Laugh Face :-D"))
