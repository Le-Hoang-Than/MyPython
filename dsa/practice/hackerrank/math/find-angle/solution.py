import math

if __name__ == '__main__':
    AB = float(input())
    BC = float(input())
    angle_rad = math.atan(AB / BC)
    angle_deg = math.degrees(angle_rad)
    print(f'{round(angle_deg)}\u00b0')
