with open("Story.txt", "r") as f:
    story=f.read()
target_start="["
target_end="]"
found=False
words=set()
for i, char in enumerate(story):
    if char==target_start:
        start_word=i
        found=True
    if char==target_end and found==True:
        word=story[start_word:i+1]
        words.add(word)
        found=False
answers={}
for word in words:
    answer = input("Enter a word you want to add for "+ word + ": ") 
    answers[word]=answer
for word in words:
    story=story.replace(word,answers[word])
print(story)