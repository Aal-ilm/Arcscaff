import arcpy
import os

# Set workspace where your shapefiles are located
workspace = r"C:\Users\core-admin\Documents\ArcGIS\Projects\ArchiveAlpha\Data\Maine_Town_and_Townships_Boundary_Polygons_-5924039825948470999"
arcpy.env.workspace = workspace

# Optional: enable overwriting outputs
arcpy.env.overwriteOutput = True

# List all shapefiles in the workspace
shapefiles = arcpy.ListFeatureClasses("*.shp")

# Print them to check
print("Shapefiles found:")
for shp in shapefiles:
    print(shp)

# Example: add shapefiles to a map in ArcGIS Pro
project_path = r"C:\Users\core-admin\Documents\ArcGIS\Projects\ArchiveAlpha\ArchiveAlpha.aprx"
aprx = arcpy.mp.ArcGISProject(project_path)

# Select the first map in the project
map_obj = aprx.listMaps()[0]

# Add each shapefile to the map
for shp in shapefiles:
    full_path = os.path.join(workspace, shp)
    map_obj.addDataFromPath(full_path)
    print(f"Added {shp} to the map.")

# Save the project
aprx.save()
print("All shapefiles loaded into the map successfully!")
