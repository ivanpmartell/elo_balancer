import random
import itertools
from indexed import IndexedOrderedDict


def splitDict(d):
    n = len(d) // 5
    i = iter(d.items())

    dictList = []
    for j in range(n):
        dic = dict(itertools.islice(i, 5))
        dictList.append(dic)

    return dictList

def closer_to(target, v1, v2, v3, v4):
    if(abs(target - v1) + abs(target - v2) < abs(target - v3) + abs(target - v4)):
        return True
    return False

players = {}
numPlayers = 50
for x in range(numPlayers):
    name = "p" + str(x)
    pvalue = random.randint(400,2000)
    players.update({name: pvalue})

targetSum = sum(players.values())/(numPlayers/5)
print("target: " + str(targetSum))

teams = splitDict(players)
sortedTeams = []
for team in teams:
    sorted_dict = sorted(team.items(), key=lambda kv: kv[1])
    sortedTeam = IndexedOrderedDict(sorted_dict)
    sortedTeams.append(sortedTeam)

#optimization
maxsteps = 20000
for step in range(maxsteps):
    r = random.randint(0,len(sortedTeams) - 1)
    currentTeam = sortedTeams[r]
    otherTeams = sortedTeams[:]
    otherTeams.pop(r)
    for otherTeam in otherTeams:
        rp = random.randint(0,4)
        phCurrent = currentTeam.items()[rp]
        phOther = otherTeam.items()[rp]

        currentElo = sum(currentTeam.values()) - phCurrent[1] + phOther[1]
        otherElo = sum(otherTeam.values()) - phOther[1] + phCurrent[1]

        if(closer_to(targetSum, currentElo, otherElo, sum(currentTeam.values()), sum(otherTeam.values()))):

            del currentTeam[phCurrent[0]]
            currentTeam[phOther[0]]= phOther[1]
            currentTeam.move_to(phOther[0], rp)

            del otherTeam[phOther[0]]
            otherTeam[phCurrent[0]] = phCurrent[1]
            otherTeam.move_to(phCurrent[0], rp)

print(sortedTeams)
for team in sortedTeams:
    elo = sum(team.values())
    print(elo)
