import sys
from art_list import arts_list
from Loadouts import Loadouts, create_loadouts_from_combs, create_combs
import tkinter as tk
from tkinter import ttk


def get_size(obj, seen=None):
    # From https://goshippo.com/blog/measure-real-size-any-python-object/
    # Recursively finds size of objects
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def filter_changed(_):
    for row in loadout_treeview.get_children():
        loadout_treeview.delete(row)

    if filter_after_create.get() == 'Хп':
        loadouts.loadouts = loadouts.get_loadouts_by_health()

    if filter_after_create.get() == 'Регенерация здоровья':
        loadouts.loadouts = loadouts.get_loadouts_by_health_regen()

    if filter_after_create.get() == 'Эффективность лечения':
        loadouts.loadouts = loadouts.get_loadouts_by_effective_regen()

    if filter_after_create.get() == 'Пулестойкость':
        loadouts.loadouts = loadouts.get_loadouts_by_bullet_resistance()

    if filter_after_create.get() == 'Выносливость':
        loadouts.loadouts = loadouts.get_loadouts_by_stamina()

    if filter_after_create.get() == 'Скорость передвижения':
        loadouts.loadouts = loadouts.get_loadouts_by_move_speed()

    if filter_after_create.get() == 'Восстановление выносливости':
        loadouts.loadouts = loadouts.get_loadouts_by_stamina_regen()

    if filter_after_create.get() == 'Защита от пси-излучения':
        loadouts.loadouts = loadouts.get_loadouts_by_psi_def()

    if filter_after_create.get() == 'Защита от радиации':
        loadouts.loadouts = loadouts.get_loadouts_by_rad_def()

    if filter_after_create.get() == 'Защита от температуры':
        loadouts.loadouts = loadouts.get_loadouts_by_temperature_def()

    if filter_after_create.get() == 'Защита от биозаражения':
        loadouts.loadouts = loadouts.get_loadouts_by_bio_def()

    if filter_after_create.get() == 'Пси-излучение':
        loadouts.loadouts = loadouts.get_loadouts_by_psi(defend=float(entry_defend.get()))

    j = 1
    for i in range(0, int(len(loadouts.loadouts))):
        loadout_treeview.insert(parent='', index=i,
                                values=[f'Сборка #{j} ({loadouts.get_loadouts()[i].get_artnames()})'],
                                tags=[loadouts.get_loadouts()[i]])
        j = j + 1


def reset():
    created_options.pack_forget()
    filter_after_create.set("Сортировать созданные по...")
    filter_on_create.pack()
    defend_label.pack()
    entry_defend.pack()
    loadout_treeview.pack_forget()
    loadout_treeview_scrollbar.pack_forget()
    filter_after_create.pack_forget()
    button_create.pack(side='left')
    entry_loadout_art_num.pack(side='left', padx=2)
    label_loadout_art_num.pack(side='left')
    button_filter.pack(side='left', padx=2)
    entry_loadouts_num.pack(side='left', padx=6)
    loadouts_num_label.pack(side='left')
    global loadouts
    alert.pack_forget()
    for row in loadout_treeview.get_children():
        loadout_treeview.delete(row)
    loadouts = Loadouts([])


