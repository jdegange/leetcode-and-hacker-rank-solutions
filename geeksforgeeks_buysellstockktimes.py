# Python program to maximize the profit 
# by doing at most k transactions 
# given stock prices for n days 

# Function to find out maximum profit by 
# buying & selling a share atmost k times 
# given stock price of n days 
def maxProfit(prices, n, k): 
	
	# Bottom-up DP approach 
	profit = [[0 for i in range(k + 1)] 
				for j in range(n)] 
	
	# Profit is zero for the first 
	# day and for zero transactions 
	for i in range(1, n): 
		
		for j in range(1, k + 1): 
			max_so_far = 0
			
			for l in range(i): 
				max_so_far = max(max_so_far, prices[i] -
							prices[l] + profit[l][j - 1]) 
							
			profit[i][j] = max(profit[i - 1][j], max_so_far)
			print(profit)
	return profit[n - 1][k] 

# Driver code 
k = 117
prices = [10, 22, 5, 75, 65, 80,10, 22, 5,1, 75, 65, 80,100, 22, 5, 75, 65, 80] 
n = len(prices) 

print("Maximum profit is:", 
	maxProfit(prices, n, k)) 

# This code is contributed by vaibhav29498 
# thank you. modified jdegange85
