def fahrenheit(celsius):
        return str((9/5) * int(celsius) + 32)

celsius = int(input('섭씨온도를 입력하세요. : '))
print('섭씨'+ str(celsius) +'를 화씨로 변환 : ' + fahrenheit(celsius))
