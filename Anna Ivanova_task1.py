#!/usr/bin/env python
# coding: utf-8

# In[4]:


Phrase1="Казнить, нельзя помиловать!"
Phrase2="To be or not to be"
if len(Phrase1)> len(Phrase2):
    print ("Фраза 1 длиннее фразы 2")
elif len(Phrase1)< len(Phrase2):
    print ("Фраза 2 длинее фразы 1")
else:
    print ("Фразы одинаковой длины")


# In[5]:


Phrase1="Казнить, нельзя помиловать!"
Phrase2="To be or not to be. What is the question!"
if len(Phrase1)> len(Phrase2):
    print ("Фраза 1 длиннее фразы 2")
elif len(Phrase1)< len(Phrase2):
    print ("Фраза 2 длинее фразы 1")
else:
    print ("Фразы одинаковой длины")


# In[6]:


Phrase1="Казнить, нельзя помиловать!"
Phrase2="Казнить, нельзя помиловать!"
if len(Phrase1)> len(Phrase2):
    print ("Фраза 1 длиннее фразы 2")
elif len(Phrase1)< len(Phrase2):
    print ("Фраза 2 длинее фразы 1")
else:
    print ("Фразы одинаковой длины")


# In[11]:


year=int (input ('Введите год '))
if year % 4 == 0:
    print ('Високосный год')
else:
    print ('Обычный год')


# In[32]:


date=int (input ('Введите дату '))
month=(input ('Введите месяц '))
if date >=21 and month=='Январь' or date<=19 and month=='Февраль':
    print ('Ваш знак зодиака: Водолей')
elif date >=20 and month =='Февраль' or date <=20 and month =='Март':
    print ('Ваш знак зодиака: Рыба')
elif date >=22 and month=='Декабрь' or date<=20 and month=='Январь':
    print ('Ваш знак зодиака: Козерог')
elif date >=22 and month=='Ноябрь' or date<=21 and month=='Декабрь':
    print ('Ваш знак зодиака: Стрелец')
elif date >=23 and month=='Октябрь' or date<=21 and month=='Ноябрь':
    print ('Ваш знак зодиака: Скорпион')
elif date >=23 and month=='Сентябрь' or date<=22 and month=='Октябрь':
    print ('Ваш знак зодиака: Весы')
elif date >=24 and month=='Август' or date<=22 and month=='Сентябрь':
    print ('Ваш знак зодиака: Дева')
elif date >=23 and month=='Июль' or date<=23 and month=='Август':
    print ('Ваш знак зодиака: Лев')
elif date >=22 and month=='Июнь' or date<=22 and month=='Июль':
    print ('Ваш знак зодиака: Рак')
elif date >=22 and month=='Май' or date<=21 and month=='Июнь':
    print ('Ваш знак зодиака: Близнецы')
elif date >=21 and month=='Апрель' or date<=21 and month=='Май':
    print ('Ваш знак зодиака: Телец')
else:
    print ('Ваш знак зодиака: Овен')


# In[24]:


width = int (input ('Введите ширину в см '))
length = int (input ('Введите длину в см '))
height = int (input ('Введите высоту в см '))
if width <= 15 and length <= 15 and height <= 15:
    print ('Коробка №1')
elif width > 15 and width <=50 or length>15 and length<=50 or height>15 and height <=50:
    print ('Коробка №2')
elif length >= 200:
    print ('Упаковка для лыж')
else:
    print ('Стандартная коробка №3')
    


# In[33]:


ticket_number=int (input ( 'Введите шестизначный номер билета '))

ticket_number1 = ticket_number//100000
ticket_number2 = (ticket_number%100000)//10000
ticket_number3 = (ticket_number%10000)//1000
ticket_number4 = (ticket_number%1000)//100
ticket_number5 = (ticket_number%100)//10
ticket_number6 = (ticket_number%10)
if ticket_number1+ticket_number2+ticket_number3 == ticket_number4+ticket_number5+ticket_number6:
    print ('Поздравляю, у Вас счастливый билет!')
else:
    print ('Увы, удача Вам обязательно улыбнется, но в другой раз!')


# In[46]:


figure = input('Введите фигуру: круг, треугольник или прямоугольник? ')
if figure==('круг'):
    radius = int (input('Введите радиус круга '))
    print ('Площадь круга=',3.14*radius)
elif figure==('треугольник'):
    l1 = int (input('Введите длину строны a '))
    l2 = int (input('Введите длину строны b '))
    l3 = int (input('Введите длину строны c '))
    p = (l1+l2+l3)/2
    print ('Площадь треугольника=',(((p-l1)*(p-l2)*(p-l3)*p)*0.5))
elif figure==('прямоугольник'):
    l1 = int (input('Введите длину строны a '))
    l2 = int (input('Введите длину строны b '))
    print ('Площадь прямоугольника=',l1*l2)


# In[ ]:




