package leetcode

func TwoSum(nums []int, target int) []int {
	var memo = make(map[int]int)

	for index, value := range nums {
		rest := target - value

		if _, ok := memo[rest]; ok {
			return []int{index, memo[rest]}
		}

		memo[value] = index
	}

	return nil
}
