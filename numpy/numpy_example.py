import numpy as np
import time

number=1000000

normal_list=list(range(number))
num_array=np.arange(number)

python_start_time=time.time()
for i in normal_list:
    normal_list[i]=i*i
python_exec_time=time.time()-python_start_time

print('python execution time is ',format(python_exec_time, '.2f'),'seconds')


numpy_start_time=time.time()
num_array=num_array**2
numpy_exec_time=time.time()-numpy_start_time

print('numpy execution time is ',format(numpy_exec_time, '.2f'),'seconds')

print('numpy is ',format(python_exec_time/numpy_exec_time, '.2f'),'times faster than python')

