import random
votes=[]
elton_intial= ["DGBMY","TD","BATJ","RM","YS"]
for i in range(len(elton_intial)):
  print(elton_intial[i])
num = random.randint(0,5)
print(elton_intial[num])
for i in range(len(elton_intial)):
  nvotes=int(input("how many ppl voted for" + str(elton_intial[i]))
  votes.append(nvotes)
for i in  range(len(elton_intial)):
  print("the votes for ", elton_intial[i], "are", votes[i])
posn_max =- 999
for i in range(len(elton_intial)):
  if votes[i] >posn_max:
    posn_max = vote[i]
    max_votes = i 
  else:
    posn_max = posn_max
print("The most popular is "+ str(initials[max_votes]) + " with a vote of " +  str(votes[max_votes]))
