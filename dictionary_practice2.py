def emoji_converter(msg):
    split_msg = msg.split(' ')
    emojis = {
        ':)' : "🙂",
        ":(" : "😥"
    }

    output = ''
    for word in split_msg:
        output += (emojis.get(word, word) + " ")
    return output

msg = input(">")
print(emoji_converter(msg))