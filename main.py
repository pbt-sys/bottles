numBottles = 15
numExchange = 4

class Solution:

    def __init__(self, numBottles, numExchange):
        
        self.numBottles = numBottles
        self.numExchange = numExchange


    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        exchangedBottles = numBottles // numExchange
        remainder = numBottles % numExchange

        return exchangedBottles, remainder

solution = Solution(numBottles, numExchange)

def main():
        
    start_num = solution.numBottles
    total_drunk = solution.numBottles
    exchange = solution.numWaterBottles(start_num, solution.numExchange)
    start_num = exchange[0] + exchange[1]
    total_drunk += exchange[0]

    while exchange[0] >= 1:
        exchange = solution.numWaterBottles(start_num, solution.numExchange)
        start_num = exchange[0] + exchange[1]
        total_drunk += exchange[0]

    total_drunk += exchange[0]

    print(total_drunk)

if __name__ == "__main__":
    main()