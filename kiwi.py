class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, fromId, toId):
        for a,b in zip(fromId, toId):
            transfer_amount = min(bottles[a], capacities[b] - bottles[b])
            bottles[a] = bottles[a] - transfer_amount
            bottles[b] = bottles[b] + transfer_amount


def main():
    kiwi = KiwiJuiceEasy()
    fromId = [2,3,2,0,1]
    toId = [0,1,1,3,2]
    capacities = [700000,800000,900000,1000000]
    bottles = [478478,478478,478478,478478]

    print("before : ",bottles)
    kiwi.thePouring(capacities, bottles, fromId, toId)
    print("after : ",bottles)

if __name__ == "__main__":
    main()
