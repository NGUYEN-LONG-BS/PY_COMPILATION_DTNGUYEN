import xlwings as xw
import numpy as np

data = np.random.rand(40,40)
print(data)
xw.view(data)       # Trên Windown thì sẽ không lỗi, trên Macos thì lỗi (phải bật file Excel lên mới không bị lỗi)
