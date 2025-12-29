class CoffeeMachine:
    def __init__(self, water_level, beans_level):
        self.water_level = water_level
        self.beans_level = beans_level

    def make_coffee(self):
        if self._water_level > 20 and self._beans_level > 5:
            self._water_level -= 20
            self._beans_level -= 5
            print("=====YOUR COFFEE READY=====")
            return True
        else:
            print("=====WE ARE OUT OF SUPPLIES=====")
            return False

    @property
    def water_level(self):
        return self._water_level

    @water_level.setter
    def water_level(self, water):
        if water < 0:
            print("=====WATER LEVEL ERROR=====")
        elif water > 1000:
            print("=====TOO MUCH WATER LEVEL=====")
            self._water_level = 1000
        else:
            self._water_level = water

    @property
    def beans_level(self):
        return self._beans_level

    @beans_level.setter
    def beans_level(self, beans):
        if beans < 0:
            print("=====WATER LEVEL ERROR=====")
        elif beans > 250:
            print("=====TOO MUCH BEANS LEVEL=====")
            self._beans_level = 250
        else:
            self._beans_level = beans

    def view_level(self):
        print(f"Water level: {self._water_level}, Beans level: {self._beans_level}")



def main():
    try:
        water = int(input("Enter water level: "))
    except:
        water = 0
    try:
        beans = int(input("Enter beans level: "))
    except:
        beans = 0

    coffee = CoffeeMachine(water, beans)

    while True:

        print("=====MAIN MENU=====")

        print("1. ADD WATER LEVEL")
        print("2. ADD BEANS LEVEL")
        print("3. ADD COFFEE")
        print("4. LEVELS")
        print("5. EXIT")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("=====ENTER VALID NUMBER=====")
            continue

        if choice == 1:
            waterlevel = int(input("SET water level: "))
            coffee.water_level += waterlevel

        elif choice == 2:
            beanslevel = int(input("SET beans level: "))
            coffee.beans_level += beanslevel
        elif choice == 3:
            coffee.make_coffee()
        elif choice == 4:
            coffee.view_level()
        elif choice == 5:
            exit()
        else:
            print("Enter a valid choice")




if __name__ == "__main__":
    main()