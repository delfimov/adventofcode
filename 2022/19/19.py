import re

def solve(time, o, blueprint, r, r_func):
    for n, robot_ore_cost, robot_clay_cost, robot_obsidian_cost, robot_obsidian_cost_clay, robot_geode_cost, robot_geode_cost_obsidian in blueprint:
        max_cost_ore = max(robot_ore_cost, robot_clay_cost, robot_obsidian_cost, robot_geode_cost)
        def dfs(max_cost, time_left, robot_type,
                robot_ore, robot_clay, robot_obsidian, robot_geode, 
                avail_ore, avail_clay, avail_obsidian, avail_geode):
            if (robot_type == 0 and robot_ore >= max_cost_ore or
                robot_type == 1 and robot_clay >= robot_obsidian_cost_clay or
                robot_type == 2 and (robot_obsidian >= robot_geode_cost_obsidian or robot_clay == 0) or
                robot_type == 3 and robot_obsidian == 0 or
                avail_geode + robot_geode * time_left + o[time_left] <= max_cost):
                return max_cost
            for time in range(time_left, 0, -1):
                if robot_type == 0 and avail_ore >= robot_ore_cost:
                    for robot_type in range(0, 4):
                        max_cost = dfs(max_cost, time - 1, robot_type, 
                                robot_ore + 1, robot_clay, robot_obsidian, robot_geode, 
                                avail_ore - robot_ore_cost + robot_ore, avail_clay + robot_clay, avail_obsidian + robot_obsidian, avail_geode + robot_geode)
                    return max_cost
                elif robot_type == 1 and avail_ore >= robot_clay_cost:
                    for robot_type in range(0, 4):
                        max_cost = dfs(max_cost, time - 1, 
                                robot_type, robot_ore, robot_clay + 1, robot_obsidian, robot_geode, 
                                avail_ore - robot_clay_cost + robot_ore, avail_clay + robot_clay, avail_obsidian + robot_obsidian, avail_geode + robot_geode)
                    return max_cost
                elif robot_type == 2 and avail_ore >= robot_obsidian_cost and avail_clay >= robot_obsidian_cost_clay:
                    for robot_type in range(0, 4):
                        max_cost = dfs(max_cost, time - 1, 
                                robot_type, robot_ore, robot_clay, robot_obsidian + 1, robot_geode, 
                                avail_ore - robot_obsidian_cost + robot_ore, avail_clay - robot_obsidian_cost_clay + robot_clay, avail_obsidian + robot_obsidian, avail_geode + robot_geode)
                    return max_cost
                elif robot_type == 3 and avail_ore >= robot_geode_cost and avail_obsidian >= robot_geode_cost_obsidian:
                    for robot_type in range(0, 4):
                        max_cost = dfs(max_cost, time - 1, 
                                robot_type, robot_ore, robot_clay, robot_obsidian, robot_geode + 1, 
                                avail_ore - robot_geode_cost + robot_ore, avail_clay + robot_clay, avail_obsidian - robot_geode_cost_obsidian + robot_obsidian, avail_geode + robot_geode)
                    return max_cost
                avail_ore, avail_clay, avail_obsidian, avail_geode = avail_ore + robot_ore, avail_clay + robot_clay, avail_obsidian + robot_obsidian, avail_geode + robot_geode
            return max(max_cost, avail_geode)
        max_cost = 0
        for robot_type in range(0, 4):
            max_cost = dfs(max_cost, time, robot_type, 1, 0, 0, 0, 0, 0, 0, 0)
        r = r_func(r, max_cost, n)
    return r

time = 24
o = [(t - 1)*t // 2 for t in range(0, time + 1)]
p = [list(map(int, re.findall("-?\d+", x))) for x in open('input.txt').readlines()]
print(solve(time, o, p, 0, lambda r, m, n: r + m*n))

time = 32
o = [(t - 1)*t // 2 for t in range(0, time + 1)]
print(solve(time, o, p[:3], 1, lambda r, m, n: r * m))
