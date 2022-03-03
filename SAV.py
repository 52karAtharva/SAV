import math



print("\nSURFACE AREA AND VOLUME\n")
print("Enter the name of solid (Cube , Cuboid , Cylinder , Cone , Sphere , Hemisphere)")
shape = input("👉")
capshape = shape.capitalize()


print("What do you want to find (CSA , TSA , VOLUME)")
CTV = input("👉")
capCTV= CTV.upper()

pi = math.pi

# Cube

if capshape == "Cube"  and capCTV == "CSA":
    edge = int(input("Enter the edge : "))
    print(capCTV , "of your" , capshape,"is =",4 * (edge**2))

elif capshape == "Cube" and capCTV == "TSA":
    edge = int(input("Enter the edge : "))
    print(capCTV, "of your", capshape, "is =", 6 * (edge ** 2))

elif capshape == "Cube" and capCTV == "VOLUME":
    edge = int(input("Enter the edge : "))
    print(capCTV, "of your", capshape, "is =", edge ** 3)

# Cuboid

elif capshape == "Cuboid" and capCTV == "CSA":
    length = int(input("Enter the length : "))
    breadth = int(input("Enter the breadth : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", 2 * height * (length + breadth))

elif capshape == "Cuboid" and capCTV == "TSA":
    length = int(input("Enter the length : "))
    breadth = int(input("Enter the breadth : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", 2*((length * breadth) + (breadth * height) + (height * length)))

elif capshape == "Cuboid" and capCTV == "VOLUME":
    length = int(input("Enter the length : "))
    breadth = int(input("Enter the breadth : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", length * breadth * height)

# Cylinder

elif capshape == "Cylinder" and capCTV == "CSA":
    radius = int(input("Enter the radius : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", 2 * 22/7 * radius * height)

elif capshape == "Cylinder" and capCTV == "TSA":
    radius = int(input("Enter the radius : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", 2 * 22/7 * radius * (radius + height))

elif capshape == "Cylinder" and capCTV == "VOLUME":
    radius = int(input("Enter the radius : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", 22/7 * (radius**2) * height)

# Cone

elif capshape == "Cone" and capCTV == "CSA":
    radius = int(input("Enter the radius : "))
    slant_height = int(input("Enter the slant height : "))
    print(capCTV, "of your", capshape, "is =", 22/7 * radius * slant_height)

elif capshape == "Cone" and capCTV == "TSA":
    radius = int(input("Enter the radius : "))
    slant_height = int(input("Enter the slant height : "))
    print(capCTV, "of your", capshape, "is =", 22/7 * radius * (slant_height + radius))

elif capshape == "Cone" and capCTV == "VOLUME":
    radius = int(input("Enter the radius : "))
    height = int(input("Enter the height : "))
    print(capCTV, "of your", capshape, "is =", (22/7 * (radius**2) * height)/3)

# Sphere

elif capshape == "Sphere" and capCTV == "CSA":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", 4 * 22/7 * (radius**2))

elif capshape == "Sphere" and capCTV == "TSA":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", 4 * 22/7 * (radius**2))

elif capshape == "Sphere" and capCTV == "VOLUME":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", (4 * 22/7 * (radius**3))/3)

# Hemisphere

elif capshape == "Hemisphere" and capCTV == "CSA":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", 2 * 22/7 * (radius ** 2))

elif capshape == "Hemisphere" and capCTV == "TSA":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", 3 * 22/7 * (radius ** 2))

elif capshape == "Hemisphere" and capCTV == "VOLUME":
    radius = int(input("Enter the radius : "))
    print(capCTV, "of your", capshape, "is =", (2 * 22/7 * (radius ** 3)) / 3)
