import pytest
import sys

def computeScore(game):
    gameState = {"score": 0, "lastTurnScore": 0, "spare":False, "strike1":False, "strike2":False, "turnsDone":0, "incompleteTurn":False}

    for roll in game:
        rollScr = rollScore(roll, gameState)
        if gameState["turnsDone"] < 10:
            gameState["score"] += rollScr
        updateTurnCount(gameState, roll)
        updateForSpare(gameState, roll)
        updateForStrike(gameState, roll)
        gameState["lastTurnScore"] = rollScr

    return gameState["score"]


def updateTurnCount(gameState, roll):
    if roll in ['/', 'X'] or gameState["incompleteTurn"]:
        gameState["incompleteTurn"] = False
        gameState["turnsDone"] += 1
    else:
        gameState["incompleteTurn"] = True


def updateForStrike(gameState, roll):
    if gameState["strike2"]:
        gameState["strike2"] = False
        gameState["score"] += rollScore(roll, gameState)
    if gameState["strike1"]:
        gameState["strike1"] = False
        gameState["strike2"] = True
        gameState["score"] += rollScore(roll, gameState)
    if roll == 'X' and gameState["turnsDone"] <= 10:
        gameState["strike1"] = True


def updateForSpare(gameState, roll):
    if gameState["spare"]:
        gameState["spare"] = False
        gameState["score"] += rollScore(roll, gameState)
    if roll == '/':
        gameState["spare"] = True


def rollScore(roll, gameState):
    score = 0
    if roll == 'X':
        score = 10
    elif roll == '/':
        score = 10 - gameState["lastTurnScore"]
    elif roll != '-':
        score = int(roll)
    return score

def test_allMissScore0():
    assert computeScore("--------------------") == 0

def test_allTurns3points():
    assert computeScore("12121212121212121212") == 30

def test_5thenAllMissScore5():
    assert computeScore("5-------------------") == 5

def test_oneSpareNoBonus():
    assert computeScore("1/------------------") == 10

def test_oneSpareWithBonus():
    assert computeScore("4/3-----------------") == 16

def test_oneStrikeWithBonus():
    assert computeScore("4/X35--------------") == 46

def test_oneStrikeWith2Bonus():
    assert computeScore("4/XX61------------") == 70

def test_oneSpareWithBonusAfterEnd():
    assert computeScore("------------------1/7") == 17

def test_allStrikes():
    assert computeScore("XXXXXXXXXXXX") == 300

if __name__ == "__main__":
    print computeScore(sys.argv[1])
