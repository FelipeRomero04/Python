def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    return tuple((i for i in coordinate))

# print(convert_coordinate('4R'))


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    
    return tuple((i for i in azara_record[1])) == rui_record[0][1]


# def clean_up(combined_record_group):
#     """Clean up a combined record group into a multi-line string of single records.

#     :param combined_record_group: tuple - everything from both participants.
#     :return: str - everything "cleaned", excess coordinates and information are removed.

#     The return statement should be a multi-lined string with items separated by newlines.

#     (see HINTS.md for an example).
#     """

#     record_formated = ''

#     for record in combined_record_group:
#         previw_record = ()

#         for cord in record:
#             if len(cord) == 2 and isinstance(cord, str):
#                 continue
#             previw_record += (cord,)
        
#         record_formated += f'{previw_record}\n'
#     return record_formated
               

def clean_up(combined_record_group):
    """
 
    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    combined_records = tuple(i[:1]+i[2:] for i in combined_record_group)
    report = "\n".join(str(record) for record in combined_records) + "\n"
    return report

print(clean_up(((
                ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
                ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
                ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
                ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
                ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
                ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange'),
                ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
                ('Model Ship in Large Bottle', '8A', 'Harbor Managers Office', ('8', 'A'), 'Purple'),
                ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
                ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
                ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
                ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
                ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')))))
        