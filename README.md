# Trip_Planner
# CS 214 FINAL PROJECT REPORT 
# INTRODUCTION
The report provides insight on the implementation of the Trip Planner project. The code utilizes a graph data structure to represent a map and road segments, as well as a hashtable for efficient storage and retrieval of points of interest (POI) information. The Trip Planner class offers three main functions: locate_all, plan_route, and find_nearby. These functions enable users to find and plan routes to POIs on a map, locate all POIs belonging to a specific category, find the shortest route from a source position to a particular POI, and retrieve a specified number of nearby POIs of a certain category.

The code begins by defining a set of eight principles, followed by a detailed description of the Trip Planner class and its functionalities. The class constructor initializes the Trip Planner object with road segments and raw POI data, utilizing various helper functions for position mapping, distance calculation, and graph traversal using Dijkstra's algorithm. The code also includes example test cases, demonstrating the functionality of the Trip Planner class. These tests showcase the capability of the code to locate POIs, plan routes, and find nearby POIs.

The analysis of this project aims to highlight the design and implementation choices made, evaluate the efficiency and correctness of the implemented functionalities, and provide insights into potential improvements or modifications.

# DESIGN CHOICES
# DEFINING FUNCTIONS IN THE CODE: Main Functions
def __init__(self, seg, raw_points): The TripPlanner class constructor initializes the trip planner object. It creates hash tables to map positions to vertices and vice versa. The road segments are transformed into a graph representation using the WuGraph class. The edges between vertices are set based on the road segments. The constructor also initializes a list of points-of-interest associated with each vertex in the road network. It iterates over the raw points-of-interest data, assigns positions and vertices to each point, and creates POI objects that are added to the list of POIs for the corresponding vertex. Overall, the constructor establishes the necessary data structures and algorithms to store and manipulate road segments and points-of-interest, enabling the trip planner to efficiently plan routes and provide information about nearby attractions.

def locate_all(self, dest_cat): The locate_all function is a method of the TripPlanner class. It iterates over the linked lists of points-of-interest associated with each vertex in the road network. For each point-of-interest, it checks if the category matches the provided destination category. If a match is found, the position of the point-of-interest is added to the result list. The function returns the list of positions for all points-of-interest that match the destination category. This function allows the trip planner to locate and retrieve all points-of-interest belonging to a specific category, facilitating further processing or display of relevant information to the user.

def plan_route(self, src_lat, src_lon, dst_name): The plan_route function is a method of the TripPlanner class. It finds the source and destination vertices based on latitude, longitude, and destination name. Using Dijkstra's algorithm, it calculates the shortest route from the source to the destination vertex. The positions along this route are added to the result list, representing the planned route. If a valid route exists, the function returns the list of positions; otherwise, it returns None. This function enables the trip planner to generate a route plan from a given source location to a specified destination, taking into account the road network graph and shortest path calculations.

def find_nearby(self, src_lat, src_lon, dst_cat, n): The find_nearby function in the TripPlanner class takes the source location, destination category, and the desired number of results as input. It returns a list of nearby points-of-interest that match the specified category.

To find nearby points-of-interest, the function computes the distances from the source vertex to all other vertices using Dijkstra's algorithm. It uses a binary heap to prioritize the vertices based on their distances. The function iterates over the vertices and inserts the indices of vertices with non-infinite distances into the binary heap. It then extracts the minimum value from the heap and processes the points-of-interest associated with that vertex. If a point-of-interest has the same category as the destination category, it is added to the result list. The process continues until the desired number of results is reached or there are no more points-of-interest or vertices to process. The function returns the list of nearby points-of-interest that match the destination category.
 
In summary, the find_nearby function leverages Dijkstra's algorithm and a binary heap to identify and retrieve nearby points-of-interest. By considering the source location, destination category, and desired number of results, it efficiently computes the distances and filters the points-of-interest to provide a relevant list of nearby locations. This capability enhances the trip planner's functionality by allowing users to explore and discover points-of-interest within a specific category in close proximity to their location.