def create_arts():
    try:
        alert.pack_forget()
        filter_on_create.pack_forget()
        loadout_treeview_scrollbar.pack(side='right', fill='y')
        loadout_treeview.pack(fill='both', expand=True)
        entry_loadouts_num.pack_forget()
        entry_loadout_art_num.pack_forget()
        defend_label.pack_forget()
        button_create.pack_forget()
        button_filter.pack_forget()
        entry_defend.pack_forget()
        label_loadout_art_num.pack_forget()
        loadouts_num_label.pack_forget()
        filter_after_create.pack(side='left', padx=5)
        created_options['text'] = f'Создано по: {filter_on_create.get()}, внутренняя защита: {float(entry_defend.get())}%'
        created_options.pack(side='left')
        global filter_var
        global loadouts
        for row in loadout_treeview.get_children():
            loadout_treeview.delete(row)

        loadouts = Loadouts(
            create_loadouts_from_combs(create_combs(arts_list, int(entry_loadout_art_num.get())),
                                       bool(filter_var.get()), defend=float(entry_defend.get())))

        if filter_on_create.get() == 'Сортировать по...':
            loadouts.loadouts = loadouts.get_loadouts()

        if filter_on_create.get() == 'Хп':
            loadouts.loadouts = loadouts.get_loadouts_by_health()

        if filter_on_create.get() == 'Регенерация здоровья':
            loadouts.loadouts = loadouts.get_loadouts_by_health_regen()

        if filter_on_create.get() == 'Эффективность лечения':
            loadouts.loadouts = loadouts.get_loadouts_by_effective_regen()

        if filter_on_create.get() == 'Пулестойкость':
            loadouts.loadouts = loadouts.get_loadouts_by_bullet_resistance()

        if filter_on_create.get() == 'Выносливость':
            loadouts.loadouts = loadouts.get_loadouts_by_stamina()

        if filter_on_create.get() == 'Скорость передвижения':
            loadouts.loadouts = loadouts.get_loadouts_by_move_speed()

        if filter_on_create.get() == 'Восстановление выносливости':
            loadouts.loadouts = loadouts.get_loadouts_by_stamina_regen()

        if filter_on_create.get() == 'Защита от пси-излучения':
            loadouts.loadouts = loadouts.get_loadouts_by_psi_def()

        if filter_on_create.get() == 'Защита от радиации':
            loadouts.loadouts = loadouts.get_loadouts_by_rad_def()

        if filter_on_create.get() == 'Защита от температуры':
            loadouts.loadouts = loadouts.get_loadouts_by_temperature_def()

        if filter_on_create.get() == 'Защита от биозаражения':
            loadouts.loadouts = loadouts.get_loadouts_by_bio_def()

        if filter_on_create.get() == 'Пси-излучение':
            loadouts.loadouts = loadouts.get_loadouts_by_psi(defend=float(entry_defend.get()))

        del loadouts.loadouts[int(entry_loadouts_num.get()):len(loadouts.loadouts)]
        j = 1
        for i in range(0, int(len(loadouts.loadouts))):
            loadout_treeview.insert(parent='', index=i,
                                    values=[f'Сборка #{j} ({loadouts.get_loadouts()[i].get_artnames()})'],
                                    tags=[loadouts.get_loadouts()[i]])
            j = j + 1
        if len(loadouts.loadouts) < int(entry_loadouts_num.get()):
            info_alert.set("!: мужык мы не потянем ты хочешь слишком \nмного сборок.. \nвозможны технические шоколадки..")
            alert.pack()

    except ValueError:
        info_alert.set(f'!: не указаны какие-то значения')
        alert.pack()


