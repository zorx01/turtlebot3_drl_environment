from ..common.settings import REWARD_FUNCTION, COLLISION_OBSTACLE, COLLISION_WALL, TUMBLE, SUCCESS, TIMEOUT, RESULTS_NUM

goal_dist_initial = 0

reward_function_internal = None

def get_reward(succeed, action_linear, action_angular, distance_to_goal, goal_angle, min_obstacle_distance):
    return reward_function_internal(succeed, action_linear, action_angular, distance_to_goal, goal_angle, min_obstacle_distance)

def get_reward_A(succeed, action_linear, action_angular, distance_moved, goal_angle, min_obstacle_dist):
        # [-3.14, 0]
        r_yaw = -1 * abs(goal_angle)

        # [-4, 0]
        r_vangular = -1 * (action_angular**2)

        # [-1, 1]
        r_distance = 100*distance_moved

        # print("\nr_distance :",r_distance)
        # print("r_vangular :",r_vangular)
        # print("r_yaw :",r_yaw)
        
        
        # [-20, 0]
        if min_obstacle_dist < 0.22:
            r_obstacle = -30
        else:
            r_obstacle = 0

        # print("r_obstacle :",r_obstacle)

        # [-2 * (2.2^2), 0]
        # r_vlinear = -1 * (((0.22 - action_linear) * 10) ** 2)

        r_vlinear = -75 * ((0.22 - action_linear)**2)

        

        # print("r_vlinear :",r_vlinear)
        # print("r_vlinear new :",r_vlinear1)
        # print("Difference :",r_vlinear-r_vlinear1)

        

        reward = r_yaw + r_distance + r_obstacle + r_vlinear + r_vangular - 1

        # print("Total R :",reward,"\n")

        if succeed == SUCCESS:
            reward += 2500
        elif succeed == COLLISION_OBSTACLE or succeed == COLLISION_WALL:
            reward -= 2000
        return float(reward)

# Define your own reward function by defining a new function: 'get_reward_X'
# Replace X with your reward function name and configure it in settings.py

def reward_initalize(init_distance_to_goal):
    global goal_dist_initial
    goal_dist_initial = init_distance_to_goal

function_name = "get_reward_" + REWARD_FUNCTION
reward_function_internal = globals()[function_name]
if reward_function_internal == None:
    quit(f"Error: reward function {function_name} does not exist")