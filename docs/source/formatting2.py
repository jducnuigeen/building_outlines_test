[['      lifecycle_stage_id ', 'integer', '_', '32', '0', '_'], ['value', 'varchar', '40', '_', '_', 'The stage of a buildings lifecycle.']]
           
[['      use_id ', 'integer', '_', '32', '0', '_'], ['value', 'varchar', '40', '_', '_', 'The building use, maintained for the Topo50 map series.']]
           
[['      building_id ', 'integer', '_', '32', '0', '_'], ['begin_lifespan', 'date', '_', '_', '_', 'The date that the building was first captured in the system.'], ['end_lifespan', 'date', '_', '_', '_', 'The date that a building was either replaced or disused.']]
           
[['      building_outline_id ', 'integer', '_', '32', '0', '_'], ['building_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['capture_method_id', 'integer', '_', '32', '0', 'Unique identifier for the building,  blah blah blah second line of comment'], ['capture_source_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['lifecycle_stage_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['suburb_locality_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['town_city_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['territorial_authority_id', 'integer', '_', '32', '0', 'Unique identifier for the building.'], ['begin_lifespan', 'date', '_', '_', '_', 'The date that the building was first captured in the system.'], ['end_lifespan', 'date', '_', '_', '_', 'The date that a building was either replaced or disused.'], ['shape', 'geometry', '_', '_', '_', 'The geometry of the building.']]
           
[['      building_name_id ', 'integer', '_', '32', '0', '_'], ['building_id', 'integer', '_', '32', '0', '_'], ['building_name', 'varchar', '250', '_', '_', '_'], ['begin_lifespan', 'date', '_', '_', '_', '_'], ['end_lifespan', 'date', '_', '_', '_', '_']]
           
[['      building_use_id ', 'integer', '_', '32', '0', '_'], ['building_id', 'integer', '_', '32', '0', '_'], ['use_id', 'integer', '_', '32', '0', '_'], ['begin_lifespan', 'date', '_', '_', '_', '_'], ['end_lifespan', 'date', '_', '_', '_', '_']]
           
[['      lifecycle_id ', 'integer', '_', '32', '0', '_'], ['parent_building_id', 'integer', '_', '32', '0', '_'], ['building_id', 'integer', '_', '32', '0', '_']]
