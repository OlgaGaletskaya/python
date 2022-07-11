class Newspapers:
    def __init__(self):
        self.name = 'Daily Planet'
   
    def get_news(name, place):
        print("NEWSPAPERS:", end=" ")
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')
        
    def planets(self, planet):
        planet_coordinates = getattr(planet, 'coordinates', 'place')
        print(f'{self.name} notifies {planet_coordinates}')