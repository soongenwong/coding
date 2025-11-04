def rebalancePortfolio(
    currentHoldings,
    targetAllocations,
    stockPrices
):

    rebalance = {}

    total_value = 0

    for stock in currentHoldings:
        value = currentHoldings[stock] * stockPrices[stock]
        total_value += value

    for stock in targetAllocations:
        target_value = total_value * targetAllocations[stock] / 100
        current_value = currentHoldings.get(stock, 0) * stockPrices[stock]
        rebalance[stock] = target_value - current_value

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
        }

    return rebalance




currentHoldings = { "TSLA": 20 }
targetAllocations = { "TSLA": 50, "NVDA": 50 }
stockPrices = { "TSLA": 250.00, "NVDA": 500.00 }

print(rebalancePortfolio(currentHoldings, targetAllocations, stockPrices))