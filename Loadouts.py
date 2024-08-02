from typing import List
from Art import Art
from Loadout import Loadout
import time
import itertools


def create_combs(art_list: List[Art], container_slots=None):
    if container_slots is None:
        container_slots = int(input('Число ячеек контейнера: '))
    start_time = time.time()
    print('создаю комбинации..')
    combs = tuple(itertools.combinations_with_replacement(art_list, container_slots))
    print(f"..{len(combs)} комбинаций создано за %s секунд" % (time.time() - start_time))
    return combs


def create_loadouts_from_combs(combs, optimize_by_inffilter=False, defend=0):
    loadout_list = []
    start_time = time.time()
    print("создаю сборки..")
    if optimize_by_inffilter:
        for comb in combs:
            rad = 0
            psi = 0
            bio = 0
            temperature = 0
            cold = 0
            for art in comb:
                rad += art.get_rad(defend=defend)
            if rad <= 0.5:
                for art in comb:
                    psi += art.get_psi(defend=defend)
                if psi <= 1.5:
                    for art in comb:
                        bio += art.get_bio(defend=defend)
                    if bio <= 0.5:
                        for art in comb:
                            temperature += art.get_temperature(defend=defend)
                        if temperature <= 0.5:
                            for art in comb:
                                cold += art.get_cold(defend=defend)
                            if cold <= 1.0:
                                loadout_list.append(Loadout(comb))
        print(f"..{len(loadout_list)} сборок создано и отфильтровано за %s секунд" % (time.time() - start_time))
    else:
        for comb in combs:
            loadout_list.append(Loadout(comb))
        print(f"..{len(loadout_list)} сборок создано за %s секунд" % (time.time() - start_time))
    return loadout_list


class Loadouts:
    __slots__ = ['loadouts']

    def __init__(self, loadouts: List[Loadout]):
        self.loadouts = loadouts

    def get_loadouts(self):
        return self.loadouts

    def get_loadout(self, index: int):
        return self.loadouts[index]

    def get_loadouts_by_health(self):
        return sorted(self.loadouts, key=lambda x: x.get_health(), reverse=True)

    def get_loadouts_by_health_regen(self):
        return sorted(self.loadouts, key=lambda x: x.get_health_regen(), reverse=True)

    def get_loadouts_by_effective_regen(self):
        return sorted(self.loadouts, key=lambda x: x.get_effective_regen(), reverse=True)

    def get_loadouts_by_bullet_resistance(self):
        return sorted(self.loadouts, key=lambda x: x.get_bullet_resistance(), reverse=True)

    def get_loadouts_by_stamina(self):
        return sorted(self.loadouts, key=lambda x: x.get_stamina(), reverse=True)

    def get_loadouts_by_move_speed(self):
        return sorted(self.loadouts, key=lambda x: x.get_move_speed(), reverse=True)

    def get_loadouts_by_stamina_regen(self):
        return sorted(self.loadouts, key=lambda x: x.get_stamina_regen(), reverse=True)

    def get_loadouts_by_rupture_def(self):
        return sorted(self.loadouts, key=lambda x: x.get_rupture_def(), reverse=True)

    def get_loadouts_by_psi_def(self):
        return sorted(self.loadouts, key=lambda x: x.get_psi_def(), reverse=True)

    def get_loadouts_by_rad_def(self):
        return sorted(self.loadouts, key=lambda x: x.get_rad_def(), reverse=True)

    def get_loadouts_by_temperature_def(self):
        return sorted(self.loadouts, key=lambda x: x.get_temperature_def(), reverse=True)

    def get_loadouts_by_bio_def(self):
        return sorted(self.loadouts, key=lambda x: x.get_bio_def(), reverse=True)

    def get_loadouts_by_psi(self, defend=0):
        return sorted(self.loadouts, key=lambda x: x.get_psi(defend=defend), reverse=True)

    def get_loadout_by_effective_regen(self):
        return max(self.loadouts, key=lambda x: x.get_effective_regen())

    def get_loadout_by_bullet_resistance(self):
        return max(self.loadouts, key=lambda x: x.get_bullet_resistance())

    def get_loadout_by_stamina(self):
        return max(self.loadouts, key=lambda x: x.get_stamina())

    def get_loadout_by_move_speed(self):
        return max(self.loadouts, key=lambda x: x.get_move_speed())
