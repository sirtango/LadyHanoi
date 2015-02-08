
def select_tower(tower_selected, tower):
    if tower_selected:
        move_disk(tower_selected, tower)
        return None
    else:
        return tower


def move_disk(from_tower, to_tower):
    disk = from_tower.pop()
    if not disk:
        return False
    if can_move(disk, to_tower):
        to_tower.append(disk)
    else:
        from_tower.append(disk)


def can_move(disk, into_tower):
    if len(into_tower) == 0:
        return True
    last = into_tower[-1]
    if disk.get_width() < last.get_width():
        return True
    return False
