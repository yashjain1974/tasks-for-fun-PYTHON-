import datetime
def practise ():
  print("сейчас будет заполняться инфа по практическим работам в 1 семестре\n")
  count=0
  number=1
  for i in range (number):
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if  lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      return sdacha
    
    def timeo ():
      import datetime
      lala=[]
      a=input("введите дату защиты через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return timeo ()
      defence=datetime.datetime(lala[0],lala[1],lala[2])
      return defence

    def imporovise (sdacha,timeo):
      import datetime
      sdacha=sdacha
      timeo=timeo
      delta=timeo-sdacha
      time=delta.days
      time=int(time)
      if time<7:
        x=3
        return x
      elif time<14 and time>7:
        x=2
        return x
      elif time>=14:
        x=1
        return x
      else:
        x=0
        return x
    
    sdacha=time()
    timeo=timeo()
    duck=imporovise(sdacha,timeo)
    kadgit=str(duck)
    sdacha=str(sdacha)+"- дата выполнения практической работы | "
    timeo=str(timeo)+" - дата защиты практической работы. Баллы за работу - "+kadgit+" | "
    #dadad
    count=count+duck
 
 
  number=1
  for i in range (number):
    x=int(input(f"сколько у вас было за {i} контрольную работу ?\n"))
    count=count+x
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      sdacha=str(sdacha)+"| "
      return sdacha
    x=str(x)
    x="за контрольную баллов -"+x+" в эту дату - "
    konrol=time()
    kontol="Контрольная - "
    kontol=kontol+x
    kontol=kontol+konrol
    

  number=int(input("сколько у вас было тестирований в 1 семе ?\n"))
  testa="тесты - "
  for i in range (number):
    x=int(input(f"сколько вы получили за {i} тест ?\n"))
    count=count+x
    
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      sdacha=str(sdacha)+"| "
      return sdacha
    
    x=str(x)
    x=x+" баллов в эту дату - "
    kokol=time()
    testa=testa+x
    testa=testa+kokol 


  if count>20:
    count=20
  count=str(count)+" - столько баллов получил ученик в первой половине сема | "
  galk=str(duck)+" - столько баллов получил ученик за практическую работу | "
  result=count+galk+sdacha+timeo+kontol+testa
  return result,duck

def rabota ():
  count=0
  print("Сейчас будет заполняться инфа о праткических работах во втором семестре (само задание и защита). Если их было больше, то напишите об этом кодеру ( мне) и я все исправлю, но чисто по логике , обычно практических работ 1 шт на семестр. Я , конечно же могу записать все даты сдачь и защит , но зачем , если их лишь одна шт\n ")
  number=1
  for i in range (number):
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      return sdacha
    
    def timeo ():
      import datetime
      lala=[]
      a=input("введите дату защиты через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return timeo ()
      defence=datetime.datetime(lala[0],lala[1],lala[2])
      return defence

    def imporovise (sdacha,timeo):
      import datetime
      sdacha=sdacha
      timeo=timeo
      delta=timeo-sdacha
      time=delta.days
      time=int(time)
      if time<7:
        x=3
        return x
      elif time<14 and time>7:
        x=2
        return x
      elif time>=14:
        x=1
        return x
      else:
        x=0
        return x
    
    sdacha=time()
    timeo=timeo()
    duck=imporovise(sdacha,timeo)
    kadgit=str(duck)
    sdacha=str(sdacha)+"- дата выполнения практической работы | "
    timeo=str(timeo)+" - дата защиты практической работы. Баллы за работу - "+kadgit+" | "
    #dadad
    count=count+duck
 
 
  number=1
  for i in range (number):
    x=int(input(f"сколько у вас было за {i} контрольную работу ?\n"))
    count=count+x
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      sdacha=str(sdacha)+"| "
      return sdacha
    x=str(x)
    x="за контрольную баллов -"+x+" в эту дату - "
    konrol=time()
    kontol="Контрольная - "
    kontol=kontol+x
    kontol=kontol+konrol
    

  number=int(input("сколько у вас было тестирований в второй половине 1 сема ?\n"))
  testa="тесты - "
  for i in range (number):
    x=int(input(f"сколько вы получили за {i} тест ?\n"))
    count=count+x
    
    def time ():
      import datetime
      lala=[]
      a=input("введите дату выполнения через пробел. Сначала вводится год , потом месяц, а потом день\n").split(" ")
      for i in range (len(a)):
        a[i]=int(a[i])
        lala.append(a[i])
      if lala[0]<2000 or lala[1]>12 or lala[2]>31 :
        return time ()
      sdacha=datetime.datetime(lala[0],lala[1],lala[2])
      sdacha=str(sdacha)+"| "
      return sdacha
    
    x=str(x)
    x=x+" баллов в эту дату - "
    kokol=time()
    testa=testa+x
    testa=testa+kokol 


  if count>20:
    count=20
  count=str(count)+" - столько баллов получил ученик во второй половине сема | "
  galk=str(duck)+" - столько баллов получил ученик за практическую работу | "
  result=count+galk+sdacha+timeo+kontol+testa
  return result,duck            #сначала идет кол-во баллов за весь сем,баллы за экз, потом идет дата сдачи, потом дата защиты , потом балл и время сдачи контрольного тестирования , а в конце идет балл и дата сдачи теста
