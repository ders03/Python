import string
#inputs 
input_number=input("Enter a number:") 
input_word=input("Enter a word:")  

#function attempt
endings_dict =dict{"ending":"ife","sh","ch","us","ay","oy","ey","uy","y"} 
into_dict =dict{"into":"ives","shes","ches","i","ays","oys","eys","uys","ies"}        
def replace(input_word, dict): 
    ext=["ife","sh","ch","us","ay","oy","ey","uy","y"]
    for ending in endings_dict: 
        for into in into_dict: 
            if input_word.endswith(tuple(ext)): 
                result=input_word.replace(ending, into) 
                print(result) 
                
replace()
        

        
    