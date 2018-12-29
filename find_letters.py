import numpy as np
dice = np.array([['Q','B','Z','J','X','K'],
 ['T','O','U','O','T','O'],
 ['O','V','W','R','G','R'],
 ['A','A','A','F','S','R'],
 ['A','U','M','E','E','G'],
 ['H','H','L','R','D','O'],
 ['N','H','D','T','H','O'],
 ['L','H','N','R','O','D'],
 ['A','F','A','I','S','R'],
 ['Y','I','F','A','S','R'],
 ['T','E','L','P','C','I'],
 ['S','S','N','S','E','U'],
 ['E','T','I','L','I','C'],
 ['I','T','I','T','I','E'],
 ['E','E','E','E','M','A'],
 ['Y','I','F','P','S','R'],
 ['A','E','A','E','E','E'],
 ['U','O','T','O','W','N'],
 ['M','N','N','E','A','G'],
 ['E','A','N','D','N','N'],
 ['S','C','T','I','E','P'],
 ['T','T','O','T','E','M'],
 ['T','S','N','W','C','C'],
 ['D','O','R','D','L','N'],
 ['R','I','Y','P','R','H']])

def boggle():
    np.random.shuffle(dice)
    shuffled_dice = np.hstack((
              dice[0,np.random.choice(6)],
              dice[1,np.random.choice(6)],
              dice[2,np.random.choice(6)],
              dice[3,np.random.choice(6)],
              dice[4,np.random.choice(6)]
            ))
    for i in range(1,5):
           shuffled_dice = np.vstack((shuffled_dice,np.hstack((
              dice[5*i,np.random.choice(6)],
              dice[5*i+1,np.random.choice(6)],
              dice[5*i+2,np.random.choice(6)],
              dice[5*i+3,np.random.choice(6)],
              dice[5*i+4,np.random.choice(6)]
            ))))
           
    return shuffled_dice