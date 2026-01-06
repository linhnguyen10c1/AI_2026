import math 
def is_number(n):
  try: 
    float(n)
    return True
  except ValueError:
    return False
  
def calc_activation_func(x, act_name):
  # x là số đầu vào, act_name tên hàm kích hoạt 
    if not is_number(x):
      print ("x must be a number")
      return 
    x = float(x)
    alpha = 0.01
    result = 0;
    if act_name == 'sigmoid':
      result =  1/ (1 + math.e**(-x))
    elif act_name == 'relu':
      if(x <= 0 ): result = 0
      else: result = x
    elif act_name == 'elu':
      if(x<= 0): result = alpha * (math.e**x - 1)
      else: result = x
    else: 
      print(f"{act_name} is not supported")
      return
    print(f"{act_name}: f({x}) = {result}")

calc_activation_func(1.5, 'sigmoid')
calc_activation_func(-1, 'relu')
calc_activation_func(-1, 'elu')
calc_activation_func(3, 'belu')

