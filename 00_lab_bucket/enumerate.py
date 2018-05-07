# ----- python's in-built .enumerate() ----- #

classes = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

for i, c in enumerate(classes):
    print(f"{i}: {c} python")


## less readable, but common structure in other languages:
# for i in range(len(courses)):
#     print(f"{i}: {courses[i]} python")