def rebalancePortfolio(
    currentHoldings,
    targetAllocations,
    stockPrices,
    maxTrades=None
):

    rebalance = {}

    total_value = 0
    diff = 0

    for stock in currentHoldings:
        value = currentHoldings[stock] * stockPrices[stock]
        total_value += value

    for stock in targetAllocations:
        target_value = total_value * targetAllocations[stock] / 100
        current_value = currentHoldings.get(stock, 0) * stockPrices[stock]
        rebalance[stock] = target_value - current_value

        for i in range(len(rebalance)):
            arr = []
            for key, value in rebalance.items():
                arr.append((key, abs(value)))
            arr.sort()

            res = []
            while len(res) < maxTrades:
                res.append(arr.pop())



        quantity = rebalance[stock] / stockPrices[stock] 
        if quantity > 0:
            action = "buy"
        
        elif quantity < 0:
            action = "sell"
            quantity = -quantity
        else:
           continue
            
        rebalance[stock] = {
            "symbol": stock,
            "action": action,
            "quantity": int(quantity),
            "price": stockPrices[stock]


            "total_value": total_value,
            "max_deviation_percent": max_deviation_percent,
            "final_allocations": final_allocations
        }

    return rebalance




currentHoldings = { "AAPL": 50,"GOOGL": 30,"MSFT": 20,"TSLA": 15,"NVDA": 10 }
targetAllocations = { "AAPL": 25, "GOOGL": 25, "MSFT": 25, "TSLA": 25 }
stockPrices = { "AAPL": 150.00, "GOOGL": 280.00,"MSFT": 330.00, "TSLA": 250.00,"NVDA": 500.00 }
maxTrades = 3



print(rebalancePortfolio(currentHoldings, targetAllocations, stockPrices, maxTrades))