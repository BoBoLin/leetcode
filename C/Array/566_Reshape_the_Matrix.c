/*
In MATLAB, there is a very useful function called 'reshape',
which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array,
and two positive integers r and c representing the row number and column number
of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix
in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = [[1,2],
	    [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4].
The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

Difficulty: Easy

*/

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

void print_array(int** array, int r, int c)
{
	int i, j;
	for(i = 0; i< r ; i++)
	{
		for(j = 0; j< c; j++)
			printf("%d ", array[i][j]);
		printf ("\n");
	}
}

int** matrixReshape(int** nums, int numsRowSize, int numsColSize, int r, int c, int** columnSizes, int* returnSize) 
{
	if(numsRowSize * numsColSize != r * c)
	{
		print_array(nums, numsRowSize, numsColSize);
		return 0;
	}
	int i, j;
	int* values;
    int** rows;

    values = returnSize;
    rows = columnSizes;

    for (i=0; i< r; i++)
    {
    	rows[i] = values + i*c;
    }

    int new_r = 0;
    int new_c = 0;
    for(i = 0; i< numsRowSize ; i++)
	{
		for(j = 0; j< numsColSize; j++)
		{
			rows[new_r][new_c] = nums[i][j];
			if(new_c == (c - 1))
			{
				new_c = 0;
				new_r ++;
			}
			else
			{
				new_c ++;
			}
		}
	}

	print_array(rows, r, c);

	return rows;
}

void main(){

    int m = 3;
    int n = 2;
    int r = 2;
    int c = 3;

    int* returnSize = calloc(r*c, sizeof(int)); 
    int** columnSizes = malloc(c*sizeof(int*));

    int input[3][2] = {{1,2},{3,4}, {5,6}};

    int* values = calloc(m*n, sizeof(int));
    int** rows = malloc(n*sizeof(int*));
    int i, j;
    for (i=0; i<m; i++)
    {
    	rows[i] = values + i*n;
    }

    for(i = 0; i< m; i++)
    {
    	for(j = 0; j<n; j++)
    	{
    		rows[i][j] = input[i][j];
    	}
    }

    rows = matrixReshape(rows, m, n, r, c, columnSizes, returnSize);
    if(rows == 0)
    	printf("FAIL\n");
    else
    	printf("NICE\n");

    free(returnSize);
    free(columnSizes);
    free(values);
    free(rows);

}



