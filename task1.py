class Camera:
    def __init__(self, manufacturer = '', memorySize = 0, focus_number = 1.0):
        self.__manufacturer = manufacturer
        self.__memorySize = memorySize
        self.__focus_number = focus_number

        self.photos_number = 10
        self.photo_efect = "Night"

    def get_manufacturer(self):
        return self.__manufacturer
    
    def get_memorySize(self):
        return self.__memorySize
    
    def get_focus_number(self):
        return self.__focus_number
    

    def __str__(self):
        return (f" '{self.__manufacturer}':  "
                f"memorySize = {self.__memorySize} MB, "
                f"focus_number = {self.__focus_number}x, "
                f"photos_number: {self.photos_number}, "
                f"photo_efect - {self.photo_efect}. ")
        
    def __repr__(self):
        return self.__str__()
    

    def __del__(self):
        print("\n", f"Camera '{self.__manufacturer}' is deconstructed.")





class Farm:
    def __init__(self, location = "", animal_number = 0, fan_power = 0):
        self.__location = location
        self.__animal_number = animal_number
        self.__fan_power = fan_power

        self.owner = "Stiven"
        self.ownerAge = 45


    def get_location(self):
        return self.__location
    
    def get_animal_number(self):
        return self.__animal_number
    
    def get_fan_power(self):
        return self.__fan_power
    

    def __str__(self):
        return (f"Farm (location = {self.__location}, "
                f"animal_number = {self.__animal_number}, "
                f"fan_power = {self.__fan_power}W), " 
                f"Owner: {self.owner}," 
                f"owner age = {self.ownerAge}. ")
    
    def __repr__(self):
        return self.__str__()
    

    def __del__(self):
        print("\n", f"Farm in {self.__location} is deconstructed.")



def main():
    cameras = [
        Camera("Canon", 128, 4.0),
        Camera("Sony", 128, 3.5),
        Camera("Panasonic", 256, 5.0)
    ]
     
    info_camera = [str(camera) for camera in cameras]

    print("\n" .join(info_camera))
    print("\n\n")
    
    
    farms = [
        Farm("North", 10, 180),
        Farm("South", 25, 1200),
        Farm("East", 30, 1300 )
    ]

    info_farms = [str(farm) for farm in farms]

    print("\n" .join(info_farms))


main()

