import math
def F1_score_DanhGiaMoHinh(tp, fp, fn):
  # 1. Kiểm tra đầu vào có phải là số nguyên không 
  if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
    print ("Đầu vào phải là số nguyên.")
    return
  # 2. Kiểm tra có lơn hơn 0 
  if tp < 0 or fp < 0 or fn < 0:
    print ("Đầu vào phải lớn hơn hoặc bằng 0.")
    return
  # 3. Tính Precision và Recall và F1-score
  if tp + fp == 0:
    precision = 0
  else:
    precision = tp / (tp + fp)
  if tp + fn == 0:
    recall = 0
  else:
    recall = tp / (tp + fn)
  if precision + recall == 0:
    f1_score = 0
  else:
    f1_score = 2 * (precision * recall) / (precision + recall)
  print ("Precsion:", precision)
  print ("Recall:", recall)
  print ("F1-score:", f1_score) 
  
F1_score_DanhGiaMoHinh(tp=2, fp=3, fn=4)
F1_score_DanhGiaMoHinh(tp='a', fp=3, fn=4)
F1_score_DanhGiaMoHinh(tp=2.1, fp=3, fn=4)


