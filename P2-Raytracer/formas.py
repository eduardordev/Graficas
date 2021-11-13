from libreria import *


class Plane(object):


    def __init__(self, position, normal, material):
        self.position = position
        self.normal = norm(normal)
        self.material = material

    def ray_intersects(self, origin, direction):
        d = dot(direction, self.normal)

        if abs(d) > 0.0001:
            t = dot(self.normal, sub(self.position, origin)) / d
            if t > 0:
                hit = suma(origin, V3(direction.x * t,
                          direction.y * t, direction.z * t))

                return Intersect(distance=t, point=hit, normal=self.normal)

        return None


class Cube(object):


    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        mid_size = size / 2

        self.planes = [
            Plane(suma(position, V3(mid_size, 0, 0)), V3(1, 0, 0), material),
            Plane(suma(position, V3(-mid_size, 0, 0)), V3(-1, 0, 0), material),
            Plane(suma(position, V3(0, mid_size, 0)), V3(0, 1, 0), material),
            Plane(suma(position, V3(0, -mid_size, 0)), V3(0, -1, 0), material),
            Plane(suma(position, V3(0, 0, mid_size)), V3(0, 0, 1), material),
            Plane(suma(position, V3(0, 0, -mid_size)), V3(0, 0, -1), material)
        ]

    def ray_intersects(self, origin, direction):
        epsilon = 0.001

        min_bounds = [0, 0, 0]
        max_bounds = [0, 0, 0]

        for i in range(3):
            min_bounds[i] = self.position[i] - (epsilon + self.size / 2)
            max_bounds[i] = self.position[i] + (epsilon + self.size / 2)

        t = float("inf")
        intersect = None
        texture_coords = None

        for plane in self.planes:
            plane_intersection = plane.ray_intersects(origin, direction)

            if plane_intersection is not None:
                if (
                    plane_intersection.point[0] >= min_bounds[0]
                    and plane_intersection.point[0] <= max_bounds[0]
                ):
                    if (
                        plane_intersection.point[1] >= min_bounds[1]
                        and plane_intersection.point[1] <= max_bounds[1]
                    ):
                        if (
                            plane_intersection.point[2] >= min_bounds[2]
                            and plane_intersection.point[2] <= max_bounds[2]
                        ):
                            if plane_intersection.distance < t:
                                t = plane_intersection.distance
                                intersect = plane_intersection

                                if abs(plane.normal[2]) > 0:
                                    coord0 = (
                                        plane_intersection.point[0] - min_bounds[0]) / (max_bounds[0] - min_bounds[0])
                                    coord1 = (
                                        plane_intersection.point[1] - min_bounds[1]) / (max_bounds[1] - min_bounds[1])

                                elif abs(plane.normal[1]) > 0:
                                    coord0 = (
                                        plane_intersection.point[0] - min_bounds[0]) / (max_bounds[0] - min_bounds[0])
                                    coord1 = (
                                        plane_intersection.point[2] - min_bounds[2]) / (max_bounds[2] - min_bounds[2])

                                elif abs(plane.normal[0]) > 0:
                                    coord0 = (
                                        plane_intersection.point[1] - min_bounds[1]) / (max_bounds[1] - min_bounds[1])
                                    coord1 = (
                                        plane_intersection.point[2] - min_bounds[2]) / (max_bounds[2] - min_bounds[2])

                                texture_coords = [coord0, coord1]

        if intersect is None:
            return None

        return Intersect(
            distance=intersect.distance, point=intersect.point, normal=intersect.normal, text_coords=texture_coords
        )


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersects(self, origin, direction):
        L = sub(self.center, origin)
        tca = dot(L, direction)
        l = length(L)

        d2 = l**2 - tca**2

        if d2 > self.radius ** 2:
            return None

        thc = (self.radius**2 - d2)**(1/2)

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        hit = suma(origin, mul(direction, t0))
        normal = norm(sub(hit, self.center))
        # en t0 pego el rayo
        return Intersect(distance=t0, normal=normal, point=hit)

class Triangle(object):
    def __init__(self, vertices, material):
        self.vertices = vertices
        self.material = material

    def ray_intersects(self, origin, direction):
        epsilon = 0.001
        v0, v1, v2 = self.vertices
        normal = cross(sub(v1, v0), sub(v2, v0))
        determinant = dot(normal, direction)

        if abs(determinant) < epsilon:
            return None

        distance = dot(normal, v0)
        t = (dot(normal, origin) + distance) / determinant
        if t < 0:
            return None

        point = suma(origin, mul(direction, t))
        u, v, w = barycentric(v0, v1, v2, point)

        if w < 0 or v < 0 or u < 0:  # 0 is actually a valid value! (it is on the edge)
            return None
        
        return Intersect(distance=distance, point=point, normal=norm(normal))
class Material(object):
    def __init__(self, diffuse=WHITE, albedo=(1, 0, 0, 0), spec=0, refractive_index=1, texture = None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = texture


class Intersect(object):
    def __init__(self, distance, point, normal, text_coords = None):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.text_coords = text_coords
        

# luz puntual


class Light(object):
    def __init__(self, position, intensity, color=WHITE):
        self.position = position
        self.intensity = intensity
        self.color = color