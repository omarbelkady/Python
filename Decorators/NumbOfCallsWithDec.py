class PleaseCountHowManyCallsIMake:
    #def constructor
    def __init__(self, func):
        self.func=func
        self.number_of_calls_i_made = 0

    #count the number of calls
    def __call__(self, *args, **kwargs):
        self.number_of_calls_i_made += 1
        print(f"This was executed {self.number_of_calls_i_made} times")
        return self.func(*args, **kwargs)

@PleaseCountHowManyCallsIMake
def say_Hi_To_Everyone():
    print("Hi Everyone")


say_Hi_To_Everyone()
for j in range(1,7):
    say_Hi_To_Everyone()
