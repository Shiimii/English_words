import os
import choose_word

# choose a word
topic, level = choose_word.choose_word()
print(f"https://ejje.weblio.jp/content/{topic}")
line = input(f"Topic is {topic} (level {level}).\n")

file = f'.\words\{topic}.md'
if not os.path.exists(file):
    with open(file, 'w', encoding='UTF-8') as file:
        file.write(f'# {topic} (level {level})\n')
        file.write(line)
else:
    print("Exists")
    