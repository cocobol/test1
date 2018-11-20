import numpy as np

training_data = []
a = 11
b = 1
for i1 in range(b, a-5):#40
    for i2 in range(i1+1, a-4):#41
        for i3 in range(i2+1, a-3):#42
            for i4 in range(i3+1, a-2):#43
                for i5 in range(i4+1, a-1):#44
                    for i6 in range(i5+1, a):#45
                        # 조건문 넣기
                        if i1+1 == i2 and i2+1 == i3 and i3+1 == i4 and i4+1 == i5 and i5+1 == i6:
                            continue
                        if i1+2 == i2 and i2+2 == i3 and i3+2 == i4 and i4+2 == i5 and i5+2 == i6:
                            continue

                        # 결과 저장 하기    
                        training_data.append([i1, i2, i3, i4, i5, i6])
                
                       
#print(training_data)
np.save('./drive/training_data.npy',training_data) # 저장

#print(training_data.index([1,2,3,4,5,7]))
print(training_data.count([1,2,3,4,5,7])) # 찾기
print('??? : ',len(training_data))


#training_data = list(np.load(file_name)) # 불러오기