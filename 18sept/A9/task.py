# thoughts = input("Enter your thoughts: ")
# with open("diary.txt", "w") as file:
#     file.write(thoughts)
#     print("Your thoughts have been saved to diary.txt")
# with open("diary.txt", "r") as file:
#     print(file.read())

with open("score.txt", "w") as file:
    file.write("Alice: 95\nBob: 87 \nCarol: 92")
scores = {}
with open("score.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(":")
        scores[name] = score
print("Current high score: ")
for i, (name, score) in enumerate(sorted(scores.items(), reverse=True), 1):
    print(f"{i}. {name}: {score}")
new_name = input("Enter new name: ")
new_score = int(input("Enter score: "))
scores[new_name] = new_score
print("Updated high score: ")
for i, (name, score) in enumerate(sorted(scores.items(), reverse=True), 1):
    print(f"{i}. {name}: {score}")
with open("score.txt", "w") as file:
    for name, score in scores.items():
        file.write(f"{name}:{score}\n")
with open("score.txt", "r") as file:
    print(file.read())
