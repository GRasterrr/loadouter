class Art:
    __slots__ = ['name',
                 'rad_resist',
                 'bio_resist',
                 'temperature_resist',
                 'psi_resist',
                 'cold',
                 'stamina_regen',
                 'bullet_resistance',
                 'health',
                 'effective_regen',
                 'health_regen',
                 'move_speed',
                 'stamina',
                 'weight',
                 'rupture_def',
                 'explosion_def',
                 'fire_def',
                 'chemical_def',
                 'rad_def',
                 'temperature_def',
                 'bio_def',
                 'psi_def',
                 'electro_reaction',
                 'fire_reaction',
                 'chemical_reaction',
                 'rupture_reaction',
                 'bio',
                 'psi',
                 'temperature',
                 'rad',
                 'bleeding'
                 ]

    def __init__(self, name, rad_resist=None, bio_resist=None, temperature_resist=None, psi_resist=None, cold=None,
                 stamina_regen=None,
                 bullet_resistance=None, health=None, effective_regen=None, health_regen=None, move_speed=None,
                 stamina=None, weight=None, rupture_def=None, explosion_def=None, fire_def=None, chemical_def=None,
                 rad_def=None, temperature_def=None,
                 bio_def=None, psi_def=None, electro_reaction=None, fire_reaction=None, chemical_reaction=None,
                 rupture_reaction=None, bio=None, psi=None, temperature=None, rad=None, bleeding=None):
        self.name = name
        self.rad_resist = rad_resist
        self.bio_resist = bio_resist
        self.temperature_resist = temperature_resist
        self.psi_resist = psi_resist
        self.cold = cold
        self.stamina_regen = stamina_regen
        self.bullet_resistance = bullet_resistance
        self.health = health
        self.effective_regen = effective_regen
        self.health_regen = health_regen
        self.move_speed = move_speed
        self.stamina = stamina
        self.weight = weight
        self.rupture_def = rupture_def
        self.explosion_def = explosion_def
        self.fire_def = fire_def
        self.chemical_def = chemical_def
        self.rad_def = rad_def
        self.temperature_def = temperature_def
        self.bio_def = bio_def
        self.psi_def = psi_def
        self.electro_reaction = electro_reaction
        self.fire_reaction = fire_reaction
        self.chemical_reaction = chemical_reaction
        self.rupture_reaction = rupture_reaction
        self.bio = bio
        self.psi = psi
        self.temperature = temperature
        self.rad = rad
        self.bleeding = bleeding

    def get_name(self):
        return self.name

    def get_rad_resist(self):
        if self.rad_resist is None:
            return 0
        else:
            return self.rad_resist

    def get_bio_resist(self):
        if self.bio_resist is None:
            return 0
        else:
            return self.bio_resist

    def get_temperature_resist(self):
        if self.temperature_resist is None:
            return 0
        else:
            return self.temperature_resist

    def get_psi_resist(self):
        if self.psi_resist is None:
            return 0
        else:
            return self.psi_resist

    def get_cold(self, defend=0):
        if self.cold is None:
            return 0
        else:
            if self.cold > 0:
                return self.cold * (1 - defend / 100)
            else:
                return self.cold

    def get_stamina_regen(self):
        if self.stamina_regen is None:
            return 0
        else:
            return self.stamina_regen

    def get_bullet_resistance(self):
        if self.bullet_resistance is None:
            return 0
        else:
            return self.bullet_resistance

    def get_health(self):
        if self.health is None:
            return 0
        else:
            return self.health

    def get_effective_regen(self):
        if self.effective_regen is None:
            return 0
        else:
            return self.effective_regen

    def get_health_regen(self):
        if self.health_regen is None:
            return 0
        else:
            return self.health_regen

    def get_move_speed(self):
        if self.move_speed is None:
            return 0
        else:
            return self.move_speed

    def get_stamina(self):
        if self.stamina is None:
            return 0
        else:
            return self.stamina

    def get_weight(self):
        if self.weight is None:
            return 0
        else:
            return self.weight

    def get_rupture_def(self):
        if self.rupture_def is None:
            return 0
        else:
            return self.rupture_def

    def get_explosion_def(self):
        if self.explosion_def is None:
            return 0
        else:
            return self.explosion_def

    def get_fire_def(self):
        if self.fire_def is None:
            return 0
        else:
            return self.fire_def

    def get_chemical_def(self):
        if self.chemical_def is None:
            return 0
        else:
            return self.chemical_def

    def get_rad_def(self):
        if self.rad_def is None:
            return 0
        else:
            return self.rad_def

    def get_temperature_def(self):
        if self.temperature_def is None:
            return 0
        else:
            return self.temperature_def

    def get_bio_def(self):
        if self.bio_def is None:
            return 0
        else:
            return self.bio_def

    def get_psi_def(self):
        if self.psi_def is None:
            return 0
        else:
            return self.psi_def

    def get_electro_reaction(self):
        if self.electro_reaction is None:
            return 0
        else:
            return self.electro_reaction

    def get_fire_reaction(self):
        if self.fire_reaction is None:
            return 0
        else:
            return self.fire_reaction

    def get_chemical_reaction(self):
        if self.chemical_reaction is None:
            return 0
        else:
            return self.chemical_reaction

    def get_rupture_reaction(self):
        if self.rupture_reaction is None:
            return 0
        else:
            return self.rupture_reaction

    def get_bio(self, defend=0):
        if self.bio is None:
            return 0
        else:
            if self.bio > 0:
                return self.bio * (1 - defend/100)
            else:
                return self.bio

    def get_psi(self, defend=0):
        if self.psi is None:
            return 0
        else:
            if self.psi > 0:
                return self.psi * (1 - defend / 100)
            else:
                return self.psi

    def get_temperature(self, defend=0):
        if self.temperature is None:
            return 0
        else:
            if self.temperature > 0:
                return self.temperature * (1 - defend / 100)
            else:
                return self.temperature

    def get_rad(self, defend=0):
        if self.rad is None:
            return 0
        else:
            if self.rad > 0:
                return self.rad * (1 - defend / 100)
            else:
                return self.rad

    def get_bleeding(self):
        if self.bleeding is None:
            return 0
        else:
            return self.bleeding
