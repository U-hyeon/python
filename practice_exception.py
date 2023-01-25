try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: # 숫자가 아니다
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err: # 해당 에러를 err이라는 변수로 사용
    print(err)

#except: # 예외처리된 에러가 아닌 모든 에러
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.") 
    print(err) # 해당 에러가 무엇인지 출력