# DEFINING FUNCTIONS IN THE CODE: Helper Functions
def _dijkstra(self, src): 
The _dijkstra function is a private method within the TripPlanner class that performs Dijkstra's algorithm to calculate the shortest distances from a given source vertex to all other vertices in the graph. To initialize the necessary data structures, the function creates arrays for distances (dist) and predecessors (pred) with appropriate initial values. The distance of the source vertex is set to 0, indicating that the distance from the source to itself is 0. A binary heap (heap) is created using the BinHeap class, with a comparison function that compares distances stored in the distance array.

The function enters a loop that continues until the heap is empty. Within each iteration, the vertex with the minimum distance (curr) is extracted from the heap. If the vertex has not been visited yet (comp[curr] is False), it is marked as visited. The function then iterates over the adjacent vertices of the current vertex. For each adjacent vertex (v), the weight of the edge connecting the current vertex to the adjacent vertex is retrieved from the graph. If the distance from the source vertex to the current vertex plus the weight of the edge is smaller than the current distance to the adjacent vertex (dist[v]), an update is performed. The distance and predecessor for the adjacent vertex are updated, and the adjacent vertex is inserted into the heap. After processing all adjacent vertices, the loop continues until the heap is empty, extracting vertices with the minimum distance and repeating the process. Finally, the function returns a list containing the distance array (dist) and the predecessor array (pred), which hold the shortest distances and predecessors for each vertex from the source.

In summary, the _dijkstra function applies Dijkstra's algorithm to determine the shortest distances and predecessors from a source vertex to all other vertices. By utilizing a binary heap for efficient vertex selection and updating the distance and predecessor information, this method plays a crucial role in the trip planner's ability to find optimal routes between different locations within the graph.

def _find_vertex_intersect(self, name): The _find_vertex_intersect method is a private function in the TripPlanner class that searches for a vertex in the graph based on a given name. It iterates through the points-of-interest array using a for loop and retrieves the linked list of points-of-interest associated with each index. Within a nested while loop, it compares the name of each point-of-interest with the given name. If a match is found, the index of the vertex is returned. If no match is found, it returns None. This method allows for efficient vertex identification by name within the graph data structure.

def _pos_to_ver(self, pos): The _pos_to_ver method is a private function in the TripPlanner class that converts a given position (pos) into its corresponding vertex in the graph. Within the function, the _v_map HashTable is utilized to store the mapping between positions and vertices. By invoking the get method of the HashTable and passing the position as the key, the corresponding vertex is retrieved from the HashTable.

This method provides an efficient way to map positions to vertices within the graph. By leveraging the key-value lookup functionality of the HashTable, the function avoids the need for linear search or iteration through the data structure. Instead, it directly retrieves the vertex associated with the given position.

In summary, the _pos_to_ver function plays a vital role in the trip planner by facilitating the conversion of positions to vertices. By utilizing the _v_map HashTable, it efficiently retrieves the vertex corresponding to a given position, allowing for seamless integration of position-based operations within the trip planning process.

def v_to_pos(self, v): The v_to_pos method is a function within the TripPlanner class that maps a vertex (v) to its corresponding position in the graph. The function uses the reverse_map HashTable data structure to retrieve the position associated with the given vertex. It calls the get method of the HashTable, passing the vertex as the key, and returns the value associated with that key.

In essence, the v_to_pos function performs a lookup operation on the reverse_map HashTable to retrieve the position corresponding to a given vertex. By using the vertex as the key, it efficiently retrieves the associated position value from the HashTable. This method enables the mapping of vertices to their respective positions in the graph.

Overall, the v_to_pos function is an essential component of the trip planner, allowing for efficient conversion of vertices to positions. By leveraging the key-value lookup functionality of the HashTable, it simplifies the process of retrieving the position associated with a given vertex, aiding in various graph-related calculations and operations.

def to_pos(self, pos): The to_pos method is a function within the TripPlanner class that converts a position object (pos) into a list of coordinates [x, y]. The function extracts the latitude and longitude values from the position object by accessing the lat and lon attributes respectively. It assigns the latitude to the variable x and the longitude to the variable y. Then, it constructs a list containing these coordinates [x, y].