def print_stats(stats_object):
    if stats_object.get_health() != 0:
        if stats_object.get_health() > 0.0:
            loadout_health.configure(foreground=stat_positive)
        else:
            loadout_health.configure(foreground=stat_negative)
        info_health.set(f'Живучесть: {round(stats_object.get_health(), round_var)}%')
        loadout_health.pack(fill='x')
    if stats_object.get_health_regen() != 0:
        if stats_object.get_health_regen() > 0.0:
            loadout_health_regen.configure(foreground=stat_positive)
        else:
            loadout_health_regen.configure(foreground=stat_negative)
        info_health_regen.set(
            f'Регенерация здоровья: {round(stats_object.get_health_regen(), round_var)}%')
        loadout_health_regen.pack(fill='x')
    if stats_object.get_effective_regen() != 0:
        if stats_object.get_effective_regen() > 0.0:
            loadout_effective_regen.configure(foreground=stat_positive)
        else:
            loadout_effective_regen.configure(foreground=stat_negative)
        info_effective_regen.set(
            f'Эффективность лечения: {round(stats_object.get_effective_regen(), round_var)}%')
        loadout_effective_regen.pack(fill='x')
    if stats_object.get_bullet_resistance() != 0:
        if stats_object.get_bullet_resistance() > 0.0:
            loadout_bullet_resistance.configure(foreground=stat_positive)
        else:
            loadout_bullet_resistance.configure(foreground=stat_negative)
        info_bullet_resistance.set(
            f'Пулестойкость: {round(stats_object.get_bullet_resistance(), round_var)}')
        loadout_bullet_resistance.pack(fill='x')
    if stats_object.get_stamina() != 0:
        if stats_object.get_stamina() > 0.0:
            loadout_stamina.configure(foreground=stat_positive)
        else:
            loadout_stamina.configure(foreground=stat_negative)
        info_stamina.set(f'Выносливость: {round(stats_object.get_stamina(), round_var)}%')
        loadout_stamina.pack(fill='x')
    if stats_object.get_move_speed() != 0:
        if stats_object.get_move_speed() > 0.0:
            loadout_move_speed.configure(foreground=stat_positive)
        else:
            loadout_move_speed.configure(foreground=stat_negative)
        info_move_speed.set(
            f'Скорость передвижения: {round(stats_object.get_move_speed(), round_var)}%')
        loadout_move_speed.pack(fill='x')
    if stats_object.get_stamina_regen() != 0:
        if stats_object.get_stamina_regen() > 0.0:
            loadout_stamina_regen.configure(foreground=stat_positive)
        else:
            loadout_stamina_regen.configure(foreground=stat_negative)
        info_stamina_regen.set(
            f'Восстановление выносливости: {round(stats_object.get_stamina_regen(), round_var)}%')
        loadout_stamina_regen.pack(fill='x')
    if stats_object.get_rupture_def() != 0:
        if stats_object.get_rupture_def() > 0.0:
            loadout_rupture_def.configure(foreground=stat_positive)
        else:
            loadout_rupture_def.configure(foreground=stat_negative)
        info_rupture_def.set(
            f'Защита от разрыва: {round(stats_object.get_rupture_def(), round_var)}')
        loadout_rupture_def.pack(fill='x')
    if stats_object.get_psi_def() != 0:
        if stats_object.get_psi_def() > 0.0:
            loadout_psi_def.configure(foreground=stat_positive)
        else:
            loadout_psi_def.configure(foreground=stat_negative)
        info_psi_def.set(f'Защита от пси-излучения: {round(stats_object.get_psi_def(), round_var)}')
        loadout_psi_def.pack(fill='x')
    if stats_object.get_rad_def() != 0:
        if stats_object.get_rad_def() > 0.0:
            loadout_rad_def.configure(foreground=stat_positive)
        else:
            loadout_rad_def.configure(foreground=stat_negative)
        info_rad_def.set(f'Защита от радиации: {round(stats_object.get_rad_def(), round_var)}')
        loadout_rad_def.pack(fill='x')
    if stats_object.get_temperature_def() != 0:
        if stats_object.get_temperature_def() > 0.0:
            loadout_temperature_def.configure(foreground=stat_positive)
        else:
            loadout_temperature_def.configure(foreground=stat_negative)
        info_temperature_def.set(
            f'Защита от температуры: {round(stats_object.get_temperature_def(), round_var)}')
        loadout_temperature_def.pack(fill='x')
    if stats_object.get_fire_def() != 0:
        if stats_object.get_fire_def() > 0.0:
            loadout_fire_def.configure(foreground=stat_positive)
        else:
            loadout_fire_def.configure(foreground=stat_negative)
        info_fire_def.set(f'Защита от огня: {round(stats_object.get_fire_def(), round_var)}')
        loadout_fire_def.pack(fill='x')
    if stats_object.get_bio_def() != 0:
        if stats_object.get_bio_def() > 0.0:
            loadout_bio_def.configure(foreground=stat_positive)
        else:
            loadout_bio_def.configure(foreground=stat_negative)
        info_bio_def.set(f'Защита от биозаражения: {round(stats_object.get_bio_def(), round_var)}')
        loadout_bio_def.pack(fill='x')
    if stats_object.get_chemical_def() != 0:
        if stats_object.get_chemical_def() > 0.0:
            loadout_chemical_def.configure(foreground=stat_positive)
        else:
            loadout_chemical_def.configure(foreground=stat_negative)
        info_chemical_def.set(f'Химзащита: {round(stats_object.get_chemical_def(), round_var)}')
        loadout_chemical_def.pack(fill='x')
    if stats_object.get_cold(defend=float(entry_defend.get())) != 0:
        if stats_object.get_cold(defend=float(entry_defend.get())) > 0.0:
            info_cold.set(f'Холод: {round(stats_object.get_cold(defend=float(entry_defend.get())), round_var)} (-{float(entry_defend.get())}%)')
            loadout_cold.configure(foreground=stat_negative)
            loadout_cold.pack(fill='x')
        else:
            info_cold.set(f'Холод: {round(stats_object.get_cold(defend=float(entry_defend.get())), round_var)}')
            loadout_cold.configure(foreground=stat_positive)
            loadout_cold.pack(fill='x')
    if stats_object.get_bio(defend=float(entry_defend.get())) != 0:
        if stats_object.get_bio(defend=float(entry_defend.get())) > 0.0:
            info_bio.set(f'Биологическое заражение: {round(stats_object.get_bio(defend=float(entry_defend.get())), round_var)} (-{float(entry_defend.get())}%)')
            loadout_bio.configure(foreground=stat_negative)
            loadout_bio.pack(fill='x')
        else:
            info_bio.set(f'Биологическое заражение: {round(stats_object.get_bio(defend=float(entry_defend.get())), round_var)}')
            loadout_bio.configure(foreground=stat_positive)
            loadout_bio.pack(fill='x')
    if stats_object.get_psi(defend=float(entry_defend.get())) != 0:
        if stats_object.get_psi(defend=float(entry_defend.get())) > 0.0:
            info_psi.set(f'Пси-излучение: {round(stats_object.get_psi(defend=float(entry_defend.get())), round_var)} (-{float(entry_defend.get())}%)')
            loadout_psi.configure(foreground=stat_negative)
            loadout_psi.pack(fill='x')
        else:
            info_psi.set(f'Пси-излучение: {round(stats_object.get_psi(defend=float(entry_defend.get())), round_var)}')
            loadout_psi.configure(foreground=stat_positive)
            loadout_psi.pack(fill='x')
    if stats_object.get_temperature(defend=float(entry_defend.get())) != 0:
        if stats_object.get_temperature(defend=float(entry_defend.get())) > 0.0:
            info_temperature.set(f'Температура: {round(stats_object.get_temperature(defend=float(entry_defend.get())), round_var)} (-{float(entry_defend.get())}%)')
            loadout_temperature.configure(foreground=stat_negative)
            loadout_temperature.pack(fill='x')
        else:
            info_temperature.set(f'Температура: {round(stats_object.get_temperature(defend=float(entry_defend.get())), round_var)}')
            loadout_temperature.configure(foreground=stat_positive)
            loadout_temperature.pack(fill='x')
    if stats_object.get_rad(defend=float(entry_defend.get())) != 0:
        if stats_object.get_rad(defend=float(entry_defend.get())) > 0.0:
            info_rad.set(f'Радиация: {round(stats_object.get_rad(defend=float(entry_defend.get())), round_var)} (-{float(entry_defend.get())}%)')
            loadout_rad.configure(foreground=stat_negative)
            loadout_rad.pack(fill='x')
        else:
            info_rad.set(f'Радиация: {round(stats_object.get_rad(defend=float(entry_defend.get())), round_var)}')
            loadout_rad.configure(foreground=stat_positive)
            loadout_rad.pack(fill='x')
    if stats_object.get_rad_resist() != 0:
        if stats_object.get_rad_resist() > 0.0:
            loadout_rad_resist.configure(foreground=stat_positive)
        else:
            loadout_rad_resist.configure(foreground=stat_negative)
        info_rad_resist.set(
            f'Сопротивление радиации: {round(stats_object.get_rad_resist(), round_var)}%')
        loadout_rad_resist.pack(fill='x')
    if stats_object.get_bio_resist() != 0:
        if stats_object.get_bio_resist() > 0.0:
            loadout_bio_resist.configure(foreground=stat_positive)
        else:
            loadout_bio_resist.configure(foreground=stat_negative)
        info_bio_resist.set(
            f'Сопротивление биозаражению: {round(stats_object.get_bio_resist(), round_var)}%')
        loadout_bio_resist.pack(fill='x')
    if stats_object.get_temperature_resist() != 0:
        if stats_object.get_temperature_resist() > 0.0:
            loadout_temperature_resist.configure(foreground=stat_positive)
        else:
            loadout_temperature_resist.configure(foreground=stat_negative)
        info_temperature_resist.set(
            f'Сопротивление температуре: {round(stats_object.get_temperature_resist(), round_var)}%')
        loadout_temperature_resist.pack(fill='x')
    if stats_object.get_psi_resist() != 0:
        if stats_object.get_psi_resist() > 0.0:
            loadout_psi_resist.configure(foreground=stat_positive)
        else:
            loadout_psi_resist.configure(foreground=stat_negative)
        info_psi_resist.set(
            f'Сопротивление пси-излучению: {round(stats_object.get_psi_resist(), round_var)}%')
        loadout_psi_resist.pack(fill='x')
    if stats_object.get_electro_reaction() != 0:
        if stats_object.get_electro_reaction() > 0.0:
            loadout_electro_reaction.configure(foreground=stat_positive)
        else:
            loadout_electro_reaction.configure(foreground=stat_negative)
        info_electro_reaction.set(
            f'Реакция на электричество: {round(stats_object.get_electro_reaction(), round_var)}%')
        loadout_electro_reaction.pack(fill='x')
    if stats_object.get_fire_reaction() != 0:
        if stats_object.get_fire_reaction() > 0.0:
            loadout_fire_reaction.configure(foreground=stat_positive)
        else:
            loadout_fire_reaction.configure(foreground=stat_negative)
        info_fire_reaction.set(
            f'Реакция на ожог: {round(stats_object.get_fire_reaction(), round_var)}%')
        loadout_fire_reaction.pack(fill='x')
    if stats_object.get_rupture_reaction() != 0:
        if stats_object.get_rupture_reaction() > 0.0:
            loadout_rupture_reaction.configure(foreground=stat_positive)
        else:
            loadout_rupture_reaction.configure(foreground=stat_negative)
        info_rupture_reaction.set(
            f'Реакция на разрыв: {round(stats_object.get_rupture_reaction(), round_var)}%')
        loadout_rupture_reaction.pack(fill='x')
    if stats_object.get_weight() != 0:
        info_weight.set(f'Переносимый вес: {round(stats_object.get_weight(), round_var)}')
        loadout_weight.pack(fill='x')
    if stats_object.get_bleeding() != 0:
        if stats_object.get_bleeding() > 0.0:
            loadout_bleeding.configure(foreground=stat_negative)
        else:
            loadout_bleeding.configure(foreground=stat_positive)
        info_bleeding.set(f'Кровотечение: {round(stats_object.get_bleeding(), round_var)}')
        loadout_bleeding.pack(fill='x')


