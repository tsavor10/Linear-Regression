# import statements
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def main():
    # header
    print("****************************************")
    print("Comparing Stocks Using Linear Regression")
    print("****************************************")
    print()

    # user input for start, end, and number 
    start_date = input("Enter Start Date (yyyy-mm-dd): ")
    end_date = input("Enter End Date (yyyy-mm-dd): ")
    print()
    number = int(input("How Many Stocks Would You Like to Compare: "))
    print()

    # creating arrays to hold calculated slopes and stock names
    slopes = []
    stock_name = []

    # for loop based on user input
    for i in range(0, number):
        # user input for ticker, then downloads stock from yfinance
        stock = input("Enter Ticker: ")
        df = yf.download(stock, start = start_date, end = end_date)

        # plot graph based on open values
        plt.plot(df['Open'], label = stock)

        # makes array out of dates
        x1 = []
        for i in range(len(df.Open)):
            x1 += [df.index[i]]

        # makes array corresponding to indices
        x2 = []   
        for i in range(len(df.Open)):
            x2 += [x1.index(x1[i])]
        
        # creates x and y values
        x_axis = np.asarray(x2)
        y_axis = np.array(df.Open)

        # creates line
        m = (np.poly1d(np.polyfit(x_axis, y_axis, 1))(np.unique(x_axis)))

        # saves slopes and stock names to arrays
        slopes += [(m[len(m)-1] - m[0]) / len(m)]
        stock_name += [stock]

        # plots line
        plt.plot(np.unique(x1), m)

        # creates labels on graph
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.title("Comparing " + str(number) + " Stocks")
        plt.legend()

    # finds highest slope, then prints corresponding stock name
    max_value = np.max(slopes)
    print()
    print("The Best Stock Is: " + stock_name[slopes.index(max_value)])    

    # prints graph
    plt.show()
    
main()
