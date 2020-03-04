# # The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species
# # (Hint: You can a slightly edited version of our CSV code from a previous session to do this),
# # I recommend downloading the species data from the same source so the columns match.
# # Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer,
# # and you provide the species data along with your Python code.
# # The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# # You leave no trace of execution, except the resulting heatmap files.
# # You provide print statements that explain what the code is doing, e.g. Fishnet file generated.
#

import arcpy
import csv
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'E:\NRS568Python_Bartha\Class5'

# create the csv that is two data sets joined.
species = []
with open("species.csv") as population_csv:
    csv_reader = csv.reader(population_csv, delimiter=',')

    line_count = 0

    for row in csv_reader:
        if line_count != 0:
            if row[0] not in species:
                species.append(row[0])
        if line_count == 0:
            print "Column names are: " + str(row)
            line_count += 1
        line_count += 1

print species
print("Processed " + str(line_count) + " lines.")

# seperating two species list creating a loop then matching species list
for s in species:
    with open("species.csv") as population_csv:
        csv_reader = csv.reader(population_csv, delimiter=',')
        file = open(s[1:3] + ".csv", "w")
        file.write("name,Longitude,Latitude\n")
        for row in csv_reader:
            if row[0] == s:

                string = ",".join(row)
                string = string + "\n"
                file.write(string)
        file.close() # Essential to avoid an error about unreadable column names            
    # create your parameters for the data that you collected
    in_Table = s[1:3] + ".csv"
    x_coords = 'Longitude'
    y_coords = 'Latitude'

    out_Layer = "shtjyjhy"
    saved_Layer = s[1:3] + ".shp"
    # you then need to set the spatial reference of the data
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
    print  # code starts to fail after this line and I can not understand why.
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
    arcpy.CopyFeatures_management(lyr, saved_Layer)
# for some reason after shortening all three .csv files to 60 lines each with no difference in setup python had errors on line 56
# at the makexylayerevent.  before I tried to shorten the .csv lists to make it generate the last part of creating heatmaps
# it successfully made the fishnets and shapefiles for all the csv


# 2. Extact the Extent, it finds for you the XMin, XMax, YMin, YMax of the generated shapefile.
# get them from the shapefile

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    # you then need to create a fishnet for your data
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    outFeatureClass = s[1:3] + "2.shp"  # Name of output fishnet

    # Set the origin of the fishnet
    originCoordinate = str(XMin) + " " + str(YMin)  # Left bottom of our point data
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)  # This sets the orientation on the y-axis, so we head north
    cellSizeWidth = "0.25"
    cellSizeHeight = "0.25"
    numRows = ""  # Leave blank, as we have set cellSize
    numColumns = "" # Leave blank, as we have set cellSize
    oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
    labels = "NO_LABELS"
    templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
    geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                       cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                       oppositeCorner, labels, templateExtent, geometryType)
    if arcpy.Exists(outFeatureClass):
        print "Created Fishnet file successfully!"

    # # you then need to join the dataset with the fishnet you created to make the heatmap
    # # 4. Undertake a Spatial Join to join the fishnet to the observed points.
    #
    # target_features= s[1:3] + "2.shp"
    # join_features= s[1:3] + ".shp"
    # out_feature_class= s[1:3] + "heatmap.shp"
    # join_operation="JOIN_ONE_TO_ONE"
    # join_type="KEEP_ALL"
    # field_mapping=""
    # match_option="INTERSECT"
    # search_radius=""
    # distance_field_name=""
    #
    # arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
    #                            join_operation, join_type, field_mapping, match_option,
    #                            search_radius, distance_field_name)
    # # make sure it created the heatmap
    # if arcpy.Exists(out_feature_class):
    #     print "Created Heatmap file successfully!"
