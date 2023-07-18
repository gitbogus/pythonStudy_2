from cerberus import Validator

Dan = input("단수를 입력하세요 : ")
if (Dan.lstrip("-").isdigit() != True):
    print("숫자를 입력해 주세요")
else:
    Dan = int(Dan)
    for i in range(1,10):
        schema = {'Dan':{'type':'integer'}, 'i':{'type':'integer','max':9}}
        Validation = Validator(schema)
        Data1 = {'Dan': Dan}
        Data2 = {'i': i}
        result = Validation.validate(Data1)
        result2 = Validation.validate(Data2)
        if (result == True and result2 == True):
            Gugulist = Dan * i
            print(Dan , "*" , i , "=" , Gugulist)
