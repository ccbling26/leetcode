package _380

import "math/rand"

type RandomizedSet struct {
	nums []int
	data map[int]int
}

func Constructor() RandomizedSet {
	return RandomizedSet{[]int{}, map[int]int{}}
}

func (this *RandomizedSet) Insert(val int) bool {
	_, ok := this.data[val]
	if ok {
		return false
	} else {
		this.data[val] = len(this.nums)
		this.nums = append(this.nums, val)
		return true
	}
}

func (this *RandomizedSet) Remove(val int) bool {
	idx, ok := this.data[val]
	if !ok {
		return false
	} else {
		lastIdx := len(this.nums) - 1
		this.nums[idx] = this.nums[lastIdx]
		this.data[this.nums[lastIdx]] = idx
		this.nums = this.nums[:lastIdx]
		delete(this.data, val)
		return true
	}
}

func (this *RandomizedSet) GetRandom() int {
	return this.nums[rand.Intn(len(this.nums))]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
