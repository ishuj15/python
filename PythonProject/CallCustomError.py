import  custom_error
from custom_error import CustomError

n=-5
if n<0:
    raise CustomError("Negative number",500)
else:
    print("Valid number")