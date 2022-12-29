#Class Amusement Ride
class AmusementRide():

    def __init__(self,name,height,age,tickets):

        self.__name = name
        self.__minHeight = height
        self.__minAge = age
        self.__numTickets = tickets

    def set_name(self,name):
         self.__name = name

    def set_minHeight(self, height):
        self.__minHeight = height

    def set_minAge(self,age):
        self.__minAge = age

    def set_tickets(self,tickets):
         self.__numTickets = tickets
        
    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__minHeight

    def get_minAge(self):
        return self.__minAge

    def get_numTickets(self):
        return self.__numTickets

    def calc_cost(self,price,tickets):
        return price*self.__numTickets

    #If age and height meet requirements return true
    def can_give_ride(self,age,height):
        if age>=self.__minAge and height>=self.__minHeight:
            return True
        else:
            return False

    def __str__(self):
        return 'Name of Ride: '+ str(self.__name) + '\nMinimum Height: ' +str(self.__minHeight) + '\nMinimum Age: ' + str(self.__minAge) +'\nNumber of Tickets: ' +str(self.__numTickets)
        
def main():
    ride1()
    ride2()

def ride1():
    name='Roller Coaster'
    age= 11
    height= 5
    print('Welcome to the',name, end='')
    print('!')
    print()
    #collect number of tickets
    tickets=int(input('Enter the number of tickets:'))
    print()
    #set up object
    ride1 = AmusementRide(name,height,age,tickets)
    #print object info
    print(ride1.__str__())
    #ask for height
    userheight=float(input('Enter your Height:'))
    #validate height
    userheight=valid(userheight)
    #ask for age
    userage=int(input('Enter your age:'))
    #validate age
    userage=valid(userage)
    #results
    result=ride1.can_give_ride(userage,userheight)

    if result:
        #if true, calculate cost
        print('You can ride the ', ride1.get_name(),end='')
        print('!')
        price=float(input('Enter the price per ticket:'))
        print('Calculating the price for ',ride1.get_numTickets(),'tickets...' )
        print('Cost: $',ride1.calc_cost(price,tickets),sep='')

    else:
        #if false, print requirements
        print('Sorry, you are not eligible to ride.')
        print('The minimum age is ', ride1.get_minAge())
        print('The minimum height is ', ride1.get_height())


def ride2():
    print()
    name='Swings'
    age= 13
    height= 5.5
    print('Welcome to the',name, end='')
    print('!')
    print()
    #number of tickets requested
    tickets=int(input('Enter the number of tickets:'))
    ride2 = AmusementRide(name,height,age,tickets)
    print()
    #print ride info
    print(ride2.__str__())
    #user height and age
    userheight=float(input('Enter your Height:'))
    userheight=valid(userheight)
    userage=float(input('Enter your age:'))
    userage=valid(userage)
    #test for ride requirements 
    result=ride2.can_give_ride(userage,userheight)

    if result:
        #if pass:
        print('You can ride the ', ride2.get_name(),end='')
        print('!')
        price=float(input('Enter the price per ticket:'))
        print('Calculating the price for ',ride2.get_numTickets(),'tickets...' )
        print('Cost: $', ride2.calc_cost(price,tickets), sep='')
    else:
        #if dont pass requirements
        print('Sorry, you are not eligible to ride.')
        print('The minimum age is ', ride2.get_minAge())
        print('The minimum height is ', ride2.get_height())

def valid(x):
    #function for validation
    while x<0:
        x=float(input('Please enter a positive number:'))
    return x
     
        
main()       
        

    
    
        
