'''Description
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that ".." represents the values in between.

Input Format 
The first line contains an integer .

Output Format 
Output the answer as explained in the task.

Sample Input

3
Sample Output

123 '''

#code:
n = int( raw_input())
l = range(1,n+1)
for i in l:
	print (i,end = "")
