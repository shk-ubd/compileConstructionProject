# Language Specification


---
## Data Types
- int (Integer)
- bool (Boolean)

## Initialization How to Declare variable?
```
int myNumber = 123
bool bit = True
```

## Conditional Statements
```
if_stmnt condition:
    //block of code
else_stmnt:
    //block of code
```

## Loops
```
for item in sequence:
    //block of code

for i in range(5):
    //block of code

```


```
for i in range(5):
    if_stmnt(bit):
        print(1)
        continue
    else_stmnt:
        print(0)
        break


```

## Functions

Function with Parameter and No return
```
dec functionName(int param):
    //codeblock
```
Function with Parameter and return
```
dec functionName(int param1,bool param2):
    //codeblock
    restore myVariable
```
Function with No Parameter and No return
```
dec functionName():
    //codeblock
```
Function with No Parameter and return
```
dec functionName():
    //codeblock
    restore myVariable
```


## Input
```
int variable = input("Enter Input: ") 
print(variable)
```

## Comments 
```
//Every line starting with double slash will be ignored
```