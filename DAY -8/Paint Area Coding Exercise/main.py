import math

def paint_calc(height,width,cover): 
    can = math.ceil((test_h * test_w)/coverage) #ceil() help to round the number
    print(f"You need {can} for the wall ")  
    
test_h = int(input("Height Of The Wall : "))
test_w = int(input("Width of the Wall : "))
coverage = 5    
paint_calc(height = test_h,width=test_w,cover=coverage)