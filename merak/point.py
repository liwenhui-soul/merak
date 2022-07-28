#!/usr/bin/env python3

import numpy as np
from typing import List, Dict


class Point(object):
    def __init__(self, id: int, vector: np.ndarray, neighbors: Dict[int, List[int]], propertis:Dict[str,object]) -> None:
        self.id = id
        self.vector = vector
        self.neighbors = neighbors
        self.properties = propertis