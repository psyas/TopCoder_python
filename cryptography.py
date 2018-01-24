class cryptography:
    def encrypt(self, numbers):
        min_val = min(numbers)
        inx = numbers.index(min_val)
        numbers[inx]+=1
        
        result = 1
        for item in numbers:

            result = result * item
        return result

def main():
    cry = cryptography()
    numbers = [1000,999,998,997,996,995]
    print(cry.encrypt(numbers))

if __name__ == "__main__":
    main()
        
