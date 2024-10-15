class DemoClass:

    def add(self, x: int, y: int):
        return x+y

    def subtract(self, x: int, y: int):
        return x-y

    def multiply(self, x: int, y: int):
        return x*y

    def divide(self, x: int, y:int):
        return x/y
    
    def consonents(self, x: str):
        return x not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    
    def vowel(self, x: str):
        return x in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    
    def greet(self):
        print("Good Morning and Welcome!")
