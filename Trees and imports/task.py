class tree:
  def name (self):
    ads=str(input("Введите название дерева\n"))
    return ads
  
  def high (self):
    cas=int(input("введите высоту дерева\n"))
    if cas<0.5:
      cas=0.5
    return cas

  def age (self):
    cas=int(input("введите возраст дерева\n"))
    if cas<0:
      cas=0
    return cas
  
  def lifeexpectancy (self):
    cas=int(input("сколько лет будер расти ваше дерево ?\n"))
    if 1>cas:
      cas=1
    return cas
  
  def grow (self,name,high,age,lifeexpectancy,c):
    import first
    from random import uniform
    self.name=name
    self.high=high
    self.age=age
    self.lifeexpectancy=lifeexpectancy
    self.c=c
    high=round(high, 1)
    if c>lifeexpectancy:
      print (f"{name} прожил долгую жизнь, а именно {age} лет. Его высота = {high} метров\n")
      exit()
    first.info(c,name,high,age,lifeexpectancy)
    duck=uniform(0.1,2.0)
    high=high+duck
    return self.grow (name,high,age+1,lifeexpectancy,c+1)

print ("Сейчас мы посадим дерево и будем наблюдать за тем, как оно растет !\n")
rock=tree()
name=rock.name()
high=rock.high()
age=rock.age()
lifeexpectancy=rock.lifeexpectancy()
c=0
rock.grow(name,high,age,lifeexpectancy,c)
