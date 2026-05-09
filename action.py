# will represent an operator/action on a node
from enums import ActionsEnum

class Action:
    def __init__(self, srcIdx, destIdx, action):
        self.srcIdx = srcIdx
        self.destIdx = destIdx
        self.action = action # should be ActionsEnum

    def __eq__(self, rhs):
        if not isinstance(rhs, Action): return False

        # identical idx's and action
        if (self.srcIdx == rhs.srcIdx) and (self.destIdx == rhs.destIdx) and (self.action == rhs.action):
            return True

        # will basically be looking for mirrored actions
        sameIdxsButSwapped = (self.srcIdx == rhs.srcIdx) and (self.destIdx == rhs.destIdx)
        oppositeActions = (self.action == ActionsEnum.UP and rhs.action == ActionsEnum.DOWN)
        oppositeActions = oppositeActions or (self.action == ActionsEnum.DOWN and rhs.action == ActionsEnum.UP)
        oppositeActions = oppositeActions or (self.action == ActionsEnum.RIGHT and rhs.action == ActionsEnum.LEFT)
        oppositeActions = oppositeActions or (self.action == ActionsEnum.LEFT and rhs.action == ActionsEnum.RIGHT)

        return (sameIdxsButSwapped and oppositeActions)

