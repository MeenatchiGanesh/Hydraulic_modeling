# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# FloodPredictionScript.py
# Created on: 2023-08-28
# Description: Script for generating flood prediction maps using data from the Brahmaputra Basin.
# ---------------------------------------------------------------------------

class LicenseError(Exception):
    pass

# Import arcpy modules
import arcpy
from arcpy.sa import *
import os

arcpy.env.overwriteOutput = True

def generate_flood_prediction(cut_line_file, profile, output_raster, output_shapefile):
    # Define input parameters
    xs_cut_lines = cut_line_file
    profile = profile
    output_shapefile = output_shapefile
    output_raster = output_raster

    try:
        if arcpy.CheckExtension("3D") == "Available":
            arcpy.CheckOutExtension("3D")
        else:
            # Raise a custom exception
            raise LicenseError

        if arcpy.CheckExtension("Spatial") == "Available":
            arcpy.CheckOutExtension("Spatial")
        else:
            # Raise a custom exception
            raise LicenseError

        # Define local variables
        tin_workspace = "D:\\Brahmaputra_Flood\\TINs\\"
        raster_workspace = "D:\\Brahmaputra_Flood\\Rasters\\"
        boundary_shapefile = "D:\\Brahmaputra_Flood\\Boundaries\\boundary.shp"
        mapping_xs = "D:\\Brahmaputra_Flood\\MappingXS.shp"

        # Perform necessary data processing steps here
        
        # Example processing steps:
        # - Join relevant fields
        # - Create TIN
        # - Convert TIN to Raster
        # - Perform raster calculations
        # - Convert raster to polygon
        # - Dissolve polygons
        # - Check geometry and repair
        
        # Save results to specified paths
        output_raster_path = os.path.join(raster_workspace, output_raster)
        output_shapefile_path = os.path.join("D:\\Brahmaputra_Flood\\Shapefiles\\", output_shapefile)

        # You can customize and continue the data processing steps here
        
        print("Flood prediction generated successfully.")

    except LicenseError:
        print("3D or Spatial Analyst license is unavailable")

    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))

    finally:
        arcpy.CheckInExtension("3D")
        arcpy.CheckInExtension("Spatial")

if __name__ == '__main__':
    dataframe_dir = "D:\\Brahmaputra_Flood\\DataFrames\\"
    plan_list = ["ModelScenario"]
    cutline_path = "Results\\Cutlines"
    profile_list = ['Profile001']
    
    for plan_index in range(len(plan_list)):
        plan = plan_list[plan_index]
        geodatabase = plan + "\\" + plan + ".gdb"
        input_xs = os.path.join(dataframe_dir, geodatabase, cutline_path)
        
        for profile in profile_list:
            output_raster_name = "Flood_" + profile + ".tif"
            output_shapefile_name = "Flood_" + profile + ".shp"
            
            generate_flood_prediction(input_xs, profile, output_raster_name, output_shapefile_name)
