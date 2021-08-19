# official link: https://github.com/nailyav/ssad/edit/main/program/main.py

s = input()[::-1].lower()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in s:
    print(str(alph.index(letter) + 1), end=' ', flush=True)
