import math
import random

def calculate_loss_function():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss_name = input("Input loss name (MAE, MSE, RMSE): ")
    total_loss = 0
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        loss = 0
        
        if loss_name == "MAE":
            loss = abs(target - predict)
            
        elif loss_name == "RMSE" or loss_name == "MSE" :
            loss = (target - predict) ** 2
            
        total_loss += loss
        print(f"loss_name: {loss_name}, sample: {i}, pred: {predict:.2f}, target: {target:.2f}, loss: {loss:.2f}")

    final_loss = 0
    
    if loss_name == "RMSE":
        final_loss = math.sqrt(total_loss / num_samples)
    else:
        final_loss = total_loss / num_samples
    print(f"final {loss_name}: {final_loss}")

calculate_loss_function()