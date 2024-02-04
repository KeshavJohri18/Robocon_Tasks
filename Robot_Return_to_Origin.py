class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        moveslist = list(moves)

        rights = moveslist.count("R")
        lefts = moveslist.count("L")
        ups = moveslist.count("U")
        downs = moveslist.count("D")

        if((ups == downs) and (rights == lefts)):
            return True
        else:
            return False