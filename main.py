#Function that will receive list containing all heights
def birthday_cake_candles(candle_heights):
    aux = [] #empty list to store the highest value and then count it
    tallest_candle = max(candle_heights); #get the highest number from list
    for n in candle_heights: #loop over list and store all occurrencies of 
        if n == tallest_candle:  # the highest number
            aux.append(n);
            occurrencies = len(aux);

    return occurrencies; #return only the number of occurrencies

print(birthday_cake_candles([4,10,10,10, 1, 2, 10]))
