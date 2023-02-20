#plan merging protocol

class plan:
          def __init__(self, start_time, end_time, location, details):
                    
                    self.start_time = start_time
                    self.end_time = end_time
                    self.location = location
                    self.details = details


def merge_plans(plan1, plan2):
              start_time = min(plan1.self.start_time, plan2.start_time)
              end_time = max(plan1.end_time, plan2.end_time)
              location = plan1.location + " and " + plan2.location 
              details = plan1.details + "\n" + plan2.details
              return plan(start_time, end_time, location, details)


def merge_overlapping_plans(plans):
          plans.sort(key=lambda x: x.start_time)
          merged_plans = []
          current_plan = plans[0]
          for plan in plans[1:]:
                    if plan.start_time <= current_plan.end_time:
                              current_plan = merge_plans(current_plan, plan)
                    else:
                              merged_plans.append(current_plan)
                              current_plan = plan 
          merged_plans.append(current_plan)
          return merged_plans


plan1 = plan("9:00","10:30","office","meeting with boss")
plan2 = plan("10:00","11:30","coffee shop","meeting with client")
plan3 = plan("12:00", "13:30","office","Lunch break")

plans = [plan1,plan2,plan3]
merged_plans = merge_overlapping_plans(plans)


for plan in merged_plans:
          print(plan.start_time,plan.end_time,plan.location,plan.details)



