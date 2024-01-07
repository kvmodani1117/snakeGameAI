TO RUN THE PROJECT, use the below command : 
python agent.py 




**************************************************
python --version
Python 3.10.11

--------------------------------------------------
pip --version
pip 23.3.2 from C:\Users\kvmod\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

--------------------------------------------------
python
import torch
>>> torch.__version__
'2.1.2+cu118'

--------------------------------------------------
FOR CUDA VERSION : (I've used CUDA 11.8 version)
nvcc --version

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0

**************************************************




NOTE : I had to downgrade my python version to 3.10.11, because, pytorch's version ('2.1.2+cu118') wasn't compatible to the latest python's version!
YOU CAN CHECK THE OFFICIAL RELEASE COMPATIBILITY MATRIX HERE : https://github.com/pytorch/pytorch/blob/main/RELEASE.md