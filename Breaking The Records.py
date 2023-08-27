scores = [12, 24, 10, 24]

def breakingRecords(scores):
    # Write your code here
    break_most = break_least = 0
    record = record_max = record_min = scores[0]
    for item in scores[1:]:
        if item > record_max:
            record_max = item
            break_most += 1
        elif item < record_min:
            record_min = item
            break_least += 1
        else:
            continue
        
    records = []
    records.append(break_most)
    records.append(break_least)
        
    return records

print(breakingRecords(scores))