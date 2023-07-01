# ОБЪЕКТНО ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ



class Car():
     def __init__(self,make,model,year):
         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriprive_name(self):
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You cant roll back an odometer')
#     def read_odometer(self):
#         print(f'This car has {self.odometer_reading} miles on it.')
#
#     def increment_odometer(self,miles):
#         self.odometer_reading += miles
#
# class Battery():
#     def __init__(self,battery_size = 70):
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         print(f'This car has a {self.battery_size} -kWh battery')
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = f'This car can go approximately {range}'
#         message += ' miles on a full charge'
#         print(message)
#
#     def upgrafe_bat(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#     def desc_upgr(self):
#         print(f'Обновленная батарея {self.battery_size}')
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = Battery()
#
#
#
# my_tesla = ElectricCar('tesla','model s ',2016)
# print(my_tesla.get_descriprive_name())
# my_tesla.battery.battery_size = 65
# my_tesla.battery.describe_battery()
# my_new_car = Car('BMW','m5',2019)
# print(my_new_car.get_descriprive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(23000)
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()


# class Restaurant():
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type
#         self.number_served = 0
#
#     def describe(self):
#         print(f'The name of restaurant is {self.name} and type is {self.type}')
#
#     def served(self):
#         print(f'The {self.number_served} people was served')
#
#     def get_open(self):
#         print('The restaurant is open')
#
#     def set_number_served(self,num_ser):
#         self.number_served = num_ser
#
#     def increment_n_v(self,increment):
#         self.number_served += increment
#
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self,flavors):
#         self.flavors = flavors
#
#     def describe_ice(self):
#         print(f'We have a {self.flavors} ice-cream')
#
# ice_cr = IceCreamStand('milk')
# ice_cr.describe_ice()
# rest = Restaurant('Mario','Italian food')
# rest.describe()
# rest.get_open()
# rest.set_number_served(55)
# rest.increment_n_v(5)
# rest.served()



#
# class User():
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#         self.login_attempts = 0
#
#     def describe(self):
#         print(f'Information about: {self.first} {self.last}')
#
#     def log_at_descr(self):
#         print(f'You have {self.login_attempts} attempts.')
#
#     def greet(self):
#         print(f'You are welcome {self.first}')
#
#     def increment_login_at(self):
#         self.login_attempts += 1
#
#     def reset_log_att(self):
#         self.login_attempts = 0
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ['разрешено добавлять сообщение','разрешено банить пользователя']
#     def show_privileges(self):
#         print(f'privileges of admin {self.privileges}')
# class Admin(User):
#     def __init__(self,first,last):
#         super().__init__(first,last)
#         self.privileges = Privileges()
#
#
# admin = Admin('Denis','Lukyanov')
# admin.describe()
# admin.privileges.show_privileges()
# users = User('Denis','Lukyanov')
# users.describe()
# users.greet()
# users.increment_login_at()
# users.increment_login_at()
# users.increment_login_at()
# users.log_at_descr()
# users.reset_log_att()
# users.log_at_descr()

# from collections import OrderedDict
#
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'c++'
# favorite_languages['phill'] = 'ruby'
# for name,languages in favorite_languages.items():
#     print(f'{name.title()} s favorite_languages is {languages.title()}. ')



