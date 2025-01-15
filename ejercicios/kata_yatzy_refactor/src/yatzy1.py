from src.pips import Pips

class Yatzy:

    ZERO = 0
    FIFTY = 50

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        NECESSARY_VALUE = 5
        return Yatzy.FIFTY if dice.count(dice[0]) == NECESSARY_VALUE else Yatzy.ZERO

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(ONE)

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO
    
    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX
    
    @classmethod
    def __find_pairs(cls, *dice):
        pairs = []
        for die in set(dice):
            if dice.count(die) > 1:
                pairs.append(die)
        return pairs
    
    @classmethod
    def __max_pair(cls, *dice):
        return max(cls.__find_pairs(*dice))
            

    @classmethod
    def score_pair(cls, *dice):
        TWO = Pips.TWO.value
        pair = cls.__max_pair(*dice)
        return pair * TWO
        
    @classmethod
    def two_pair(cls, *dice):
        pairs = cls.__find_pairs(*dice)
        return (pairs[0] * 2) + (pairs[1] * 2) if len(pairs) > 1 else Yatzy.ZERO

    @staticmethod
    def four_of_a_kind(*dice):
        for die in dice:
            return die * 4 if dice.count(die) > 3 else Yatzy.ZERO

    @staticmethod
    def three_of_a_kind(*dice):
        for die in dice:
            return die * 3 if dice.count(die) > 2 else Yatzy.ZERO

    @staticmethod
    def smallStraight(*dice):
        small_staight = (1,2,3,4,5)
        return Yatzy.chance(*dice) if small_staight == tuple(sorted(dice)) else Yatzy.ZERO

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
