def divide(nu, de):
  try:
    result = nu/de
  except ZeroDivisionError :
      print("Error Division by zero")
  else: 
    result = nu/de
    print("Result: ", result)
  finally:
    print("End of program")

print(divide(5, 0))
print(divide(5, 2))
  
