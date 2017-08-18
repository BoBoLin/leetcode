/*
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

Difficulrt : Easy

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int arrayPairSum(int* nums, int numsSize) {
	int i = 0;
	int sum = 0;
	for(i = 0; i < numsSize; i+=2)
	{
		sum += nums[i];
	}
	return sum;
}
/*
	qsort(table, sizeof(table), sizeof(table[0]), comp_func);
	average case : O(n lgn) 
*/

int cmp (const void *a, const void *b)
{
	if (*(int *)a > *(int *)b) return 1;
	else if(*(int *)a < *(int *)b) return -1;
	else return 0;
}

void main(){
	int input[10] = {1, 4, 3, 2};
	int result = 0;
	//memset(input, 0, sizeof(tmp));
	int i = 0;
	qsort(input, 4, sizeof(input[0]), cmp);

	result = arrayPairSum(input, 4);

	printf("%d\n", result);
}
