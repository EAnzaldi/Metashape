import Metashape as meta

#Matching accuracy (downscaling by factor of x)
Highest = 0
High = 1
Medium = 2
Low = 4
Lowest = 8
#Depths maps accuracy
Ultra_dep = 1
High_dep = 2
Medium_dep = 4
Low_dep = 8
Lowest_dep = 16

doc = meta.app.document #currently opened document in actual Metashape window
""" try: doc.open("D:\ellyb\POLITO\03\Droni\Esercitazioni\Py\PP1.psz")
except RuntimeError:
    meta.Application.messageBox("Can't open project")"""

meta.Application.gpu_mask=1; #1 GPU activated (binary value) 
chunk=doc.chunk
#for chunk in doc.chunks:
    #Align photos   
chunk.matchPhotos(downscale = Medium, #accuracy
generic_preselection = True,
filter_stationary_points = True,
keypoint_limit = 40000, #default
tiepoint_limit = 4000) #default
#Align cameras
chunk.alignCameras()
#doc.save()
chunk.buildDepthMaps(downscale=Medium_dep, filter_mode=meta.MildFiltering, reuse_depth=True)
chunk.buildPointCloud(point_colors=True, point_confidence=True)


