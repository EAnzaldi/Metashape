import Metashape as meta

#alignment accuracy (each side x*original)
Highest = 0
High = 1
Medium = 2
Low = 4
Lowest = 8

#depths maps accuracy
Ultra_dep = 1
High_dep = 2
Medium_dep = 4
Low_dep = 8
Lowest_dep = 16

#maximum confidence filtered
maxc=3;

doc = meta.app.document #currently opened document
chunk=doc.chunk

chunk.matchPhotos(downscale = Medium, #accuracy
generic_preselection = True, #default
filter_stationary_points = True, #default
keypoint_limit = 40000, #default
tiepoint_limit = 4000) #default
chunk.alignCameras()

chunk.buildDepthMaps(
    downscale=Medium_dep, #accuracy
    filter_mode=meta.MildFiltering, #default
    reuse_depth=True) #enable reuse depth maps option
chunk.buildPointCloud(
    point_colors=True, #default
    point_confidence=True) #enable point confidence calculation

pc = chunk.point_cloud #point cloud just generated
pc.setConfidenceFilter(0, maxc) #filter only low-confidence points
pc.removePoints(list(range(128))) #removes activated points
pc.resetFilters() #reset to activate remaining points