def forget_stats():
    loadout_name.pack_forget()
    loadout_health.pack_forget()
    loadout_health_regen.pack_forget()
    loadout_effective_regen.pack_forget()
    loadout_bullet_resistance.pack_forget()
    loadout_stamina.pack_forget()
    loadout_move_speed.pack_forget()
    loadout_stamina_regen.pack_forget()
    loadout_rupture_def.pack_forget()
    loadout_psi_def.pack_forget()
    loadout_rad_def.pack_forget()
    loadout_temperature_def.pack_forget()
    loadout_fire_def.pack_forget()
    loadout_bio_def.pack_forget()
    loadout_chemical_def.pack_forget()
    loadout_cold.pack_forget()
    loadout_bio.pack_forget()
    loadout_psi.pack_forget()
    loadout_temperature.pack_forget()
    loadout_rad.pack_forget()
    loadout_rad_resist.pack_forget()
    loadout_bio_resist.pack_forget()
    loadout_temperature_resist.pack_forget()
    loadout_psi_resist.pack_forget()
    loadout_electro_reaction.pack_forget()
    loadout_fire_reaction.pack_forget()
    loadout_rupture_reaction.pack_forget()
    loadout_weight.pack_forget()
    loadout_bleeding.pack_forget()


def use_global_stats():
    global info_artnames
    global info_health
    global info_health_regen
    global info_effective_regen
    global info_bullet_resistance
    global info_stamina
    global info_move_speed
    global info_stamina_regen
    global info_rupture_def
    global info_psi_def
    global info_rad_def
    global info_temperature_def
    global info_fire_def
    global info_bio_def
    global info_chemical_def
    global info_cold
    global info_bio
    global info_psi
    global info_temperature
    global info_rad
    global info_rad_resist
    global info_bio_resist
    global info_temperature_resist
    global info_psi_resist
    global info_electro_reaction
    global info_fire_reaction
    global info_rupture_reaction
    global info_weight
    global info_bleeding


