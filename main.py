#Ask the user’s age. If they are 18 or over, display the message “You can vote”. If they are aged 17, display the message “You can learn to drive”. If they are 16, display the message, “You can buy a lottery ticket”. If they are under 16, display the message “You can go trick or treating” 
yname=input("Enter you name: ")
print("\nHi ",yname)
age=int(input("\nPlease enter your age: "))
if age>=18:# If they are 18 or over, display the message “You can vote”. 
  print("\n",yname, "you are eligable to vote")
elif age>=17:#If they are aged 17, display the message “You can learn to drive”. 
  print("\n",yname, "you can learn to drive")
elif age>=16:#If they are 16, display the message, “You can buy a lottery ticket”. 
  print("\n",yname, "you can buy a lottery ticket")
else:#If they are under 16, display the message “You can go trick or treating” 
  print("\n",yname, " you can go to trick or treating")
