from task_manager.tasks import drink_beer, smoke_cigarette, go_to_toilet

# link task names to functions and rate limiting information

task_config = {
    "drink_beer": {
        "func": drink_beer,
        "rate_limit": 5,  # how often may this task be executed per second
    },
    "smoke_cigarette": {
        "func": smoke_cigarette,
        "rate_limit": 3,  # how often may this task be executed per second
    },
    "go_to_toilet": {
        "func": go_to_toilet,
        "rate_limit": 2,  # how often may this task be executed per second
    },
}