def item_select_art(_):
    forget_stats()
    use_global_stats()
    if len(arts_treeview.selection()) != 0:
        for selected_art in arts_treeview.selection():
            for i in loadout_treeview.selection():
                for j in range(0, int(entry_loadouts_num.get())):
                    if str(loadouts.get_loadouts()[j]) == loadout_treeview.item(i)['tags'][0]:
                        loadout = loadouts.get_loadouts()[j]
                        for k in range(0, int(entry_loadout_art_num.get())):
                            if arts_treeview.item(selected_art)['tags'][1] == str(loadout.arts[k]):
                                art = loadout.arts[k]
                                info_artnames.set(art.get_name())
                                loadout_name.pack(fill='x')
                                print_stats(art)
    else:
        item_select(_=2)


def item_select(_):
    for row in arts_treeview.get_children():
        arts_treeview.delete(row)
    forget_stats()
    use_global_stats()
    for i in loadout_treeview.selection():
        for j in range(0, int(entry_loadouts_num.get())):
            if str(loadouts.get_loadouts()[j]) == loadout_treeview.item(i)['tags'][0]:
                loadout = loadouts.get_loadouts()[j]
                for k in range(0, int(entry_loadout_art_num.get())):
                    arts_treeview.insert(parent='', index=0, values=[f'{loadout.arts[k].get_name()}'],
                                         tags=[loadout, loadout.arts[k]])
                print_stats(loadout)


