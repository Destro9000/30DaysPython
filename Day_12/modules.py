'''
    Write a function which generates a six digit/character random_user_id.

      print(random_user_id()) 
      '1ee33d'

    Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

    Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

Exercises: Level 2

    Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
    Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
    Write a function generate_colors which can generate any number of hexa or rgb colors.

   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

Exercises: Level 3

    Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
    Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
'''

#____Exercise 1_____


from random import choice, choices, randint ,shuffle, sample

# Pool of characters an ID can be built from: a-z, A-Z and 0-9
CHARACTERS = string.ascii_letters + string.digits
CHARACTERS_2 = '0123456789ABCDEF'

def random_user_id(length=6):
    return "".join(choices(CHARACTERS, k=length))



'''
def user_id_gen_by_user():
  
  length_id = int(input("Enter the length of the id:"))
  times = int(input('Enter the number of times: '))
  
  for _ in range(times):
    print("".join(choices(CHARACTERS, k=length_id))) 


user_id_gen_by_user()'''

def rgb_color_gen():
  return f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'

print(rgb_color_gen())

def list_of_hexa_colors(number):
  
  return [f"#{''.join(choices(CHARACTERS_2, k=6))}" for _ in range(number)]

print(list_of_hexa_colors(2))

def list_of_rgb_colors(number):
  return [f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})" for _ in range(number)]

print(list_of_rgb_colors(7))

def generate_colors(type, number):
  
  
  if(type == 'rbg'):
    return [f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})" for _ in range(number)]
  elif type == 'hexa':
    return [f"#{''.join(choices(CHARACTERS_2, k=6))}" for _ in range(number)]
  else:
    return 'Not a proper type!!!'

print(generate_colors('h', 4))


def shuffle_list(lst):
  return sample(lst, len(lst))

