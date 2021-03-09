class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def display(self):
        print("My current speed is {}".format(self.speed))


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car")
    my_car.accelerate()
    my_car.accelerate()
    my_car.display()
    my_car.brake()
    my_car.display()
