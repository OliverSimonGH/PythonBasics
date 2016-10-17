twilight_quotes = "About three things I was absolutely positive, First I love chocolate and Second, Edward was a vampire."
# print(twilight_quotes)
twilight_quotes = twilight_quotes.split(" ")

for i in twilight_quotes:
    if len(i) > 4:
        print(i)
    elif "love" or "jacob" in twilight_quotes:
        continue