# config
window = tk.Tk()
window.title('stalcalc v2')
window.geometry('650x360+600+300')
window.resizable(False, False)

# vars
filter_vars = (
    "Хп", "Регенерация здоровья",
    "Эффективность лечения", "Пулестойкость", "Выносливость", "Скорость передвижения",
    "Восстановление выносливости", "Защита от пси-излучения", "Защита от радиации",
    "Защита от температуры", "Защита от биозаражения", "Пси-излучение")
filter_on_create_var = tk.StringVar()
stat_negative = '#700000'
stat_positive = '#028500'
defend_var = 0
loadouts = Loadouts([])
round_var = 2
font_var_default = ("Arial", 9)
info_alert = tk.StringVar()
info_alert.set('!: для 6 ячеек надо ~32гб оперативки \n(у меня комп не тянет я не проверял)')
info_artnames = tk.StringVar()
info_health = tk.StringVar()
info_health_regen = tk.StringVar()
info_effective_regen = tk.StringVar()
info_bullet_resistance = tk.StringVar()
info_stamina = tk.StringVar()
info_move_speed = tk.StringVar()
info_stamina_regen = tk.StringVar()
info_rupture_def = tk.StringVar()
info_psi_def = tk.StringVar()
info_rad_def = tk.StringVar()
info_temperature_def = tk.StringVar()
info_fire_def = tk.StringVar()
info_bio_def = tk.StringVar()
info_chemical_def = tk.StringVar()
info_cold = tk.StringVar()
info_bio = tk.StringVar()
info_psi = tk.StringVar()
info_temperature = tk.StringVar()
info_rad = tk.StringVar()
info_rad_resist = tk.StringVar()
info_bio_resist = tk.StringVar()
info_temperature_resist = tk.StringVar()
info_psi_resist = tk.StringVar()
info_electro_reaction = tk.StringVar()
info_fire_reaction = tk.StringVar()
info_rupture_reaction = tk.StringVar()
info_weight = tk.StringVar()
info_bleeding = tk.StringVar()

