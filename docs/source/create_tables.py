from tabulate import tabulate

building_name_table = [
                ["building_name_id", "character", 250, "noprec", "noscl", "An Id for a building name: 5","A hardware store" ],
                ["building_id", "integer", 4, "noprec", "noscl", "3928", "A unique id for a building" ]
                ]


rst_table = tabulate(building_name_table,tablefmt='rst')


json.dumps(rst_table)

print 