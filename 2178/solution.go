package _2178

func maximumEvenSplit(finalSum int64) []int64 {
	if finalSum%2 == 1 {
		return []int64{}
	}
	res := []int64{}
	i := int64(2)
	for i <= finalSum {
		res = append(res, i)
		finalSum -= i
		i += 2
	}
	res[len(res)-1] += finalSum
	return res
}
