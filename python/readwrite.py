#!/bin/python3

months = open('months.txt')
##print(months.readline())
##print(months.readlines())
##months.seek(0)
##print(months.readlines())

for month in months:
	print(month.strip())

months.close()

##Opening a new file

days = open('days.txt', 'a')

days.write("\nTuesday")



days.close();
