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

def UpsamplingNearest2d(matrix2D:np.ndarray)->np.ndarray:
    """Gap doi matrix2D voi cac du lieu la du lieu gan nhat ben 
    trai cua no"""
    m,n=matrix2D.shape
    output_array=np.zeros((m * 2, n * 2))
    for i in range(m):
        for j in range(n):
            output_array[i*2, j*2] = matrix2D[i, j]  
            output_array[i*2+1, j*2] = matrix2D[i, j]  
            output_array[i*2, j*2+1] = matrix2D[i, j]  
            output_array[i*2+1, j*2+1] = matrix2D[i, j]  
    return output_array
##############DO NOT MODIFY THIS PART#######################
def main():
    file_path = input("Enter file path:")
    matrix,_ = read_file(file_path)
    print("OUTPUT:")
    result = UpsamplingNearest2d(matrix)
    if result is not None:
        for row in result:
            print(row)
if __name__=="__main__":
    main()
##############END OF MAIN#######################