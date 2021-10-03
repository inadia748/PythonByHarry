#5. Can you change the self parameter inside a class to something else (say 'harry'). Try chaning self to 'slf' or 'harry' and see the effects.

class Sample:
   

    def __init__(slf, name):
        slf.name = name

obj = Sample('Nadia')
print(obj.name)
