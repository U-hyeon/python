import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import librosa.display
import librosa
import soundfile as sf
import time

from concurrent.futures import ThreadPoolExecutor

BOUNDARY = 0.85
'''
# ------------------------------------------------
os.chdir("/Users/jeon-uhyeon/Desktop/final_project/dataset")
os.getcwd()
# wav_data, sample_rate = open_wav_with_resample(file_name, 'float32', sample_rate, 44100)
wav_data, sample_rate = open_wav(file_name, sample_rate)
edited_data = split_wav(wav_data, sample_rate, 3, 5)
result_file_name = 'result.wav'
librosa.output.write_wav(result_file_name, edited_data, sample_rate)
'''

def same_text_from_front(str1, str2):
    n = min(len(str1), len(str2))
    for i in range(n):
        if str1[i] != str2[i]:
            if i==0:
                return False, str1
            else:
                return str1[:i], str1[i:]
    if n == len(str1):
        return str1, False
    else:
        return str2, str1[n:]

def split_new_wav(A, sr, hop_length, start_frame, end_frame, dir_name): # ndarray(mfcc), start frame, end frame
    # 추출할 데이터 범위 계산
    start_sample = start_frame * hop_length
    end_sample = end_frame * hop_length

    # 데이터 추출
    extracted_data = A[start_sample:end_sample]

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    index = 0
    for i in range(1,100): # index 결정
        temp_name = str(i) + ".wav"
        if not os.path.exists( os.path.join(dir_name, temp_name) ):
            index = i
            break

    file_name = os.path.join(dir_name, str(index) + ".wav")
    print("new file name : ", file_name)
    print("extracted : frame ", start_frame, "~", end_frame, ", length = ", extracted_data.shape)
    sf.write(file_name , extracted_data, sr)

def extend_column_with_silence(arr, column): # shape 통일을 위해 신호의 뒤쪽에 무음구간을 추가
    '''
    # 새로운 열 추가
    new_col = np.zeros((arr.shape[0], column))
    new_col[0, :] = -6.48458313e+02

    # 배열과 새로운 열을 합침
    new_arr = np.concatenate((arr, new_col), axis=1)
    new_arr[:, -1][1:] = 0.0
    '''

    # 모든 값이 0인 새로운 배열 생성
    new_col = np.zeros((arr.shape[0], column))
    # 배열과 새로운 열을 합침
    new_arr = np.concatenate((arr, new_col), axis=1)

    return new_arr

def extend_array_set(A, B): # shape 통일
    max_a2_b2 = np.maximum(A.shape[1], B.shape[1])
    min_a2_b2 = np.minimum(A.shape[1], B.shape[1])
    # print("reshape by (min a2 b2 = ", min_a2_b2, ", max a2 b2 = ", max_a2_b2, ")")

    ex_col = max_a2_b2 - min_a2_b2

    if A.shape[1] == B.shape[1]:  # shape이 일치
        pass
    elif A.shape[1] == min_a2_b2:  # A의 shape이 더 작다
        A_rsp = extend_column_with_silence(A, ex_col)
        B_rsp = B
        # print("MFCC A_rsp : \n", A_rsp)
        return A_rsp, B_rsp
        pass
    else:  # B의 shape이 더 작다
        A_rsp = A
        B_rsp = extend_column_with_silence(B, ex_col)
        # print("MFCC B_rsp : \n", B_rsp)
        return A_rsp, B_rsp
        pass

    return A, B


#----------------------위쪽은 완성된코드-----------------------------
#---------------------아래쪽은 미완성된코드----------------------------

def total_align(A,B):
    r_sim: float = -1
    temp_A_start = 0
    temp_B_start = 0
    A_point: int = 0
    B_point: int = 0

    r_sim, A_point, B_point = total_sim(A,B)
    while(r_sim > BOUNDARY) and (A_point < A.shape[1]) and (B_point < B.shape[1]):
        temp_A_start = temp_A_start + A_point
        temp_B_start = temp_B_start + B_point
        if not ( (temp_A_start < A.shape[1]) and (temp_B_start < B.shape[1]) ):
            r_sim, A_point, B_point = total_sim( A[:, temp_A_start:],B[:, temp_B_start:] )
        else:
            return r_sim, A_point

    return r_sim, A_point

