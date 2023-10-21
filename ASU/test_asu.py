# Import modules
from __future__ import absolute_import
import osm2gmns as og
import pandas as pd
from grid2demand import GRID2DEMAND
import path4gmns as pg


# # Produce routable network along with POIs
# net = og.getNetFromFile('asu.osm', 
#                         network_types=('auto','bike','walk'), 
#                         POI=True,
#                         POI_sampling_ratio=1,
#                         strict_mode=True, 
#                         min_nodes=10,
#                         default_lanes=True, 
#                         default_speed=True, 
#                         default_capacity=True, 
#                         start_node_id=1, 
#                         start_link_id=1)
# default_lanes_dict = {'motorway': 4, 'trunk': 3, 'primary': 3, 'secondary': 2, 'tertiary': 2,
#                       'residential': 1, 'service': 1, 'cycleway':1, 'footway':1, 'track':1,
#                       'unclassified': 1, 'connector': 2}
# default_speed_dict = {'motorway': 120, 'trunk': 100, 'primary': 80, 'secondary': 60, 'tertiary': 40,
#                       'residential': 30, 'service': 30, 'cycleway':5, 'footway':5, 'track':30,
#                       'unclassified': 30, 'connector':120}
# default_capacity_dict = {'motorway': 2300, 'trunk': 2200, 'primary': 1800, 'secondary': 1600, 'tertiary': 1200,
#                       'residential': 1000, 'service': 800, 'cycleway':800, 'footway':800, 'track':800,
#                       'unclassified': 800, 'connector':9999}
# og.connectPOIWithNet(net)
# og.generateNodeActivityInfo(net)
# og.outputNetToCSV(net)


# # grid2demand
# if __name__ == "__main__":
#     # Step 0: Specify input directory, if not, use current working directory as default input directory
#     input_dir = "C:/Users/aditr/OneDrive/Desktop/Arizona State University/GitHub/Python Modeling/ASU/Code/"
    
#     # Initialize a GRID2DEMAND object
#     gd = GRID2DEMAND(input_dir)

#     # Step 1: Load node and poi data from input directory
#     node_dict, poi_dict = gd.load_network.values()

#     # Step 2: Generate zone dictionary from node dictionary by specifying number of x blocks and y blocks
#     zone_dict = gd.net2zone(node_dict, num_x_blocks=25, num_y_blocks=25)
#     # # Generate zone based on grid size with 10 km width and 10km height for each zone
#     # zone_dict = gd.net2zone(node_dict, cell_width=10, cell_height=10)

#     # Step 3: synchronize geometry info between zone, node and poi
#     #       add zone_id to node and poi dictionaries
#     #       also add node_list and poi_list to zone dictionary
#     updated_dict = gd.sync_geometry_between_zone_and_node_poi(zone_dict, node_dict, poi_dict)
#     zone_dict_update, node_dict_update, poi_dict_update = updated_dict.values()

#     # Step 4: Calculate zone-to-zone od distance matrix
#     zone_od_distance_matrix = gd.calc_zone_od_distance_matrix(zone_dict_update)

#     # Step 5: Generate poi trip rate for each poi
#     poi_trip_rate = gd.gen_poi_trip_rate(poi_dict_update)

#     # Step 6: Generate node production attraction for each node based on poi_trip_rate
#     node_prod_attr = gd.gen_node_prod_attr(node_dict_update, poi_trip_rate)

#     # Step 6.1: Calculate zone production and attraction based on node production and attraction
#     zone_prod_attr = gd.calc_zone_prod_attr(node_prod_attr, zone_dict_update)

#     # Step 7: Run gravity model to generate agent-based demand
#     df_demand = gd.run_gravity_model(zone_prod_attr, zone_od_distance_matrix)

#     # Step 8: generate agent-based demand
#     df_agent = gd.gen_agent_based_demand(node_prod_attr, zone_prod_attr, df_demand=df_demand)

#     # You can also view and edit the package setting by using gd.pkg_settings
#     print(gd.pkg_settings)

#     # Step 9: Output demand, agent, zone, zone_od_dist_table, zone_od_dist_matrix files
#     gd.save_demand
#     gd.save_agent
#     gd.save_zone
#     gd.save_zone_od_dist_table
#     gd.save_zone_od_dist_matrix


# # path4gmns zone synthesis
# network = pg.read_network()

# # by default, grid_dimension is 8, total_demand is 10,000,
# # time_budget is 120 min, mode is 'auto'
# pg.network_to_zones(network)
# pg.output_zones(network)
# # synthesized demand will be saved as demand.csv 
# # and will overwrite any existing demand file with the same name.
# # synthesized zone will be output as zone.csv.
# pg.output_synthesized_demand(network)


# # path4gmns load demand
# network = pg.read_network()
# # it reads zone.csv by default
# pg.read_zones(network)
# # it reads demand.csv by default
# pg.load_demand(network)


# # path4gmns shortest path
# # create the network object by reading node.csv and link.csv
# network = pg.read_network(length_unit='meter', speed_unit='kph')
# x = 211
# y = 346

# # node path from node 1 to node 2
# print('\nshortest path (node id) from node',x,'to node',y,','
#       +network.find_shortest_path(x, y, mode='r'))
# # link path from node 1 to node 2
# print('\nshortest path (link id) from node',x,'to node',y,','
#       +network.find_shortest_path(x, y, mode='r',seq_type='link'))


# # path4gmns traffic assignment
# network = pg.read_network()
# pg.read_zones(network)
# pg.load_demand(network)

# # specify the parameters for traffic assignment
# column_gen_num = 10
# column_update_num = 10

# # path-based UE only
# pg.perform_column_generation(column_gen_num, column_update_num, network)
# pg.perform_simple_simulation(network)
# pg.output_agent_trajectory(network)
# # if you do not want to include geometry info in the output file,
# # use pg.output_columns(network, False)
# # output column information to agent.csv
# pg.output_columns(network)
# # output link performance to link_performance.csv
# pg.output_link_performance(network)


# # path4gmns accessibility and equity evaluation
# network = pg.read_network()
# pg.read_zones(network)
# pg.evaluate_accessibility(network, single_mode=False)
# pg.evaluate_equity(network, single_mode=False)
