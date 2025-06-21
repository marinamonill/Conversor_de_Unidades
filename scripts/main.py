from proyecto_conversion.longitud import metros_a_kilometros, pulgadas_a_centimetros
from proyecto_conversion.temperatura import celsius_a_fahrenheit
from proyecto_conversion.masa import gramos_a_kilogramos

def main():
    print("1500 metros son", metros_a_kilometros(1500), "km")
    print("10 pulgadas son", pulgadas_a_centimetros(10), "cm")
    print("0 grados Celsius son", celsius_a_fahrenheit(0), "°F")
    print("1000 gramos son", gramos_a_kilogramos(1000), "kg")

if __name__ == "__main__":
    main()
