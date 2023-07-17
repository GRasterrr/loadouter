from typing import Tuple
from Art import Art


class Loadout:
    __slots__ = ['arts']

    def __init__(self, arts: Tuple[Art]):
        self.arts = arts

    def get_rad_resist(self):
        rad_resist = 0
        for i in self.arts:
            rad_resist += i.get_rad_resist()
        return rad_resist

    def get_bio_resist(self):
        bio_resist = 0
        for i in self.arts:
            bio_resist += i.get_bio_resist()
        return bio_resist

    def get_temperature_resist(self):
        temperature_resist = 0
        for i in self.arts:
            temperature_resist += i.get_temperature_resist()
        return temperature_resist

    def get_psi_resist(self):
        psi_resist = 0
        for i in self.arts:
            psi_resist += i.get_psi_resist()
        return psi_resist

    def get_cold(self, defend=0):
        cold = 0
        for i in self.arts:
            cold += i.get_cold(defend=defend)
        return cold

    def get_stamina_regen(self):
        stamina_regen = 0
        for i in self.arts:
            stamina_regen += i.get_stamina_regen()
        return stamina_regen

    def get_bullet_resistance(self):
        bullet_resistance = 0
        for i in self.arts:
            bullet_resistance += i.get_bullet_resistance()
        return bullet_resistance

    def get_health(self):
        health = 0
        for i in self.arts:
            health += i.get_health()
        return health

    def get_effective_regen(self):
        effective_regen = 0
        for i in self.arts:
            effective_regen += i.get_effective_regen()
        return effective_regen

    def get_health_regen(self):
        health_regen = 0
        for i in self.arts:
            health_regen += i.get_health_regen()
        return health_regen

    def get_move_speed(self):
        move_speed = 0
        for i in self.arts:
            move_speed += i.get_move_speed()
        return move_speed

    def get_stamina(self):
        stamina = 0
        for i in self.arts:
            stamina += i.get_stamina()
        return stamina

    def get_weight(self):
        weight = 0
        for i in self.arts:
            weight += i.get_weight()
        return weight

    def get_rupture_def(self):
        rupture_def = 0
        for i in self.arts:
            rupture_def += i.get_rupture_def()
        return rupture_def

    def get_explosion_def(self):
        explosion_def = 0
        for i in self.arts:
            explosion_def += i.get_explosion_def()
        return explosion_def

    def get_fire_def(self):
        fire_def = 0
        for i in self.arts:
            fire_def += i.get_fire_def()
        return fire_def

    def get_chemical_def(self):
        chemical_def = 0
        for i in self.arts:
            chemical_def += i.get_chemical_def()
        return chemical_def

    def get_rad_def(self):
        rad_def = 0
        for i in self.arts:
            rad_def += i.get_rad_def()
        return rad_def

    def get_temperature_def(self):
        temperature_def = 0
        for i in self.arts:
            temperature_def += i.get_temperature_def()
        return temperature_def

    def get_bio_def(self):
        bio_def = 0
        for i in self.arts:
            bio_def += i.get_bio_def()
        return bio_def

    def get_psi_def(self):
        psi_def = 0
        for i in self.arts:
            psi_def += i.get_psi_def()
        return psi_def

    def get_electro_reaction(self):
        electro_reaction = 0
        for i in self.arts:
            electro_reaction += i.get_electro_reaction()
        return electro_reaction

    def get_fire_reaction(self):
        fire_reaction = 0
        for i in self.arts:
            fire_reaction += i.get_fire_reaction()
        return fire_reaction

    def get_chemical_reaction(self):
        chemical_reaction = 0
        for i in self.arts:
            chemical_reaction += i.get_chemical_reaction()
        return chemical_reaction

    def get_rupture_reaction(self):
        rupture_reaction = 0
        for i in self.arts:
            rupture_reaction += i.get_rupture_reaction()
        return rupture_reaction

    def get_bio(self, defend=0):
        bio = 0
        for i in self.arts:
            bio += i.get_bio(defend=defend)
        return bio

    def get_psi(self, defend=0):
        psi = 0
        for i in self.arts:
            psi += i.get_psi(defend=defend)
        return psi

    def get_temperature(self, defend=0):
        temperature = 0
        for i in self.arts:
            temperature += i.get_temperature(defend=defend)
        return temperature

    def get_rad(self, defend=0):
        rad = 0
        for i in self.arts:
            rad += i.get_rad(defend=defend)
        return rad

    def get_bleeding(self):
        bleeding = 0
        for i in self.arts:
            bleeding += i.get_bleeding()
        return bleeding

    def get_artnames(self):
        names = ''
        for i in self.arts:
            names += i.name + ' '
        return names

    def print_info(self):
        print("")
        print("Арты сборки:", self.get_artnames())
        print("   Живучесть:", self.get_health())
        print("   Регенерация здоровья:", self.get_health_regen())
        print("   Эффективность лечения:", self.get_effective_regen())
        print("   Пулестойкость:", self.get_bullet_resistance())
        print("   Выносливость:", self.get_stamina())
        print("   Скорость передвижения:", self.get_move_speed())
        print("   Восстановление выносливости:", self.get_stamina_regen())
        print("   Защита от разрыва:", self.get_rupture_def())
        print("   Защита от пси-излучения:", self.get_psi_def())
        print("   Защита от радиации:", self.get_rad_def())
        print("   Защита от температуры:", self.get_temperature_def())
        print("   Защита от огня:", self.get_fire_def())
        print("   Защита от биозаражения:", self.get_bio_def())
        print("   Химзащита:", self.get_chemical_def())
        print("   Холод:", self.get_cold())
        print("   Биологическое заражение:", self.get_bio())
        print("   Пси-излучение:", self.get_psi())
        print("   Температура:", self.get_temperature())
        print("   Радиация:", self.get_rad())
        print("   Сопротивление радиации:", self.get_rad_resist())
        print("   Сопротивление биозаражению:", self.get_bio_resist())
        print("   Сопротивление температуре:", self.get_temperature_resist())
        print("   Сопротивление пси-излучению:", self.get_psi_resist())
        print("   Реакция на электричество:", self.get_electro_reaction())
        print("   Реакция на ожог:", self.get_fire_reaction())
        print("   Реакция на разрыв:", self.get_rupture_reaction())
        print("   Переносимый вес:", self.get_weight())
        print("   Кровотечение:", self.get_bleeding())
