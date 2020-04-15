while True:
	try:
		number=int(input(“What’s your favorite number dude?\n”))
		print(18/number)
		break
	except ValueError:
		print(“Make sure to enter only digits”)
	except ZeroDivisionError:
		print(“You cannot divide by Zero”)
	except:
		break
	finally:				#finally keyword no matter what happens this will always be executed
		print(“loop complete”)
