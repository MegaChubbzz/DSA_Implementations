from operator import attrgetter

class Activity:
    def __init__(self, name, initial_start_time, initial_finish_time):
        self.name = name
        self.start_time = initial_start_time
        self.finish_time = initial_finish_time

    def conflicts_with(self, other_activity):
        if self.finish_time <= other_activity.start_time:
            return False
        elif other_activity.finish_time <= self.start_time:
            return False
        else:
            return True
        

def activity_selection(activities):
    chosen_activities = []
    activities.sort(key = attrgetter("finish_time"))
    current = activities[0]
    chosen_activities.append(current)
    for i in range(1, len(activities)):
        if not activities[i].conflicts_with(current):
            chosen_activities.append(activities[i])
            current = activities[i]
    return chosen_activities