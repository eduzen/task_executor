import queue

# fill queue with jobs that should be done to a target
jobs = queue.Queue()
jobs.put((1, "dave", "drink_beer"))
jobs.put((2, "dave", "smoke_cigarette"))
jobs.put((3, "dave", "drink_beer"))
jobs.put((4, "dave", "go_to_toilet"))
jobs.put((5, "dave", "drink_beer"))
jobs.put((6, "cris", "smoke_cigarette"))
jobs.put((7, "cris", "drink_beer"))
jobs.put((8, "cris", "drink_beer"))
jobs.put((9, "cris", "go_to_toilet"))
jobs.put((10, "cris", "smoke_cigarette"))
jobs.put((11, "andi", "drink_beer"))
jobs.put((12, "andi", "smoke_cigarette"))
jobs.put((13, "andi", "drink_beer"))
jobs.put((14, "andi", "go_to_toilet"))
jobs.put((15, "andi", "drink_beer"))
jobs.put((16, "nick", "smoke_cigarette"))
jobs.put((17, "nick", "drink_beer"))
jobs.put((18, "nick", "drink_beer"))
jobs.put((19, "nick", "go_to_toilet"))
jobs.put((20, "nick", "smoke_cigarette"))
jobs.put((21, "phil", "drink_beer"))
jobs.put((22, "phil", "smoke_cigarette"))
jobs.put((23, "phil", "drink_beer"))
jobs.put((24, "phil", "go_to_toilet"))
jobs.put((25, "phil", "drink_beer"))
jobs.put((26, "maxi", "smoke_cigarette"))
jobs.put((27, "maxi", "drink_beer"))
jobs.put((28, "maxi", "drink_beer"))
jobs.put((29, "maxi", "go_to_toilet"))
jobs.put((30, "maxi", "smoke_cigarette"))