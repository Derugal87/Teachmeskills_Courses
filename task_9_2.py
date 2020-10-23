print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(one=1, two=2, three=3))



# def main(**kwargs):
#     return{key * 2:value for key,value in kwargs.items()}
#
# print(main(a=1, b=2))

