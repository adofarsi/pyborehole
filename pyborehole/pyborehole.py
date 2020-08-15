

def mesh_borehole(*, hole_diameter=1):
    """
    Mesh the borehole geometry.

    See https://en.wikipedia.org/wiki/Snell%27s_law

    Parameters
    ----------
    hole_diameter : float
        Diameter of the borehole.

    Returns
    -------
    theta : float
        refraction angle

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.

    >>> mesh_borehole(hole_diameter = 1)
    0.5605584137424605
    """
    import pygmsh
    import numpy as np

    hole_radius = 2 * hole_diameter
    box_size = 20 * hole_diameter
    mesh_size_hole = hole_diameter / 100
    mesh_size_box = box_size / 5

    geom = pygmsh.built_in.Geometry()

    circle = geom.add_circle(
        x0=[0.5 * box_size, 0.5 * box_size, 0.0],
        radius=hole_radius, lcar=mesh_size_hole,
        num_sections=4, make_surface=False
    )

    geom.add_rectangle(0.0, box_size, 0.0, box_size, 0.0,
                       lcar=mesh_size_box,
                       holes=[circle.line_loop])

    mesh = pygmsh.generate_mesh(geom, geo_filename="h.geo")

    ele_cnn = np.array(mesh.cells_dict["triangle"])
    nod_crd = np.array(mesh.points)

    print(ele_cnn.size)
    print(nod_crd.size)
    pass
