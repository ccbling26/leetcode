package _134

func canCompleteCircuit(gas []int, cost []int) int {
	n := len(gas)
	all := 0
	res := 0
	idx := 0
	for i := 0; i < n; i++ {
		val := gas[i] - cost[i]
		all += val
		res += val
		if res < 0 {
			res = 0
			idx = i + 1
		}
	}
	if all < 0 {
		return -1
	}
	return idx
}