# frames
righttopframe = ttk.Frame(window)
rightbottomframe = ttk.Frame(window)
lefttopframe = ttk.Frame(window)
leftbottomframe = ttk.Frame(window)
rightbottom_labels = ttk.Frame(rightbottomframe)

# widgets
defend_label = ttk.Label(leftbottomframe, text='Внутренняя защита')
entry_defend = ttk.Combobox(leftbottomframe, width=4, values=('0', '50', '55', '60', '85', '93.5'))
filter_after_create = ttk.Combobox(lefttopframe, state='readonly', values=filter_vars, width=30)
filter_after_create.set("Сортировать созданные по...")
filter_on_create = ttk.Combobox(leftbottomframe, state='readonly', values=filter_vars, width=30)
filter_on_create.set("Сортировать по...")
created_options = ttk.Label(righttopframe, text=f'Создано по: {filter_on_create.get()}')
sborki_label = ttk.Label(lefttopframe, text='Сборки')
loadout_treeview = ttk.Treeview(leftbottomframe, columns=['loadouts'], show='headings')
loadout_treeview.heading('loadouts', text='Сборки')
loadout_treeview.column('loadouts', width=222)
loadout_treeview_scrollbar = ttk.Scrollbar(leftbottomframe, orient='vertical', command=loadout_treeview.yview)
loadout_treeview.configure(yscrollcommand=loadout_treeview_scrollbar.set)
arts_treeview = ttk.Treeview(rightbottomframe, columns=['arts'], show='headings')
arts_treeview.heading('arts', text='Арты сборки')
arts_treeview.column('arts', width=96)
button_create = ttk.Button(righttopframe, text='Создать сборки', command=create_arts)
filter_var = tk.IntVar()
button_filter = ttk.Checkbutton(righttopframe, text='Фильтр заражений', variable=filter_var)
button_reset = ttk.Button(righttopframe, text='Сбросить', command=reset)
entry_loadouts_num = ttk.Combobox(lefttopframe, width=4, values=('10', '30', '50', '100', '300'))
loadouts_num_label = ttk.Label(lefttopframe, text='Кол-во сборок')
entry_loadout_art_num = ttk.Combobox(righttopframe, width=1, values=('2', '3', '4', '5', '6'))
label_loadout_art_num = ttk.Label(righttopframe, text='Ячеек')
alert = ttk.Label(rightbottom_labels, textvariable=info_alert, background='yellow', font=("Arial", 11))
empty_label = ttk.Label(rightbottom_labels, text='Пусто', font=font_var_default)
loadout_name = ttk.Label(rightbottom_labels, text='Имена артов', font=font_var_default,
                         textvariable=info_artnames)
loadout_health = ttk.Label(rightbottom_labels, text='Живучесть', font=font_var_default,
                           textvariable=info_health)
loadout_health_regen = ttk.Label(rightbottom_labels, text='Регенерация здоровья', font=font_var_default,
                                 textvariable=info_health_regen)
loadout_effective_regen = ttk.Label(rightbottom_labels, text='Эффективность лечения', font=font_var_default,
                                    textvariable=info_effective_regen)
loadout_bullet_resistance = ttk.Label(rightbottom_labels, text='Пулестойкость', font=font_var_default,
                                      textvariable=info_bullet_resistance)
loadout_stamina = ttk.Label(rightbottom_labels, text='Выносливость', font=font_var_default,
                            textvariable=info_stamina)
loadout_move_speed = ttk.Label(rightbottom_labels, text='Скорость передвижения', font=font_var_default,
                               textvariable=info_move_speed)
loadout_stamina_regen = ttk.Label(rightbottom_labels, text='Восстановление выносливости',
                                  font=font_var_default, textvariable=info_stamina_regen)
loadout_rupture_def = ttk.Label(rightbottom_labels, text='Защита от разрыва', font=font_var_default,
                                textvariable=info_rupture_def)
