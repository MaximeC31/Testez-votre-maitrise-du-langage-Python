words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# result = []
# for word in words:
#     count = 0
#     for letter in word:
#         if letter in "aeiouy":
#             count = count + 1
#     result.append((word, count))

result = [(word, len([c for c in word if c in "aeiouy"])) for word in words]

print(result)
