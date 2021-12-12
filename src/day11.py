"""day 11 module"""

from typing import Tuple, List, Dict


class Octopus:
    def __init__(
        self,
        idx: Tuple[int, int],
        energy_level: int,
        all_ids: List[Tuple[int, int]],
        dims: Tuple[int, int],
    ):
        self.idx = idx
        self.row_id = idx[0]
        self.col_id = idx[1]
        self.all_ids = all_ids
        self.energy_level = energy_level
        self.flashed_this_turn: bool = False
        self.num_rows = dims[0]
        self.num_cols = dims[1]
        self.neighbor_idxs = self.set_neighbor_idx(all_ids)
        self.neighbors: List["Octopus"] = []
        self._turn_number = -1

    def set_neighbor_idx(self, all_ids) -> List[Tuple[int, int]]:
        possible_neighbors = [
            (self.idx[0], self.idx[1] - 1),  # left
            (self.idx[0], self.idx[1] + 1),  # right
            (self.idx[0] - 1, self.idx[1]),  # above
            (self.idx[0] + 1, self.idx[1]),  # below
            (self.idx[0] - 1, self.idx[1] - 1),  # row up and left
            (self.idx[0] - 1, self.idx[1] + 1),  # row down and left
            (self.idx[0] + 1, self.idx[1] - 1),  # row up and right
            (self.idx[0] + 1, self.idx[1] + 1),  # row down and right
        ]
        neighbor_idx = []
        for idx in possible_neighbors:
            if idx[0] < 0 or idx[1] < 0:  # look for out of bounds
                continue
            if (
                idx[0] > self.num_rows or idx[1] > self.num_cols
            ):  # look for out of bounds
                continue
            # corner
            if abs(self.col_id - idx[1]) == 1 and abs(self.row_id - idx[0]) == 1:
                neighbor_idx.append(idx)
            # cardinal
            elif abs(self.col_id - idx[1]) == 1:
                neighbor_idx.append(idx)
            elif abs(self.row_id - idx[0]) == 1:
                neighbor_idx.append(idx)
        return neighbor_idx

    def take_a_turn(self, turn_no: int):
        "Gets ran after explicitly bumping the energy_level by 1"
        if turn_no == self._turn_number and self.flashed_this_turn:
            return None
        elif turn_no == self._turn_number and not self.flashed_this_turn:
            pass
        elif turn_no > self._turn_number and not self.flashed_this_turn:
            if abs(turn_no - self._turn_number) > 1:
                print("issue, trying to skip turns")
                raise ValueError
            self._turn_number = turn_no  # should equate to  +=1
        elif turn_no > self._turn_number and self.flashed_this_turn:
            print(
                f"octopus {self.idx} already flashed on turn {turn_no} but internal set to {self._turn_number}"
            )
        else:
            print(
                f"{self.idx}, {self._turn_number}, {turn_no}, {self.flashed_this_turn}"
            )
            raise ValueError("error at take_a_turn")

        if self.energy_level > 9:
            self.flash()

    def flash(self):
        # print(f"octopus {self.idx} blowing up!")
        self.flashed_this_turn = True
        octopus: Octopus
        for octopus in self.neighbors:
            # print(f"octopus {self.idx} is flashing {octopus.idx}")
            octopus.get_flashed(turn_no=self._turn_number)

    def get_flashed(self, turn_no: int) -> None:
        # print(f"octopus {self.idx} for flashed")
        self.energy_level += 1
        if self.flashed_this_turn:
            return None
        else:
            self.take_a_turn(turn_no=turn_no)
            return None

    def get_ready_to_take_a_turn(self):
        self.flashed_this_turn = False

    def reset_energy(self):
        self.energy_level = 0

    def bump_energy_level(self):
        self.energy_level += 1

    def set_neighbors(self, octopuses: List["Octopus"]):
        neighbors: List["Octopus"] = [
            o for o in octopuses if o.idx in self.neighbor_idxs
        ]
        self.neighbors = neighbors


def get_data(filepath: str = "./data/day11_sample.txt") -> List[List[int]]:
    with open(filepath, "r") as f:
        raw_data = f.readlines()
    line: str
    data: List[List[int]] = []
    for line in raw_data:
        data.append([int(x) for x in line.strip()])

    return data


class Octopuses:
    def __init__(
        self,
        data: List[List[int]],
        octopuses: List["Octopus"],
        all_ids: List[Tuple[int, int]],
    ):
        self.octopuses = octopuses
        self.data = data
        self.grid = data
        self.octopus_grid = None
        self.all_ids = all_ids
        self.initialize_grid()
        self.update_grid()
        self.show_grid()
        for octopus in self.octopuses:
            octopus.set_neighbor_idx(all_ids)
            octopus.set_neighbors(self.octopuses)
        self.num_flashes: Dict[int, int] = dict()

    def yield_octopus(self):
        for octopus in self.octopuses:
            yield octopus

    def initialize_grid(self):
        octopuses = self.yield_octopus()
        octopus_grid = []
        for row in self.data:
            new_col = []
            for v in row:
                new_col.append(next(octopuses))
            octopus_grid.append(row)
        self.grid = self.data
        self.octopus_grid = octopus_grid

    def show_grid(self):
        for row in self.grid:
            print(row)

    def update_grid(self):
        new_grid: List[List[int]] = []  # [[x for x in ls] for ls in self.data]
        get_octopus = self.yield_octopus()
        for i, octopuse_energy_levels in enumerate(self.grid):
            new_row: List[int] = []
            for j, level in enumerate(octopuse_energy_levels):
                octo = next(get_octopus)
                new_row.append(octo.energy_level)
            new_grid.append(new_row)
        self.grid = new_grid

    def take_steps(self, num_steps: int):

        for i in range(num_steps):
            # first bump energy levels
            for octopus in self.octopuses:
                octopus.get_ready_to_take_a_turn()
                octopus.bump_energy_level()
            # now check for any flashing and domino effect flashing
            for octopus in self.octopuses:
                octopus.take_a_turn(turn_no=i)
            for octopus in self.octopuses:
                if octopus.flashed_this_turn:
                    octopus.reset_energy()
            self.num_flashes[i + 1] = sum([o.flashed_this_turn for o in self.octopuses])
            print(f"Number of flashes at step:{i} {self.num_flashes[i+1]}")
            self.update_grid()
            self.show_grid()
            print("*" * 20)


def main(filepath: str = "./data/day11_sample.txt", num_steps: int = 1):

    data = get_data(filepath)

    all_ids = [(i, j) for i in range(len(data)) for j in range(len(data[0]))]
    all_energy_levels = []
    for row in data:
        for v in row:
            all_energy_levels.append(v)
    num_rows = len(data)
    num_cols = len(data[0])
    octopuses_ls = []
    for i, idx in enumerate(all_ids):
        octopuses_ls.append(
            Octopus(
                idx,
                energy_level=all_energy_levels[i],
                all_ids=all_ids,
                dims=(num_rows, num_cols),
            )
        )
    octopuses = Octopuses(data, octopuses_ls, all_ids)

    octopuses.take_steps(num_steps)
    return octopuses


if __name__ == "__main__":
    num_steps = 100
    octopuses = main("./data/day11_sample.txt", num_steps)
    print(
        f"Total number of flashes: {sum([v for v in octopuses.num_flashes.values()])}"
    )
