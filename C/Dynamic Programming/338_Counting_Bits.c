/*
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of
1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss?
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.

Difficulty : Medium

*/

#include <stdio.h>
#include <stdlib.h>

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int i = 0;
    int count = 1;
    int len = 0;

	int* tmp = calloc(256, sizeof(int));

    while (len <= num)
    {
    	len += count;
    	for(i = 0; i< count ; i++)
    	{
    		tmp[i] = returnSize[i] + 1;
    		returnSize[count + i] = tmp[i];

    	}
    	count *= 2;

    }

    free(tmp);

    return returnSize; 


}


int main()
{

	int* arr = calloc(256, sizeof(int));

	int i;
	int num = 5;

	int* result = calloc(num, sizeof(int));
	
	/*for(i = 0; i < 10; i++) {
        printf("arr[%d] = %d\n", i, *(arr+i));
    }*/

    countBits(num, arr);

    for(i = 0; i < num+1; i++) {
    	//result[i] = arr[i];
        *(result + i) = *(arr+i);
        printf("result[%d] = %d\n", i, *(result+i));

    }

    free(arr);
    free(result);

	return 0;
}