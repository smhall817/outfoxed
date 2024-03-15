### This program does a number of deductions for the board game "Outfoxed"
### To adjust the number of games, change the variable num_games in line 105

def play():

    import random
    
    suspects = [
        {'name' : 'Harold', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : True,
         'glasses' : True, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : True},
        {'name' : 'Henry', 'pocketwatch' : False, 'flower' : False, 'hat' : True,
         'necklace' : False, 'cane' : True, 'umbrella' : False, 'bag' : False,
         'glasses' : True, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Edith', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : True,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : True,
         'cloak' : True},
        {'name' : 'Riley', 'pocketwatch' : True, 'flower' : False, 'hat' : True,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : True, 'gloves' : False, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Daisy', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : True, 'cane' : True, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : True},
        {'name' : 'Lily', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : True, 'cane' : False, 'umbrella' : True, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : True, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Beatrice', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : True, 'bag' : False,
         'glasses' : False, 'scarf' : True, 'gloves' : True, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Belle', 'pocketwatch' : False, 'flower' : True, 'hat' : False,
         'necklace' : False, 'cane' : True, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : True,
         'cloak' : False},
        {'name' : 'Ingrid', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : True, 'bag' : False,
         'glasses' : True, 'scarf' : False, 'gloves' : True, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Charles', 'pocketwatch' : True, 'flower' : True, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : False,
         'glasses' : True, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Arthur', 'pocketwatch' : False, 'flower' : False, 'hat' : True,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : True,
         'glasses' : False, 'scarf' : True, 'gloves' : False, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Belvedere', 'pocketwatch' : True, 'flower' : False, 'hat' : True,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : True,
         'cloak' : False},
        {'name' : 'Gertrude', 'pocketwatch' : False, 'flower' : True, 'hat' : False,
         'necklace' : True, 'cane' : True, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : False},
        {'name' : 'Alice', 'pocketwatch' : True, 'flower' : False, 'hat' : False,
         'necklace' : True, 'cane' : False, 'umbrella' : False, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : False, 'monocle' : False,
         'cloak' : True},
        {'name' : 'Maggie', 'pocketwatch' : False, 'flower' : False, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : True, 'bag' : False,
         'glasses' : False, 'scarf' : False, 'gloves' : True, 'monocle' : True,
         'cloak' : False},
        {'name' : 'Mary', 'pocketwatch' : False, 'flower' : True, 'hat' : False,
         'necklace' : False, 'cane' : False, 'umbrella' : False, 'bag' : True,
         'glasses' : False, 'scarf' : True, 'gloves' : False, 'monocle' : False,
         'cloak' : False}
        ]
    
    answer = random.choice(suspects)
    #print('Answer: ' + answer['name'])
    
    question_list = ['pocketwatch', 'flower', 'hat', 'necklace', 'cane', 'umbrella',
                 'bag', 'glasses', 'scarf', 'gloves', 'monocle', 'cloak']
    
    num_questions = 0
    
    def ask():
    
        question = random.choice(question_list)
    #    print("Question " + str(num_questions + 1) + ': ' + question)
        question_list.remove(question)
    
        for s in reversed(suspects):
            if s[question] != answer[question]:
                suspects.remove(s)
                
    #    for s in suspects:
    #        print(s['name'])
                
    while len(suspects) > 1:
        ask()
        num_questions += 1
        
    #print(suspects)
    return(num_questions)

results = []

num_games = 100000

for i in range(num_games):
    results.append(play())
    
import matplotlib.pyplot as plt
from collections import Counter

labels = Counter(results).keys()
freq = Counter(results).values()

plt.bar(labels, freq, color = 'dodgerblue')
plt.xlabel('Number of questions needed to reach answer (Average = ' + str(sum(results) / len(results)) + ')')
plt.ylabel('Frequency')
plt.title(str(num_games) + ' Rounds of \"Outfoxed\" Board Game')