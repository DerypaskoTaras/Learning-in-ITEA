class Car:
    wheel = 4
    engine = 'Diesel engine'
    max_speed = 120
    Car_mileage = 0

    def start_engine(self):
        print("Your car's engine is starting")

    def stop_engine(self):
        print("Your car's engine is stopped")

    def car_power(self):
        print('The power of your car is 100 horsepower')

    def car_weight(self):
        print('Your car weighs no more than 1000 kg.')


class PassengerCar(Car):
    Maximum_passengers = 8

    def car_power(self):
        print('The power of your car is 150 horsepower')

    def Passengers_boarding(self):
        print('Passengers have finished boarding in your car')


class CargoCar(Car):
    Loading_capacity = 3500

    def car_loading(self):
        print('Your car is loaded')

    def car_weight(self):
        print('Your car weighs over 3500 kg.')

    def car_power(self):
        print('The power of your car is 800 horsepower')