In summary, the to_pos function performs a straightforward transformation of a position object into a list of coordinates. It facilitates the extraction and reformatting of latitude and longitude values, enabling the representation of a position in a more convenient format for further processing or usage within the trip planner.

def _to_raw_i(self, i): The _to_raw_i function is a method in the TripPlanner class that converts an object i into a list representation of its properties [m, n, p, r]. It extracts the latitude and longitude values from the position attribute of i and assigns them to variables m and n. The category and name properties of i are also retrieved and assigned to variables p and r. Finally, a list is constructed with these variables [m, n, p, r].

In summary, the _to_raw_i function provides a convenient way to transform an object's properties into a standardized list representation. By extracting specific attributes of the object i and assigning them to variables, it constructs a list that encapsulates the relevant information. This method is valuable for obtaining a compact and structured format of an object's properties, facilitating further processing or output requirements within the trip planner.


def dist(self, point_1, point_2): The dist function calculates the Euclidean distance between two points, point_1 and point_2, within the TripPlanner class.

The function subtracts the latitude of point_1 from the latitude of point_2, squares the result, and assigns it to the variable x. Similarly, it subtracts the longitude of point_1 from the longitude of point_2, squares the result, and assigns it to the variable y. Then, it computes the sum of x and y, takes the square root of the sum, and returns the result as the Euclidean distance.

In summary, the dist function uses the difference in latitude and longitude coordinates between two points to calculate their Euclidean distance. By squaring the differences, summing them, and taking the square root, it determines the straight-line distance between the two points. This method facilitates distance calculations between geographic locations and aids in various aspects of route planning and optimization within the trip planner.

# CHOICES OF ADT, DATA STRUCTURES AND ALGORITHMS
# Stack: Last-In-First-Out (LIFO)
Role: The stack ADT is used to store and manage data during various operations in the program, such as traversing vertices and tracking intermediate results.
Data Structure: Linked list stack.
Reasoning: The linked list implementation of the stack data structure was chosen because it provides efficient insertion and deletion operations at the top of the stack. The dynamic nature of linked lists allows for flexibility in managing the stack as elements are pushed and popped. Time complexity is O(1) for push and pop operations.

# Queue: First-In-First-Out
Role: The queue ADT is used for managing elements in a first-in, first-out (FIFO) manner during operations such as breadth-first search or processing adjacent vertices.
Data Structure: Ring buffer.
Reasoning: The ring buffer implementation of the queue data structure was selected due to its efficient memory utilization and constant-time enqueue and dequeue operations. Ring buffers provide a fixed-size circular buffer, which is suitable for scenarios where the maximum capacity is known in advance. Time complexity is O(1) for enqueue and dequeue operations.

# Dictionaries
Role: Dictionaries are used to store and retrieve key-value pairs efficiently, such as mapping positions to vertices and vice versa.
Data Structure: Hash table.
Reasoning: Hash tables were chosen as the data structure for dictionaries due to their constant-time average-case lookup, insertion, and deletion operations. Hash tables provide a good balance between time complexity and memory usage, making them suitable for efficient key-value pair management. Average-case O(1) for insertion, deletion, and lookup operations. In the worst case, the time complexity can be O(n), where n is the number of key-value pairs.

# Dijkstra's Algorithm
Role: Dijkstra's algorithm is used to find the shortest path between two vertices in the graph.
Reasoning: Dijkstra's algorithm was chosen because it guarantees finding the shortest path in a weighted graph with non-negative edge weights. It provides an efficient and effective solution to the problem of finding the optimal route between points of interest. Time complexity is O((|V| + |E|) log |V|), where |V| is the number of vertices and |E| is the number of edges in the graph. This complexity arises from the usage of a priority queue (implemented with a binary heap) for efficient selection of the next vertex with the minimum distance.

# Depth-First Search (DFS)
Role: DFS is utilized to traverse the graph and explore connected vertices.
Reasoning: DFS was chosen due to its simplicity and ability to efficiently traverse connected components of a graph. It is particularly useful in scenarios where exploration of the entire graph or connected regions is required. Time complexity is  O(|V| + |E|), where |V| is the number of vertices and |E| is the number of edges in the graph. DFS visits each vertex and each edge once.

