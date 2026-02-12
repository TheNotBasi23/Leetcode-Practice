class SnapshotArray:
    def __init__(self, length: int):
        self.myDict = {0: [0 for _ in range(length)]}
        self.length = length
    def set(self, index: int, val: int) -> None:
        self.myDict[len(self.myDict) - 1][index] = val
    def snap(self) -> int:
        snapID = len(self.myDict) - 1
        self.myDict[len(self.myDict)] = {}
        if snapID != 0:
            for key in self.myDict[snapID]:
                self.myDict[snapID + 1][key]  = self.myDict[snapID][key]
        return snapID
    def get(self, index: int, snap_id: int) -> int:
        return self.myDict[0][index] if index not in self.myDict[snap_id] else self.myDict[snap_id][index]