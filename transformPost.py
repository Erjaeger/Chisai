import os
entries = os.listdir('./posts')

# originDoc = open("./src/posts/cadeaux-pour-noel.html",
#                  "r", encoding='utf-8')
# originDoc = open("./src/newposts/cadeaux-pour-noel.html",
#                  "r", encoding='utf-8')
# finalDoc = open("./src/newposts/cadeaux-pour-noel2.html",
#                 "w", encoding='utf-8')

# lines = originDoc.read()
# print(lines)

for e in entries:
    e = e.split('.')[0]

    os.system(
        f'pandoc %cd%\posts\{e}.html -f html -t markdown -s -o %cd%\posts\{e}.md')

print(os.system('dir'))
# print(entries)
