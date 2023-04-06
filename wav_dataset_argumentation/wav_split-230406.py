# 샘플 Python 스크립트입니다.

# ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.


import numpy as np
import os
import matplotlib.pyplot as plt
import librosa.display
import librosa
import soundfile as sf
'''
file_name = 'test.wav'
sample_rate = 192000  # 192KHz
data_length = sample_rate * 60  # 192KHz * 60

def open_wav_with_resample(file_name, bit, origin_rate, new_rate):
  data, rate = sf.read(file_name, dtype=bit)
  data = data.T
  data = librosa.resample(data, origin_rate, new_rate)
  return data, new_rate

def open_wav(file_name, origin_rate):
  data, rate = librosa.load(file_name, sr=origin_rate)
  return data, rate

def split_wav(data, sample_rate, start, end):
    start *= sample_rate  # start : sec 단위
    end *= sample_rate  # end : sec 단위
    return data[start:end]

# ------------------------------------------------
os.chdir("/Users/jeon-uhyeon/Desktop/final_project/dataset")
os.getcwd()
# wav_data, sample_rate = open_wav_with_resample(file_name, 'float32', sample_rate, 44100)
wav_data, sample_rate = open_wav(file_name, sample_rate)
edited_data = split_wav(wav_data, sample_rate, 3, 5)
result_file_name = 'result.wav'
librosa.output.write_wav(result_file_name, edited_data, sample_rate)
'''

def cos_sim(A, B): # (numpy, numpy) 유사도 출력함수
    # 초기화
    r = -1

    # shape 통일
    min_a2_b2 = np.minimum(A.shape[1], B.shape[1])
    print("reshape by (min a2 b2 = ", min_a2_b2, ")")
    """
    A_rsp = np.reshape(A[:, :min_a2_b2], (A.shape[0], min_a2_b2))
    B_rsp = np.reshape(B[:, :min_a2_b2], (B.shape[0], min_a2_b2))
    """
    A_rsp = np.reshape(A, (A.shape[0], min_a2_b2))
    B_rsp = np.reshape(B, (B.shape[0], min_a2_b2))

    for i in range( -(A_rsp.shape[1]), A_rsp.shape[1] ): # 특징벡터 A time shift
        A_shift = np.roll(A_rsp, i, axis=1) # 특징벡터 A_stretch 에 대한 nparray 를 열에 대하여 i 만큼 shift
        A_flat = A_shift.flatten() # 유사도 계산을 위해 1차원 배열로 변환
        B_flat = B_rsp.flatten() # 유사도 계산을 위해 1차원 배열로 변환

        # 유사도 계산
        up = np.dot(A_flat, B_flat) # 내적 = 분자
        abs_a = np.linalg.norm(A) # 벡터의 크기(스칼라)
        abs_b = np.linalg.norm(B) # 벡터의 크기(스칼라)
        down = abs_a * abs_b # 분모
        temp = up/down # 유사도 계산

        # 각 루프중 최대값 선택
        if temp > r : r = temp
    return r

os.chdir("/Users/jeon-uhyeon/Desktop/final_project/dataset")
path1 = '가수-150.wav' # 파일선택
path2 = '가수-200.wav' # 비교파일선택
#sample_rate=16000

# Load the example clip
# y, sr = librosa.load(librosa.ex('nutcracker'))
y1, sr1 = librosa.load(path1)
y2, sr2 = librosa.load(path2)

# Set the hop length; at 22050 Hz, 512 samples ~= 23ms
hop_length = 512

# time stretch
'''
for speed in np.arange(0.1, 3.0, 0.1):
    y1_stretch = librosa.effects.time_stretch(y1, rate=speed)
'''
speed = 4/3
y1_stretch = librosa.effects.time_stretch(y1, rate=speed)

# Separate harmonics and percussives into two waveforms
y1_harmonic, y1_percussive = librosa.effects.hpss(y1_stretch)
y2_harmonic, y2_percussive = librosa.effects.hpss(y2)

# Beat track on the percussive signal
tempo1, beat_frames1 = librosa.beat.beat_track(y=y1_percussive, sr=sr1)
tempo2, beat_frames2 = librosa.beat.beat_track(y=y2_percussive, sr=sr2)

# Compute MFCC features from the raw signal
mfcc1 = librosa.feature.mfcc(y=y1_stretch, sr=sr1, hop_length=hop_length, n_mfcc=13)
print("SR : ", sr1)
print("MFCC shape : ", mfcc1.shape)
# print("MFCC : \n", mfcc1)
librosa.display.specshow(mfcc1, sr=sr1, hop_length=hop_length, x_axis='time')
plt.show()

mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2, hop_length=hop_length, n_mfcc=13)
print("SR : ", sr2)
print("MFCC shape : ", mfcc2.shape)
# print("MFCC : \n", mfcc2)
librosa.display.specshow(mfcc2, sr=sr2, hop_length=hop_length, x_axis='time')
plt.show()

# print("flatten")
# flat1 = mfcc1.flatten()
# flat2 = mfcc2.flatten()
# print("mfcc1 : ", flat1)
# print("mfcc2 : ", flat2)
# dot_p = np.dot(flat1, flat2)
# print("dot : ", dot_p)
# abs1 = np.linalg.norm(flat1)
# abs2 = np.linalg.norm(flat2)
# print("abs1 : ", abs1)
# print("abs2 : ", abs2)
print("similarity : ", cos_sim(mfcc1, mfcc2))

"""
# And the first-order differences (delta features)
mfcc1_delta = librosa.feature.delta(mfcc1)
mfcc2_delta = librosa.feature.delta(mfcc2)

# Stack and synchronize between beat events
# This time, we'll use the mean value (default) instead of median
beat_mfcc_delta1 = librosa.util.sync(np.vstack([mfcc1, mfcc1_delta]), beat_frames1)
beat_mfcc_delta2 = librosa.util.sync(np.vstack([mfcc2, mfcc2_delta]), beat_frames2)

# Compute chroma features from the harmonic signal
chromagram1 = librosa.feature.chroma_cqt(y=y1_harmonic, sr=sr1)
chromagram2 = librosa.feature.chroma_cqt(y=y2_harmonic, sr=sr2)

# Aggregate chroma features between beat events
# We'll use the median value of each feature between beat frames
beat_chroma1 = librosa.util.sync(chromagram1, beat_frames1, aggregate=np.median)
beat_chroma2 = librosa.util.sync(chromagram2, beat_frames2, aggregate=np.median)

# Finally, stack all beat-synchronous features together
beat_features1 = np.vstack([beat_chroma1, beat_mfcc_delta1])
beat_features2 = np.vstack([beat_chroma2, beat_mfcc_delta2])
"""