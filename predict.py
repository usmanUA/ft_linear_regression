from utils.dataHelpers import readThetas


def main():
    '''Reads the user input for car mileage and preditcs its price'''
    try:
        mileage = input("\033[33mEnter Car's Mileage in KMs: \033[0m")
        while len(mileage) == 0 or len(mileage) > 6:
            print("\033[31mPlease Enter value between 1 - 999999 KMs\033[0m")
            mileage = input("\033[33mEnter Car's Mileage in KMs: \033[0m")
        mileage = int(mileage)
    except OverflowError:
        AssertionError("Int overflow occured.")
    try:
        thetas = readThetas('thetas.txt')
        price = float(thetas[0]) + (float(thetas[1]) * mileage)
    except FloatingPointError:
        AssertionError("Can not convert str to float")
    print(f"\033[36mThe price of the car with mileage {mileage} is: \033[0m{price}")


if __name__ == '__main__':
    main()
