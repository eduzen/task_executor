# task_executor [![Build Status](https://travis-ci.org/eduzen/task_executor.svg?branch=master)](https://travis-ci.org/eduzen/task_executor)

# Usage

We are using docker and docker-compose. If you already have this two requirements, just run:
```bash
make start

# only test and flake8
make test
````

Exercise:
Given in the code is a queue filled with a number of tasks that need to be executed.
Your job is to write a task executor that goes through each task and executes it.
Each task specifies a target. Think of the target as the entity that is effected by the task.
It should execute all tasks in the fastest time possible, but there are constraints.

1) no more than 3 tasks may be executed in parallel
2) each target (dave for example) can only execute one task at once
3) each type of task has a rate limit specific to it. This number tells you how often this specific task may be executed per second.
4) the tasks for each target must stay in the same order

Use of libraries of all kinds is encouraged! Please use Python 3+

