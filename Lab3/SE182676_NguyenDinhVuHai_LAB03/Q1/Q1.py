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

def Conv2d(matrix2D:np.ndarray,filter:np.ndarray)->np.ndarray:
    """Tinh bo loc 2 chieu cho matrix su dung filter,
    coi nhu matrix co chieu la RxC va filter co so chieu la 3x3
    Apply filter cho matrix tren voi filter, chu y padding zero 
    cho matrix truoc khi filter, ket qua tra ve output co cung 
    kich thuoc voi input"""
    pad_matrix = np.pad(matrix2D,[(1,1),(1,1)],mode='constant',constant_values=0)
    m,n = filter.shape
    if (m == n):
        y,x = pad_matrix.shape
        y=y-m+1
        x=x-m+1
        new_matrix = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_matrix[i][j] = np.sum(pad_matrix[i:i+m,j:j+m]*filter)
    return new_matrix
##############DO NOT MODIFY THIS PART#######################
def main():
    file_path = input("Enter a file:")
    matrix,filter_matrix = read_file(file_path)
    print("OUTPUT:")
    result = Conv2d(matrix,filter_matrix)
    # print(result)
    if result is not None:
        for row in result:
            print(row)

if __name__=="__main__":
    main()
##############END OF MAIN#######################

