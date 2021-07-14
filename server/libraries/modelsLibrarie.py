def fnModelValidate(model, info):
    try:
        # if(type(info) == dict):
        for m in model:
            print(m)
            print(model[m])
            print(type(model[m]))
            if(type(model[m]) == dict):
                print('es un json')

        # for i in info:
        #     print(i) #parametros
        #     print(info[i]) #info
    except Exception as e:
        print('algo')