loadout_psi_def = ttk.Label(rightbottom_labels, text='Защита от пси-излучения', font=font_var_default,
                            textvariable=info_psi_def)
loadout_rad_def = ttk.Label(rightbottom_labels, text='Защита от радиации', font=font_var_default,
                            textvariable=info_rad_def)
loadout_temperature_def = ttk.Label(rightbottom_labels, text='Защита от температуры', font=font_var_default,
                                    textvariable=info_temperature_def)
loadout_fire_def = ttk.Label(rightbottom_labels, text='Защита от огня', font=font_var_default,
                             textvariable=info_fire_def)
loadout_bio_def = ttk.Label(rightbottom_labels, text='Защита от биозаражения', font=font_var_default,
                            textvariable=info_bio_def)
loadout_chemical_def = ttk.Label(rightbottom_labels, text='Химзащита', font=font_var_default,
                                 textvariable=info_chemical_def)
loadout_cold = ttk.Label(rightbottom_labels, text='Холод', font=font_var_default, textvariable=info_cold)
loadout_bio = ttk.Label(rightbottom_labels, text='Биологическое заражение', font=font_var_default,
                        textvariable=info_bio)
loadout_psi = ttk.Label(rightbottom_labels, text='Пси-излучение', font=font_var_default,
                        textvariable=info_psi)
loadout_temperature = ttk.Label(rightbottom_labels, text='Температура', font=font_var_default,
                                textvariable=info_temperature)
loadout_rad = ttk.Label(rightbottom_labels, text='Радиация', font=font_var_default, textvariable=info_rad)
loadout_rad_resist = ttk.Label(rightbottom_labels, text='Сопротивление радиации', font=font_var_default,
                               textvariable=info_rad_resist)
loadout_bio_resist = ttk.Label(rightbottom_labels, text='Сопротивление биозаражению', font=font_var_default,
                               textvariable=info_bio_resist)
loadout_temperature_resist = ttk.Label(rightbottom_labels, text='Сопротивление температуре',
                                       font=font_var_default, textvariable=info_temperature_resist)
loadout_psi_resist = ttk.Label(rightbottom_labels, text='Сопротивление пси-излучению',
                               font=font_var_default, textvariable=info_psi_resist)
loadout_electro_reaction = ttk.Label(rightbottom_labels, text='Реакция на электричество',
                                     font=font_var_default, textvariable=info_electro_reaction)
loadout_fire_reaction = ttk.Label(rightbottom_labels, text='Реакция на ожог', font=font_var_default,
                                  textvariable=info_fire_reaction)
loadout_rupture_reaction = ttk.Label(rightbottom_labels, text='Реакция на разрыв', font=font_var_default,
                                     textvariable=info_rupture_reaction)
loadout_weight = ttk.Label(rightbottom_labels, text='Переносимый вес', font=font_var_default,
                           textvariable=info_weight)
loadout_bleeding = ttk.Label(rightbottom_labels, text='Кровотечение', font=font_var_default,
                             textvariable=info_bleeding)

# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=4)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)

# place a widget
rightbottomframe.grid(row=1, column=1, sticky='nsew')
arts_treeview.pack(side='left', fill='y')
rightbottom_labels.pack(side='left', fill='y')
alert.pack()

righttopframe.grid(row=0, column=1, sticky='nsew')
button_create.pack(side='left')
entry_loadout_art_num.pack(side='left', padx=2)
label_loadout_art_num.pack(side='left')
button_filter.pack(side='left', padx=2)
button_reset.pack(side='right', padx=5)

leftbottomframe.grid(row=1, column=0, sticky='nsew')
filter_on_create.pack()
defend_label.pack(pady=2)
entry_defend.pack()

lefttopframe.grid(row=0, column=0, sticky='nsew')
entry_loadouts_num.pack(side='left', padx=6)
loadouts_num_label.pack(side='left')

arts_treeview.bind('<<TreeviewSelect>>', item_select_art)
loadout_treeview.bind('<<TreeviewSelect>>', item_select)
filter_after_create.bind('<<ComboboxSelected>>', filter_changed)
window.mainloop()
