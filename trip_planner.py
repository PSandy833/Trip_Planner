import heapq
import math
from collections import defaultdict

class TripPlanner:
    def __init__(self, seg, raw_points):
        self.graph = defaultdict(list)
        self.poi_map = defaultdict(list)
        self.position_to_vertex = {}
        self.vertex_to_position = {}

        # Initialize the graph with road segments
        for start, end, distance in seg:
            self.graph[start].append((end, distance))
            self.graph[end].append((start, distance))

        # Initialize POIs
        for poi in raw_points:
            lat, lon, category, name = poi
            position = (lat, lon)
            self.position_to_vertex[position] = len(self.position_to_vertex)
            vertex = self.position_to_vertex[position]
            self.vertex_to_position[vertex] = position
            self.poi_map[vertex].append({"category": category, "name": name})

    def locate_all(self, dest_cat):
        result = []
        for vertex, pois in self.poi_map.items():
            for poi in pois:
                if poi["category"] == dest_cat:
                    result.append(self.vertex_to_position[vertex])
        return result

    def plan_route(self, src_lat, src_lon, dst_name):
        src_pos = (src_lat, src_lon)
        if src_pos not in self.position_to_vertex:
            return None

        src_vertex = self.position_to_vertex[src_pos]
        dst_vertex = self._find_vertex_intersect(dst_name)
        if dst_vertex is None:
            return None

        dist, pred = self._dijkstra(src_vertex)
        if dist[dst_vertex] == math.inf:
            return None

        route = []
        while dst_vertex is not None:
            route.append(self.vertex_to_position[dst_vertex])
            dst_vertex = pred[dst_vertex]

        return route[::-1]

    def find_nearby(self, src_lat, src_lon, dst_cat, n):
        src_pos = (src_lat, src_lon)
        if src_pos not in self.position_to_vertex:
            return []

        src_vertex = self.position_to_vertex[src_pos]
        dist, _ = self._dijkstra(src_vertex)

        nearby = []
        for vertex, pois in self.poi_map.items():
            if dist[vertex] != math.inf:
                for poi in pois:
                    if poi["category"] == dst_cat:
                        nearby.append((dist[vertex], self.vertex_to_position[vertex], poi))

        nearby.sort(key=lambda x: (x[0], x[2]["name"].lower()))
        return [f"{poi['name']} ({lat}, {lon})" for _, (lat, lon), poi in nearby[:n]]

    def _dijkstra(self, src):
        dist = {vertex: math.inf for vertex in self.graph}
        pred = {vertex: None for vertex in self.graph}
        dist[src] = 0
        heap = [(0, src)]

        while heap:
            curr_dist, curr_vertex = heapq.heappop(heap)

            if curr_dist > dist[curr_vertex]:
                continue

            for neighbor, weight in self.graph[curr_vertex]:
                new_dist = dist[curr_vertex] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    pred[neighbor] = curr_vertex
                    heapq.heappush(heap, (new_dist, neighbor))

        return dist, pred

    def _find_vertex_intersect(self, name):
        for vertex, pois in self.poi_map.items():
            for poi in pois:
                if poi["name"] == name:
                    return vertex
        return None

    def dist(self, point_1, point_2):
        lat1, lon1 = point_1
        lat2, lon2 = point_2
        return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

# Example Usage
# Road segments: (start, end, distance)
road_segments = [
    (0, 1, 5),
    (1, 2, 10),
    (2, 3, 3),
    (0, 3, 15)
]

# Points of Interest: (latitude, longitude, category, name)
pois = [
    (0, 0, "Restaurant", "Food Place"),
    (1, 1, "Museum", "Art Gallery"),
    (2, 2, "Park", "Central Park"),
    (3, 3, "Museum", "History Museum")
]

trip_planner = TripPlanner(road_segments, pois)

# Locate all museums
print(trip_planner.locate_all("Museum"))

# Plan route from (0, 0) to "Central Park"
print(trip_planner.plan_route(0, 0, "Central Park"))

# Find 2 nearby museums from (0, 0)
print(trip_planner.find_nearby(0, 0, "Museum", 2))
