import utils.autoanchor as autoAC

new_anchors = autoAC.kmean_anchors('E:/yolov7-main/data/cymeo.yaml', 9, 1280, 4.0, 20000, True)
print(new_anchors)