#인자의 순서를 다르게 지정할수있다.
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang = "파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")