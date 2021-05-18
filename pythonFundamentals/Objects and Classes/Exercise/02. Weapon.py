class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return f"shooting..."  # no need for else since the return exits the if
        return f"no bullets left"

    # printing the actual value of the object instead the value shown in the memory
    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()

print(weapon)
