nums= [1,54,57,12,111,4231,6,413911,2,22,1,0,22,-1131,-123,-149,5,-10]
nums_to_str= ['1','54','57','12','111','4231','6','413911','2','22','1','0','22','-1131','-123','-149','5','-10']
nums_to_str.sort()
#Groups all the numbers with the 1s starting  digits and then all the 2s starting digit and all the 3s starting digit ...
#print(nums_to_str)

#The above was not great I will convert line 1 to a string using this method
nums.sort(key=str)
print(nums)
