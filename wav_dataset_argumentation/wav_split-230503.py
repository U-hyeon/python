# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.


import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import librosa.display
import librosa
import soundfile as sf
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

def split_new_wav(A, sr, hop_length, start_frame, end_frame, dir_name): # ndarray(mfcc), start frame, end frame
    # 추출할 데이터 범위 계산
    start_sample = start_frame * hop_length
    end_sample = end_frame * hop_length

    # 데이터 추출
    extracted_data = A[start_sample:end_sample]

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    index = 0
    for i in range(1,100):
        temp_name = str(i) + ".wav"
        print(temp_name)
        if not os.path.exists( os.path.join(dir_name, temp_name) ):
            index = i
            break

    file_name = str(index) + ".wav"
    sf.write( ( os.path.join(dir_name, file_name) ), extracted_data, sr)


#----------------------위쪽은 완성된코드-----------------------------
#---------------------아래쪽은 미완성된코드----------------------------


def total_sim(A, B): # 전체 유사도 (numpy.ndarray, numpy.ndarray)
    # 초기화
    r = -1

    for speed in np.arange(0.1, 3.0, 0.1): # 0.1 ~ 3배속, 0.1 단위
        B_stretch = librosa.effects.time_stretch(B, rate=speed)
        # temp_sim_A = -1
        temp_sim_B = -1
        temp = -1
        A_half : int = A.shape[1] / 2
        A_point : int = A.shape[1] / 2

        while(A_half > 1):
            # 루프시작과 동시에 각 변수 초기화
            A_half = int(A_half / 2)
            B_half : int = B_stretch.shape[1] / 2
            B_point : int = B_stretch.shape[1] / 2
            temp_sim_B = -1

            while(B_half > 1):
                B_half = B_half / 2
                temp = cos_sim(A[:, :int(A_point)], B_stretch[:, :int(B_point)])
                if  temp > temp_sim_B :
                    temp_sim_B = temp
                    B_point = B_point + B_half
                else:
                    B_point = B_point - B_half

            if temp >= 0.9:  # 기준치 = 0.9
                A_point = A_point + A_half
            else:
                A_point = A_point - A_half

        temp = cos_sim(A, B_stretch)

        if (temp > r): r = temp
    return r, A_point

def cos_sim(A, B): # (numpy.ndarray, numpy.ndarray) 유사도 출력함수
    # 초기화
    r = -1

    # shape 통일
    A_rsp, B_rsp = extend_array_set(A, B)

    # 출력 after reshape
    # librosa.display.specshow(A_rsp, sr=22050, hop_length=512, x_axis='time')
    # plt.show()
    # librosa.display.specshow(B_rsp, sr=22050, hop_length=512, x_axis='time')
    # plt.show()

    """
    A_rsp = np.reshape(A[:, :min_a2_b2], (A.shape[0], min_a2_b2))
    B_rsp = np.reshape(B[:, :min_a2_b2], (B.shape[0], min_a2_b2))
    """
    '''
    A_rsp = np.reshape(A[:, :min_a2_b2], (A.shape[0], min_a2_b2))
    B_rsp = np.reshape(B[:, :min_a2_b2], (B.shape[0], min_a2_b2))
    '''

    for i in range( -(A_rsp.shape[1]), A_rsp.shape[1] ): # 특징벡터 A time shift
        A_shift = np.roll(A_rsp, i, axis=1) # 특징벡터 A_stretch 에 대한 nparray 를 열에 대하여 i 만큼 shift
        A_flat = A_shift.flatten() # 유사도 계산을 위해 1차원 배열로 변환
        B_flat = B_rsp.flatten() # 유사도 계산을 위해 1차원 배열로 변환

        # 유사도 계산
        up = np.dot(A_flat, B_flat) # 내적 = 분자
        abs_a = np.linalg.norm(A) # 벡터의 크기(스칼라)
        abs_b = np.linalg.norm(B) # 벡터의 크기(스칼라)
        # print("abs : ", abs_a, abs_b)
        down = abs_a * abs_b # 분모
        temp = up/down # 유사도 계산

        # 각 루프중 최대값 선택
        if temp > r : r = temp
    return r

# ----------------- [main] ---------------

# os.path.join(new_dir_name, file_name)
os.chdir("/Users/jeon-uhyeon/Desktop/final_project/dataset")

text1 = "ㄱㅏㅅㅜ" # 음소분리를 진행할 데이터셋 이름
text2 = "ㄱㅏㅅㅣㄱㅗㄱㅣ" # 비교군 이름
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
            if not os.path.exists(path2):
                print("there is no such file : " + path2)
                break
            # sample_rate=16000

            # Load the example clip
            A, sr1 = librosa.load(path1)
            B, sr2 = librosa.load(path2)
            print(type(A), sr1)
            print(A.shape)

            # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
            hop_length = 512
            sim = -1

            start1 = 0
            end1 = 0
            '''
            # time stretch
            for speed in np.arange(0.1, 3.0, 0.1):
                B_stretch = librosa.effects.time_stretch(B, rate=speed)
                
                # Separate harmonics and percussives into two waveforms
                # A_harmonic, A_percussive = librosa.effects.hpss(A)
                # B_harmonic, B_percussive = librosa.effects.hpss(B_stretch)
                #
                # # Beat track on the percussive signal
                # tempo1, beat_frames1 = librosa.beat.beat_track(y=A_percussive, sr=sr1)
                # tempo2, beat_frames2 = librosa.beat.beat_track(y=B_percussive, sr=sr2)
                
                # Compute MFCC features from the raw signal
                mfcc_A = librosa.feature.mfcc(y=A, sr=sr1, hop_length=hop_length, n_mfcc=13)
                # librosa.display.specshow(mfcc_A, sr=sr1, hop_length=hop_length, x_axis='time')
                # plt.show()

                mfcc_B = librosa.feature.mfcc(y=B_stretch, sr=sr2, hop_length=hop_length, n_mfcc=13)
                # librosa.display.specshow(mfcc_B, sr=sr2, hop_length=hop_length, x_axis='time')
                # plt.show()
            '''
            # Compute MFCC features from the raw signal
            mfcc_A = librosa.feature.mfcc(y=A, sr=sr1, hop_length=hop_length, n_mfcc=13)
            # librosa.display.specshow(mfcc_A, sr=sr1, hop_length=hop_length, x_axis='time')
            # plt.show()

            mfcc_B = librosa.feature.mfcc(y=B, sr=sr2, hop_length=hop_length, n_mfcc=13)
            # librosa.display.specshow(mfcc_B, sr=sr2, hop_length=hop_length, x_axis='time')
            # plt.show()

            temp, A_split_point = total_sim(mfcc_A, mfcc_B)
            print (temp, A_split_point)
            if temp > sim:
                sim = temp

            print("similarity : ", sim)

        # 지정된 구간을 이용하여 A-데이터셋 음소분할진행
        split_new_wav(A, sr1, hop_length, 0, int(A_split_point), text_new_front)
        split_new_wav(A, sr1, hop_length, int(A_split_point), mfcc_A.shape[1], text_new_back)
        os.remove(path1)

else:
    print("No Same Text!")