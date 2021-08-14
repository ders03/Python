#Ask the user for a number, then a word, and then print out a phrase that depends on the number and the word.You should pluralize the word by adding an “s” to the end whenever they enter a number that is 0 or greater than 1. You’ll need to implement an if/else statement in your code, since you don’t want to pluralize the word in every instance! 


#inputs 
input_number=input("Enter a number:") 
input_word=input("Enter a word:") 

#base case - needs string with cases 
ext = ["sh", "ay", "oy", "ey", "uy", "y", "ch", "ife", "us"]
if input_word.endswith(tuple(ext)) == False and input_number!="1":
        print(input_number + " " + input_word + "s")  
        
elif input_number.endswith("1"):
    print(input_number + " " + input_word)
#life case        
elif input_word.endswith("ife") and input_number!="1": 
            result=input_word.replace("ife", "ives") 
            print(input_number + " " + result) 
#sh/ch case shes/ches
elif input_word.endswith("sh") and input_number!="1": 
    result=input_word.replace("sh", "shes") 
    print(input_number + " " + result) 
    
elif input_word.endswith("ch") and input_number!="1":
    new=input_word[::-1]
    result=new.replace("hc", "sehc", 1) 
    back=result[::-1]
    print(input_number + " " + back)
#us case 
elif input_word.endswith("us") and input_number!="1": 
    result=input_word.replace("us", "i") 
    print(input_number + " " + result)
#ay/oy/ey/uy -> ays/oys/eys/uys case 
elif input_word.endswith("ay") and input_number!="1": 
    result=input_word.replace("ay", "ays") 
    print(input_number + " " + result)

elif input_word.endswith("oy") and input_number!="1":  
    result=input_word.replace("oy", "oys") 
    print(input_number + " " + result)

elif input_word.endswith("ey") and input_number!="1": 
    result=input_word.replace("ey", "eys")
    print(input_number + " " + result)

elif input_word.endswith("uy") and input_number!="1": 
    result=input_word.replace("uy", "uys")
    print(input_number + " " + result) 
#y -> ies case 
elif input_word.endswith("y") and input_number!="1": 
    result=input_word.replace("y", "ies") 
    print(input_number + " " + result) 