class InterestingParty:
    def bestInvitation(self, first, second):
        interest = list()
        interest_set = set()
        for a,b in zip(first, second):
            interest.append(a)
            interest.append(b)
            interest_set.add(a)
            interest_set.add(b)
        return max([interest.count(x) for x in interest_set])

def main():
    hi = InterestingParty()
    first = ["a",'b','c','a']
    second = ['e','a','a','f']

    print(hi.bestInvitation(first, second))

if __name__ == "__main__":
    main()
