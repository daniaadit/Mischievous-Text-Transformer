import re 
from datetime import datetime
import random 

def original_suffix(day: int)-> str:
    if 11<=day % 100 <=13:
        return 'th'
    return {1:'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')


def transform_text(text: str)-> str: #transforms phone number  

    text = re.sub(r'\b\d{10}\b', '**********', text)
    text = re.sub(r'\b\d{5}-\d{5}','**********', text)

    date_pattern = r'\b(\d{2})-(\d{2})-(\d{4})\b'
    date_pattern = r'\b(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b'   

    def date_repl(m):
        day, month, year = m.group(1), m.group(2), m.group(3)
        try:
            dt = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")                 
            print(dt)
        except ValueError:
            return m.group(0) #date and time when invalid 
        day_int = dt.day
        suffix = original_suffix(day_int)
        return f"{day_int}{suffix} {dt.strftime('%B %Y')}"

    text = re.sub(date_pattern, date_repl, text)     

    text = re.sub(r'\bPython\b', '🐍Python', text)   
    return text 


if __name__ == "__main__":
    input_text = input("Enter text: ")
    print ("\nTransformed text:")
    print(transform_text(input_text)) 

