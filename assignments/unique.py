import random

hashtags = [
    '#javascriptdeveloper',
    '#java',
    '#javadeveloper',
    '#coding',
    '#stackoverflow',
    '#googlesearch',
    '#tech',
    '#technology',
    '#backend',
    '#backenddeveloper',
    '#frontenddeveloper',
    '#frontend',
    '#computerengineering',
    '#computerprogramming',
    '#computernetworking',
    '#database',
    '#sql',
    '#sqlserver',
    '#mysql',
    '#php',
    '#phpdeveloper',
    '#nodejs',
    '#cpanel',
    '#softwaredeveloper',
    '#softwareengineer',
    '#softwaredevelopment',
    '#html5',
    '#htmlcss',
    '#css3',
    '#python',
    '#pythonprogramming',
    '#python3',
    '#pythondeveloper',
    '#webdeveloper',
    '#webdesign',
    '#webdevelopment',
    '#webdesigner',
    '#webdev',
    '#webdevelopers',
    '#datascience',
    '#datascientist',
    '#datastructures',
    '#datasecurity',
    '#datastorage',
    '#androiddeveloper',
    '#androidstudio',
    '#androidapps',
    '#iosdeveloper',
    '#android',
    '#ios',
    '#coder',
    '#codelife',
    '#codergirl',
    '#coderlife',
    '#fullstackdeveloper',
    '#fullstack',
    '#javascript',
    '#machinelearning',
    '#ai',
    '#developers',
    '#websitedevelopment',
    '#computerscience',
    '#developerlife',
    '#codeismylife',
    '#peoplewhocode',
    '#coders',
    '#codingdays',
    '#programmingmemes',
    '#programmingjokes',
    '#programminghumor',
    '#programmingisfun',
    '#programmingfacts',
    '#learnprogramming',
    '#javaprogramming',
    '#learntocode',
    '#programmingquotes',
    '#cprogramming',
    '#programmingislife',
    '#programminglife',
    '#programming',
    '#microsoft',
    '#windows10',
    '#angularjs',
    '#reactjs',
    '#vuejs',
    '#dev',
    '#developerslife',
    '#iosdevelopment',
    '#flutter',
    '#databases',
]

print(len(hashtags))

# print(set(hashtags))

def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)

# print(list_duplicates(hashtags))
# print(len(hashtags))
tags_1 = random.sample(hashtags, 30)
print(len(tags_1))
print('------------tags1----------------')
print(','.join(tags_1))
print('check duplicates')
print(list_duplicates(tags_1))
print('------------end->->tags1----------------')

sample_list2 = [item for item in hashtags if item not in tags_1]
tags_2 = random.sample(sample_list2, 30)
print(len(tags_2))
print('------------tags2----------------')
print(','.join(tags_2))
print('check duplicates')
print(list_duplicates(tags_2))

print('------------end->->tags2----------------')

tags_3 = [item for item in sample_list2 if item not in tags_2]
print(len(tags_3))
print('------------tags3----------------')
print(','.join(tags_3))
print('check duplicates')
print(list_duplicates(tags_3))

print('------------end->->tags3----------------')
