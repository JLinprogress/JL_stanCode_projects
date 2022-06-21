"""
File: weather_master.py
Name: Jerry Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -66


def main():
	"""
	TODO:
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data_ini = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data_ini == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data_ini
		minimum = data_ini
		summary = data_ini
		under_16 = 0
		counter = 0
		if data_ini < 16:
			under_16 += 1
		if data_ini != EXIT:
			counter += 1

		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			# user EXIT the program after only inputting one data
			if data == EXIT and counter == 1:
				print('Highest temperature = ' + str(data_ini))
				print('Lowest temperature = ' + str(data_ini))
				print('Average = ' + str(data_ini))
				print(str(under_16) + ' cold day(s)')
				break

			# user input more than one data before ending the program
			else:
				if data == EXIT:
					print('Highest temperature = ' + str(maximum))
					print('Lowest temperature = ' + str(minimum))
					print('Average = ' + str((float(summary) / float(counter))))
					print(str(under_16) + ' cold day(s)')
					break
				if data != EXIT:
					summary += data
					counter += 1
				if data > maximum:
					maximum = data
				if data < minimum:
					minimum = data
				if data < 16:
					under_16 += 1



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
