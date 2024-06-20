a=str(input())
words=a.split("WUB")
o_word=[word for word in words if word]
o_song=" ".join(o_word)
print(o_song)