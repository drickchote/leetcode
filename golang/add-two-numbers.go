package main

import (
	"fmt"
	"math"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func convert_number_to_node(number uint64) *ListNode {
	var listNode ListNode = ListNode{Val: int(number % 10)}
	number = number - number%10
	tempNode := &listNode
	factor := 2
	for number > 0 {
		nextVal := number % uint64(math.Pow(10, float64(factor))) / uint64(math.Pow(10, float64(factor-1)))
		tempNode.Next = &ListNode{Val: int(nextVal)}
		number = number - number%uint64(math.Pow(10, float64(factor)))
		factor++
		tempNode = tempNode.Next
	}

	return &listNode
}

func convert_node_to_number(l1 *ListNode) uint64 {
	temp := l1
	factor := 1
	result := uint64(0)

	temp = l1

	for temp != nil {
		result += uint64(temp.Val * int(factor))
		factor *= 10
		temp = temp.Next

	}
	return result
}

// This is the solution
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil && l2 == nil {
		return nil
	}

	if l1 == nil {
		if l2.Val <= 9 {
			return l2
		}

		node := new(ListNode)
		node.Val = l2.Val % 10
		node.Next = addTwoNumbers(l2.Next, &ListNode{Val: 1})
		return node
	}

	if l2 == nil {
		if l1.Val <= 9 {
			return l1
		}

		node := new(ListNode)
		node.Val = l1.Val % 10
		node.Next = addTwoNumbers(l1.Next, &ListNode{Val: 1})
		return node
	}

	nodeResult := l1.Val + l2.Val

	if nodeResult > 9 {
		nodeResult %= 10

		if l1.Next == nil {
			l1.Next = new(ListNode)
		}
		l1.Next.Val++
	}

	node := ListNode{Val: nodeResult}

	node.Next = addTwoNumbers(l1.Next, l2.Next)
	return &node
}

func printNode(node *ListNode) {
	for node != nil {
		fmt.Printf("%d ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

func main() {
	number1 := convert_number_to_node(9999999)
	number2 := convert_number_to_node(9999)

	result := addTwoNumbers(number1, number2)

	printNode(result)
}
