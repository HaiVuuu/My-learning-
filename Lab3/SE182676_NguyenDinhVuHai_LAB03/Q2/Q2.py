#########Khong duoc dung thu vien nao khac ngoai cac thu vien nay###
import numpy as np
####################################################################
################## THU VIEN DOC FILE, KHONG SUA################

def read_file(path_file:str)->np.ndarray:
    """
    path_file: File to be read
    """
    # path_file = os.path.+path_file
    matrix=None 
    filter_matrix=None 
    with open(path_file,'r') as f_in:
        # 2 dong dau la row va col cua matrix 
        # cac dong sau la cua matrix 
        # 2 dong tiep la row va col cua filter 
        matrix_row = int(f_in.readline().strip())
        matrix_col = int(f_in.readline().strip())
        matrix = np.zeros((matrix_row,matrix_col))
        for n in range(matrix_row):
            matrix_row = f_in.readline().split()
            matrix[n] = np.array(matrix_row)
        filter_row = int(f_in.readline())
        filter_col = int(f_in.readline())
        filter_matrix = np.zeros((filter_row,filter_col))
        for n in range(filter_row):
            filter_row = f_in.readline().split()
            filter_matrix[n] = np.array(filter_row)
    return matrix,filter_matrix
    
###############################################################

def MaxPool2d(matrix2D:np.ndarray)->np.ndarray:
    """Su dung MaxPooling2D bang cach tim trong kernel_size
    gia tri lon nhat, chu y matrix2D khong padding, coi nhu 
    kernel_size=(2,2)"""
    m,n = matrix2D.shape
    x=2
    y=2
    mx=m//x
    ny=n//y
    print(matrix2D[:mx*x, :ny*y].reshape(mx,x,ny,y).max(axis=(1,3)))

##############DO NOT MODIFY THIS PART#######################
def main():
    file_path = input("Enter file path:")
    matrix,_ = read_file(file_path)
    print("OUTPUT:")
    result = MaxPool2d(matrix)
    if result is not None:
        for row in result:
            print(row)
if __name__=="__main__":
    main()
##############END OF MAIN#######################