def total_sim(A, B): # 전체 유사도 (numpy.ndarray, numpy.ndarray)
    # 초기화
    r_sim = -1

    '''
    # 직선적 탐색
    A_point = 1
    temp_sim_A = -1
    r_B_point: int = 0
    for len_A in range(A.shape[1]):
        temp_sim_B = -1
        temp_B_point = 0
        for len_B in range(B.shape[1]):
            for speed in np.arange(0.1, 3.0, 0.1):  # 0.1 ~ 3배속, 0.1 단위
                B_stretch = librosa.effects.time_stretch(B[:, :len_B], rate=speed)
                temp = cos_sim(A[:, :len_A], B_stretch)
                if temp_sim_B < temp:
                    temp_sim_B = temp
                    temp_B_point = len_B
        if temp_sim_A < temp_sim_B:
            temp_sim_A = temp_sim_B
        if temp_sim_A > 1:
            print("sim error with ", temp_sim_A)
        else:
            if temp_sim_A > r:
                r = temp_sim_A
            if temp_sim_A > BOUNDARY:
                A_point = len_A
                r_B_point = temp_B_point
    '''

    temp_sim_A = -1
    temp_sim_B = -1
    temp_sim_stretch: float = -1
    temp = -1

    A_half : int = A.shape[1] / 2
    A_point : int = A.shape[1] / 2
    B_point: int = B.shape[1] / 2
    r_B_point: int = 0

    print("\nA_point:", A_point, end=" > ")
    while(A_half > 1):
        # 루프시작과 동시에 각 변수 초기화
        A_half = int(A_half / 2)
        B_point = 0
        temp_sim_B = -1

        for len_B in np.arange(0, B.shape[1], 4):
            for speed in np.arange(0.1, 3.0, 0.1): # 0.1 ~ 3배속, 0.1 단위
                B_stretch = librosa.effects.time_stretch(B[:, :len_B], rate=speed)
                temp_sim_stretch = cos_sim(A[:, :int(A_point)], B_stretch)
                if temp_sim_B < temp_sim_stretch:
                    temp_sim_B = temp_sim_stretch

            if  temp_sim_B >= BOUNDARY :
                temp_sim_A = temp_sim_B
                B_point = len_B

        if temp_sim_A >= BOUNDARY:  # 기준치보다 크면 더 많은부분을 포함해본다.
            A_point = A_point + A_half
        else: # 기준치보다 작다면 더 적은 부분을 포함해본다.
            A_point = A_point - A_half
        r_B_point = B_point
        print(A_point, end=" > ")

    # temp = cos_sim(A, B_stretch)
    if (temp_sim_A > 1): print("\ntemp_sim : ", temp_sim_A, end="\n")
    if (temp_sim_A > r_sim): r_sim = temp_sim_A
    # '''

    print("r=",r_sim,", A_point=", A_point)
    return r_sim, A_point, r_B_point

def cos_sim(A, B): # (numpy.ndarray, numpy.ndarray) 유사도 출력함수
    # 초기화
    r = -1
    temp: float = -1

    # shape 통일
    A_rsp, B_rsp = extend_array_set(A, B)

    # 출력 after reshape
    # librosa.display.specshow(A_rsp, sr=22050, hop_length=512, x_axis='time')
    # plt.show()
    # librosa.display.specshow(B_rsp, sr=22050, hop_length=512, x_axis='time')
    # plt.show()
    '''
    for i in range( -(A_rsp.shape[1]), A_rsp.shape[1] ): # 특징벡터 A time shift
        A_shift = np.roll(A_rsp, i, axis=1) # 특징벡터 A_stretch 에 대한 nparray 를 열에 대하여 i 만큼 shift
        A_flat = A_shift.flatten() # 유사도 계산을 위해 1차원 배열로 변환
        B_flat = B_rsp.flatten() # 유사도 계산을 위해 1차원 배열로 변환

        # 유사도 계산1
        up = np.dot(A_flat, B_flat) # 내적 = 분자
        abs_a = np.linalg.norm(A) # 벡터의 크기(스칼라)
        abs_b = np.linalg.norm(B) # 벡터의 크기(스칼라)
        # print("abs : ", abs_a, abs_b)
        down = abs_a * abs_b # 분모
        if (down==0):
            temp = -1
        temp = up/down # 유사도 계산

        # # 유사도 계산2
        # # 각 벡터의 크기 계산
        # norm_A = np.linalg.norm(A_shift, axis=1, keepdims=True)
        # norm_B = np.linalg.norm(B_rsp, axis=1, keepdims=True)
        # # 코사인 유사도 계산
        # temp = np.sum(A_shift * B_rsp, axis=1, keepdims=True) / (norm_A * norm_B)
    
        # 각 루프중 최대값 선택
        if temp > r:
            r = temp
    '''
    with ThreadPoolExecutor() as executor:
        results = []
        for i in range(-(A_rsp.shape[1]), A_rsp.shape[1]):
            results.append(executor.submit(compute_similarity, A_rsp, B_rsp, i))

        for future in results:
            result = future.result()
            if result > r:
                r = result
    # '''

    return r

def compute_similarity(A_rsp, B_rsp, i):
    A_shift = np.roll(A_rsp, i, axis=1)
    A_flat = A_shift.flatten()
    B_flat = B_rsp.flatten()

    up = np.dot(A_flat, B_flat)
    abs_a = np.linalg.norm(A_rsp)
    abs_b = np.linalg.norm(B_rsp)
    down = abs_a * abs_b
    if down == 0:
        temp = -1
    temp = up / down

    return temp

