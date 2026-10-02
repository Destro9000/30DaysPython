'''
    Declare your age as integer variable
    Declare your height as a float variable
    Declare a variable that store a complex number
    Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

        Enter base: 20
        Enter height: 10
        The area of the triangle is 100

    Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

        Enter side a: 5
        Enter side b: 4
        Enter side c: 3
        The perimeter of the triangle is 12

    Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
    Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
    Calculate the slope, x-intercept and y-intercept of y = 2x -2
    Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
    Compare the slopes in tasks 8 and 9.
    Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
    Find the length of 'python' and 'dragon' and make a falsy comparison statement.
    Use and operator to check if 'on' is found in both 'python' and 'dragon'
    I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
    There is no 'on' in both dragon and python
    Find the length of the text python and convert the value to float and convert it to string
    Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
    Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
    Check if type of '10' is equal to type of 10
    Check if int('9.8') is equal to 10
    Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

        Enter hours: 40
        Enter rate per hour: 28
        Your weekly earning is 1120

    Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

        Enter number of years you have lived: 100
        You have lived for 3153600000 seconds.

    Write a Python script that displays the following table

        1 1 1 1 1
        2 1 2 4 8
        3 1 3 9 27
        4 1 4 16 64
        5 1 5 25 125

'''

age = 26
height_1 = 178.6
complex_num = 1 +1j


base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the base of the triangle: "))
area_of_triangle = (base * height) / 2
print("The area of the triangle is: ", area_of_triangle)


side_a = float(input("Enter the first side of the triangle: "))
side_b = float(input("Enter the second side of the triangle: "))
side_c = float(input("Enter the third side of the triangle: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter)

length = float(input("Enter the length of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
rect_area = length * height
rect_peri = length * 2 + height * 2 
print("The area of the rectangle is: ", rect_area)
print("The perimeter of the rectangle is: ", rect_peri)

radius = float(input("Enter the radius of the circle: "))
PI = 3.14
area_circle = radius ** 2 * PI
peri_circle = radius * 2 * PI
print("The area of the rectangle is: ", area_circle)
print("The perimeter of the rectangle is: ", peri_circle)

x1 = int(input("Enter the first x coordinate"))
y1 = 2*x1-2
print("The y coordinate is: ", y1)

x2 = int(input("Enter the first x coordinate"))
y2 = 2*x2-2
print("The y coordinate is: ", y2)

slope = (y2-y1)/(x2-x1)

x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10

slope = (y_2-y_1)/(x_2-x_1)

x = int(input("Enter the x value: "))
y = x**2 + 6*x + 9


print(not len('python') == len('dragon')) #false
print("on" in "python")
print("on" in "dragon")

sentence = " I hope this course is not full of jargon"

print("jargon" in sentence)

print('There is no on in dragon or python', not "on" in "dragon")


python = "python"
len_python = float(len(python))
string_len = str(len_python)

print('The length of the python word in fload is:', string_len)


number = int(input("Enter the number you want to evaluate"))

print("is the number even?", number%2 == 0)
print(7//3 == int(2.7))
print(type("10") == type(10))
print(10 == int(9.8))

hours = int(input('Enter the hours: '))
rate = int(input('Enter the rate per hour: '))
earnings = hours * rate
print("Your weekly earning are: ", earnings)

years = int(input("Enter the number of years you have lived: "))
total_in_seconds = 365 * 24 * 60 * years * 60
print("You lived a total of ", total_in_seconds, " seconds")