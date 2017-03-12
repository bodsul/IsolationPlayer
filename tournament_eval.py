from __future__ import division
import sys

my_file = sys.argv[1]

def GetPerf(lines, matchstr):
    Agent = [float(line.split(' ')[-1]) for line in lines if line.startswith(matchstr)]
    IdVAgent = []
    StudVAgent = []
    for j in range(0, len(Agent)):
        if j % 2:
            StudVAgent.append(Agent[j])
        else:
            IdVAgent.append(Agent[j])
    return IdVAgent, StudVAgent
    
lines = [line.rstrip('\n') for line in open(my_file)]

ID_Improved_lines = [line.split('         ')[1] for line in lines if line.startswith('ID_Improved')]
Student_lines = [line.split('             ')[1] for line in lines if line.startswith('Student') ]

#print(ID_Improved_lines)
#print(Student_lines)


wins = [j for j in range(0, len(ID_Improved_lines)) if float(Student_lines[j].strip('%')) > float(ID_Improved_lines[j].strip('%'))]
draws = [j for j in range(0, len(ID_Improved_lines)) if float(Student_lines[j].strip('%')) == float(ID_Improved_lines[j].strip('%'))]
losses = [j for j in range(0, len(ID_Improved_lines)) if float(Student_lines[j].strip('%')) < float(ID_Improved_lines[j].strip('%'))]

print('wins VS id_improved', len(wins))
print('draws VS id_improved', len(draws))
print('losses VS id_improved', len(losses))


for j in range(0, len(Student_lines)):
	print(j+1, '&', ID_Improved_lines[j].strip('%'), '&', Student_lines[j].strip('%'), '\\\\', '\hline')
	

IdVRandom, StudVRandom = GetPerf(lines, '  Match 1')
IdVMMNull, StudVMMNull = GetPerf(lines, '  Match 2')
IdVMMOpen, StudVMMOpen = GetPerf(lines, '  Match 3')
IdVMMImproved, StudVMMImproved = GetPerf(lines, '  Match 4')
IdVABNull, StudVABNull = GetPerf(lines, '  Match 5')
IdVABOpen, StudVABOpen = GetPerf(lines, '  Match 6')
IdVABImproved, StudVABImproved = GetPerf(lines, '  Match 7')

print('Performance vs each agent')
print('Agent Eval Function', '&', 'ID_improved win %', '&', 'Agent with Custom Score Eval Function', '\\\\', '\hline')
print('Random', '&', 100 - 100*sum(IdVRandom)/(20*len(IdVRandom)), '&', 100 - 100*sum(StudVRandom)/(20*len(StudVRandom)), '\\\\', '\hline')
print('MM\_Null', '&', 100 - 100*sum(IdVMMNull)/(20*len(IdVMMNull)), '&', 100 - 100*sum(StudVMMNull)/(20*len(StudVMMNull)), '\\\\', '\hline')
print('MM\_open', '&', 100 - 100*sum(IdVMMOpen)/(20*len(IdVMMOpen)), '&', 100 - 100*sum(StudVMMOpen)/(20*len(StudVMMOpen)), '\\\\', '\hline')
print('MM\_improved', '&', 100 - 100*sum(IdVMMImproved)/(20*len(IdVMMImproved)), '&', 100 - 100*sum(StudVMMImproved)/(20*len(StudVMMImproved)), '\\\\', '\hline')
print('AB\_Null', '&', 100 - 100*sum(IdVABNull)/(20*len(IdVABNull)), '&', 100 - 100*sum(StudVABNull)/(20*len(StudVABNull)), '\\\\', '\hline')
print('AB\_open', '&', 100 - 100*sum(IdVABOpen)/(20*len(IdVABOpen)), '&', 100 - 100*sum(StudVABOpen)/(20*len(StudVABOpen)), '\\\\', '\hline')
print('AB\_improved', '&', 100 - 100*sum(IdVABImproved)/(20*len(IdVABImproved)), '&', 100 - 100*sum(StudVABImproved)/(20*len(StudVABImproved)), '\\\\', '\hline')