# ----------------- [main] ---------------
#
# def main(text1, text2):
#   pass

#-------------------------------------

start = time.time() # 시작시간 저장

path = "/Users/jeon-uhyeon/Desktop/final_project/dataset"
os.chdir(path)

text1 = "ㄱㅏㅅㅜ" # 음소분리를 진행할 데이터셋 이름
text2 = "ㄱㅏㅅㅣㄱㅗㄱㅣ" # 비교군 이름

# main(text1, text2)

text_new_front, text_new_back = same_text_from_front(text1, text2)

print("첫번째 텍스트 정보 : " + text1)
print("두번째 텍스트 정보 : " + text2)


if text_new_front != False:
    print("공통된 텍스트 정보 : " + text_new_front)

    for index1 in range(1,100):
        A_split_point : int = 15 # 분할지점 프레임 변수

        index_new = 1

        f_name1 = str(index1) + ".wav"
        path1 = os.path.join(text1, f_name1)  # 파일선택

        if os.listdir(text1) == []:
            shutil.rmtree(text1)
            print("폴더 삭제 완료")

        if not os.path.exists(path1):
            print("there is no such file : " + path1)
            shutil.rmtree(text1)
            print("빈 폴더 삭제 완료")
            break

        for index2 in range(1, 100):
            f_name2 = str(index2) + ".wav"
            path2 = os.path.join(text2, f_name2) # 비교파일선택
            if not os.path.exists(path2): # 비교파일 없으면
                print("there is no such file : " + path2)
                break
            # sample_rate=16000

            # Load the example clip
            A, sr1 = librosa.load(path1)
            B, sr2 = librosa.load(path2)
            print(type(A), sr1)
            # print(A.shape)

            # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
            hop_length = 128
            sim = -1

            start1 = 0
            end1 = 0

            # Compute MFCC features from the raw signal
            mfcc_A = librosa.feature.mfcc(y=A, sr=sr1, hop_length=hop_length, n_mfcc=13)
            # librosa.display.specshow(mfcc_A, sr=sr1, hop_length=hop_length, x_axis='time')
            # plt.show()

            mfcc_B = librosa.feature.mfcc(y=B, sr=sr2, hop_length=hop_length, n_mfcc=13)
            # librosa.display.specshow(mfcc_B, sr=sr2, hop_length=hop_length, x_axis='time')
            # plt.show()

            print("shape = ", mfcc_A.shape)
            temp: float = -1
            temp, A_split_point = total_align(mfcc_A, mfcc_B)
            print ("temp = ", temp, ", A length = ", mfcc_A.shape[1], ", split point = ", int(A_split_point))
            if temp > sim:
                sim = temp

            print("similarity : ", sim)

        if sim > BOUNDARY:
            # 지정된 구간을 이용하여 A-데이터셋 음소분할진행
            split_new_wav(A, sr1, hop_length, 0, int(A_split_point), text_new_front)
            split_new_wav(A, sr1, hop_length, int(A_split_point), mfcc_A.shape[1], text_new_back)
            os.remove(path1)

else:
    print("No Same Text!")

print("\n작업 소요시간 :", time.time() - start, " sec")  # 현재시각 - 시작시간 = 실행 시간 (단위 : 초)

'''
text1 = "가수-50-150len" # 음소분리를 진행할 데이터셋 이름
text2 = "가수-150-org" # 비교군 이름

path1 = os.path.join("ㄱㅏㅅ", "12.wav")

# Load the example clip
A, sr1 = librosa.load(path1)
# A, sr1 = librosa.load(text1 + ".wav")
B, sr2 = librosa.load("가수-50-org.wav")
# B, sr2 = librosa.load(text2 + ".wav")

# A,B = extend_array_set(A, B)

hop_length = 512
# Compute MFCC features from the raw signal
mfcc_A = librosa.feature.mfcc(y=A, sr=sr1, hop_length=hop_length, n_mfcc=13)

mfcc_B = librosa.feature.mfcc(y=B, sr=sr2, hop_length=hop_length, n_mfcc=13)

s1 = mfcc_A[:, :20]
s2 = mfcc_B[:, :20]

t1, t2 = extend_array_set(mfcc_A, mfcc_B)

librosa.display.specshow(t1, sr=sr1, hop_length=hop_length, x_axis='time')
plt.show()
librosa.display.specshow(t2, sr=sr2, hop_length=hop_length, x_axis='time')
plt.show()

print("mfcc_A")
print(s1)
print("mfcc_B")
print(s2)

sim = -1
sim = cos_sim(s1, s2)

print(t1.shape, t2.shape)
print("sim = ", type(sim), sim)

for i in range(0,13):
    print( t1[i][20] )
'''