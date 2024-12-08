
def add(num_a,num_b):
    total = num_a + num_b
    return total 

def subtraction(num_a,num_b):
    total = num_a-num_b
    return total

def multiply(num_a,num_b):
    total = num_a*num_b
    return total 

def divide(num_a,num_b):
    total = num_a/num_b
    return total


num_1 = float(input("what is the first value ?:"))

should_continue = True 
while should_continue : 

 operations = {
  "add":add,
  "subtraction":subtraction,
  "multiply":multiply,
  "divide":divide
}
 for symbols in operations :
    print(symbols)

 operations_symbol = input("what operation do you want to perform")
 num_2 = float(input("what is the second value ?:"))

 answer = operations[operations_symbol](num_1,num_2)
 print(answer)

 further = input(f"do you want to do more calculations with {answer}.Type 'yes' or 'no'")

 if further == "yes" :
    num_1 = answer 
 else :
  should_continue = False 

