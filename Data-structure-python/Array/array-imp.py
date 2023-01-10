import array as arr

array = arr.array('i', [1, 2, 3])

print('the array created was: ')
for i in array:
    print(i, end=' ')
print('\n')

array.append(4)
print('appending 4 to the array: ')
for i in array:
    print(i, end=' ')
print('\n')

array.insert(2, 50)
print('inserting 50 into position 2 of the array: ')
for i in array:
    print(i, end=' ')
print('\n')

print('exemple of empty initialized array:', end=' ')
array_2 = arr.array('i')

array_2.append(int(input()))
print('printing the number: ', end='')
print(array_2[0])
print('\n')

'''

Type Code	C Type	            Python Type 	    Minimum size in Bytes
'b'	        signed char	        int	                        1
'B'	        unsigned char	    int	                        1
'u'	        Py_UNICODE          unicode character	        2
'h'	        signed short	    int	                        2
'H'     	unsigned short	    int	                        2
'i'	        signed int	        int	                        2
'I'	        unsigned int        int                         2
'l'     	signed long	        int	                        4
'L'     	unsigned long	    int	                        4
'q'     	signed long long	int	                        8
'Q'     	unsigned long long	int	                        8
'f'     	float	            float	                    4
'd'	        double	            float	                    8

'''
