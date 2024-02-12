from fastapi import HTTPException


async def str_validation(sentence):
    if sentence.strip() == "" or is_number(sentence):
        raise HTTPException(status_code=400, detail="Invalid string")
    

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False