import trimesh
import numpy as np

cube = trimesh.creation.box(extents=(2, 2, 2), transform=trimesh.transformations.translation_matrix([1, 1, 1]))

p1 = np.array([0, 0, 1])
p2 = np.array([2, 1, 2])
p3 = np.array([1, 2, 2])

normal = np.cross(p2 - p1, p3 - p1)
normal = normal / np.linalg.norm(normal)

plane_normal = -normal
plane_origin = p1
bottom_half = trimesh.intersections.slice_mesh_plane(cube, plane_normal, plane_origin, cap=True)

scene = trimesh.Scene()

bottom_half.visual.face_colors = [200, 50, 50, 180]
scene.add_geometry(bottom_half)

edges = cube.edges_unique
lines = []

for edge in edges:
    pt1, pt2 = cube.vertices[edge[0]], cube.vertices[edge[1]]
    lines.append(np.stack([pt1, pt2]))

scene.set_camera(
    distance=3.0,
    center=[1, 1, 1],
    angles=[np.radians(30), np.radians(45), 0]
)

scene.show(resolution=(600, 400))
