def AB_minus():
    a=int(input('a= '))
    b=int(input('a= '))
    a, b=input('a와 b 값을 입력하시오 ').split()
    
    c= a-b
    print('a-b= ', a-b)
    print(type(c)) # 상태 확인
    
    AB_multiply(a,b)
    c=AB_div(a,b)
    
    print ('minus ={}, divide={} '.format(ret, c))