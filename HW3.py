# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:47:28 2022

@author: kaieu
"""

import string
import collections
from numpy import dot
from numpy.linalg import norm

text1 = "Just watch the movie. I'm not going to say much. It's amazing. And I'm in complete disbelief that it actually happened. Well-made. well-acted. well-directed. Fun, funny and crazy with a ton of heart. Can't wait to watch it again."
text2 = "I enjoyed this movie very much because it had an amazing plot, contained plenty of action scenes and much of suspense. Regarding the plot, there are some plot twists that I did not expect so, it was a nice surprise and something that made the movie even more interesting and enjoyable."
# text3 = "I can see some people criticising this for being too crowd-pleasing, as there is a lot of fan service, references, and moments that seem designed to get crowds cheering. I didn't feel like it was too cynical. The core of the film - its premise, pacing, acting, action etc - are all solid."
# text4 = "I couldn't help but smile through most of this film. There are some truly incredible moments that I never thought I would see and will live in on cinema. The story was also more emotionally affecting than I expected."
text5 = "If you go to the cinema with your kids to see this, you will have a fantastic time. You will laugh out loud several times, you will feast on the visuals and enjoy the music. The characters are adorable and your kids will be up and dancing at the end."
text6 = "Let's begin with the two best elements for me, firstly the visuals, this movie looks terrific, some gorgeous shots, those behind the camera did a tremendous jobs. Secondly, the horror element, they managed to surprise you constantly, you didn't know when the next scare was coming, good fun for those that love jump scenes."
textmap={}

def text2list(t):
    mapping = str.maketrans(string.ascii_uppercase,string.ascii_lowercase, string.punctuation)
    t=t.translate(mapping)
    t=t.strip().split()
    return t

def createMap(*args):
    text=''
    for i in args:
        text += i + ' '
    dic={}
    text=text2list(text)
    for i,j in enumerate(set(text)):
        dic[j]=i
    return dic
    
textmap=createMap(text1, text2, text5, text6)
    
def createTextVector(t):
    t=text2list(t)
    c=collections.Counter(t)
    li = [0] * len(textmap)
    for i in c.keys():
        li[textmap[i]]=c[i]
    return li

li1 = createTextVector(text1)
li2 = createTextVector(text2)
li3 = createTextVector(text5)
li4 = createTextVector(text6)

sim1 = dot(li1,li2)/(norm(li1)*norm(li2))
sim2 = dot(li1,li3)/(norm(li1)*norm(li3))
sim3 = dot(li1,li4)/(norm(li1)*norm(li4))
sim4 = dot(li2,li3)/(norm(li2)*norm(li3))
sim5 = dot(li2,li4)/(norm(li2)*norm(li4))
sim6 = dot(li3,li4)/(norm(li3)*norm(li4))


print(f'Similarity between text 1 and text 2 is {sim1}')
print(f'Similarity between text 1 and text 5 is {sim2}')
print(f'Similarity between text 1 and text 6 is {sim3}')
print(f'Similarity between text 2 and text 5 is {sim4}')
print(f'Similarity between text 2 and text 6 is {sim5}')
print(f'Similarity between text 5 and text 6 is {sim6}')