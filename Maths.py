class Maths():
    def multiplication_table(self,number):
        for x in range(100):
            print(x,'x',number,'=',number*x)


    def square_table(self,number):
        for x in range(number):
            print(x,'^','2','=',x*x)

    def cube_table(self,number):
        for x in range(number):
            print(x,'^','3','=',x*x*x)



    def square (self,length,breadth):
        print('Area or Perimetere')
        a = input('> ').lower()
        if a == 'area':
            l = int(input('Enter Length'))
            length = l
            b =int(input('Enter Breadth'))
            breadth = b
            output = length*breadth
            print('Area = ', output ,'cm^2' )
        elif a == 'breadth':
            l = int(input('Enter Length'))
            length = l
            b =int(input('Enter Breadth'))
            breadth = b
            output = length*breadth
            print(2*(l+b))










