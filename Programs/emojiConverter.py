message=input("Enter a text with Emoji >> ")
words=message.split(' ')
emoji_Conv_Dict={
    ":)": "😊",
    ":(":"🤔",
    ":-D":"😁"
}
output=""
for word in words:
    output+=emoji_Conv_Dict.get(word,word)+" "
print(output)