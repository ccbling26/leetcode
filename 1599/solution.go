package _1599

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	if 4*boardingCost-runningCost <= 0 {
		return -1
	}
	var minRound, curRound, maxProfits, curProfits, restNum int
	i, n := 0, len(customers)
	for i < n || restNum != 0 {
		if i < n {
			restNum += customers[i]
			i++
		}
		curProfits += min(restNum, 4)*boardingCost - runningCost
		curRound++
		if curProfits > maxProfits {
			maxProfits = curProfits
			minRound = curRound
		}
		restNum -= min(restNum, 4)
	}
	if minRound > 0 {
		return minRound
	}
	return -1
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