# Binary Heap
Role: Binary heaps are used to implement priority queues, enabling efficient management of elements with varying priorities.
Reasoning: Binary heaps were selected for implementing priority queues because they offer logarithmic time complexity for insertion, deletion, and finding the minimum element. The choice of binary heap ensures efficient prioritization and ordering of elements, crucial for certain operations in the program like finding nearby points of interest. Time complexity is O(log n) for insertion, deletion, and finding the minimum element, where n is the number of elements in the heap. The heap operations maintain the heap property and ensure efficient access to the minimum element.

Overall, the selection of data structures and algorithms was based on their efficiency, suitability for the specific problem requirements, and the trade-offs between time complexity, space complexity, and ease of implementation.


# OPEN-ENDED QUESTIONS 
As an implementer of a trip planner application, the task of enhancing its features often involves making important design and implementation decisions. This essay explores two scenarios where modifications are requested by the boss: prioritizing businesses offering discounts in rankings and introducing a "shadow ban" feature to filter certain businesses. We will examine the potential positive and negative effects of these changes and discuss the considerations that should guide our decision-making process.

# Prioritizing Businesses with Discounts:
If tasked with making businesses offering discounts rank higher in the trip planner, several design and implementation adjustments can be considered. This may involve incorporating a discount factor or weight in the algorithm used to find nearby locations and adjusting the ranking criteria to include the discount factor along with other factors such as proximity, ratings, and reviews. While this change can have positive effects, such as encouraging businesses to provide discounts and increasing user satisfaction, it is important to also recognize the potential negative impacts.

# Positive Effects:
By prioritizing businesses offering discounts, users are incentivized to utilize the trip planner, attracted by the prospect of cost savings. This fosters a competitive environment among businesses, leading to improved deals and offerings. Additionally, the inclusion of discounts can enhance user satisfaction and promote positive engagement with the platform.

# Negative Effects:
Introducing a bias towards businesses offering discounts may inadvertently overshadow non-discounted businesses. This can impact their visibility, potentially affecting their revenue and competitiveness. Striking a balance between promoting businesses offering discounts and ensuring fairness to all businesses is crucial to maintain a diverse and inclusive marketplace.

In considering whether to implement this feature, we must assess its alignment with the company's goals and values. It is essential to evaluate the potential impact on user experience, fairness, and the overall integrity of the platform. Alternative approaches should also be explored to promote fairness and inclusivity among businesses, such as providing additional exposure for businesses based on overall quality rather than solely relying on discounts.

# Shadow Banning Certain Businesses:
The request to introduce a "shadow ban" feature, where businesses would be invisible to users in query results, raises complex considerations regarding user experience, fairness, and the potential consequences for businesses.

# Positive Effects:
Implementing a shadow ban feature can help filter out spam, fraudulent, or low-quality businesses, thereby enhancing the user experience. By ensuring that only legitimate and reputable businesses are displayed, users can have greater trust in the platform and its recommendations. This can contribute to maintaining the overall quality and reliability of the trip planner.

# Negative Effects:
The introduction of a shadow ban feature must be approached with caution. Arbitrary or unfair application of shadow banning criteria can lead to bias and potential discrimination. Excluding businesses without transparent and justifiable reasons may result in the loss of visibility and potential revenue for those affected. Proper implementation and ongoing monitoring are necessary to avoid false positives and unintended consequences.

Deciding whether to implement a shadow ban feature requires a careful evaluation of the purpose and policies of the trip planner platform, legal considerations, and ethical implications. Striking a balance between maintaining a high-quality user experience and ensuring fairness and transparency in how businesses are treated is of paramount importance.

# Conclusion:
As implementers of a trip planner application, making modifications to the features involves thoughtful consideration of their potential effects. Prioritizing businesses offering discounts can provide benefits such as encouraging discounts and increasing user satisfaction, but it must be balanced with fairness to all businesses. Introducing a shadow ban feature can enhance user experience and platform integrity, but careful implementation is necessary to prevent unintended consequences and maintain fairness. Ultimately, decisions regarding these modifications should be guided by the goal of creating a trip planner that is both valuable for users and supportive of a diverse and thriving business ecosystem. 

