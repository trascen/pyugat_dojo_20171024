

def score(game):
    def score_for_roll(prev, roll):
        if roll == 'X': return 10
        if roll == '/': return 10 - int(prev)
        return int(roll)
    
    def frame_scorer(frame, prev_in_frame, roll):
        res = []

        if roll == 'X':
            res += [lambda r: strike_bonus_scorer(r)]
        elif roll == '/':
            res += [lambda r: spare_bonus_scorer(roll, r)]

        new_frame = roll == 'X' or roll == '/' or prev_in_frame is not None

        if frame < 10 or not new_frame:
            res += [lambda r: frame_scorer(frame+new_frame, None if new_frame else roll, r)]

        return score_for_roll(prev_in_frame, roll), res

    def strike_bonus_scorer(roll):
        return score_for_roll(None, roll), [lambda r: spare_bonus_scorer(roll, r)]

    def spare_bonus_scorer(prev, roll):
        return score_for_roll(prev, roll), []

    total = 0
    processors = [lambda r: frame_scorer(1, None, r)]

    for roll in game:
        scores, new_procs = zip(*[p(roll) for p in processors])
        total += sum(scores)
        processors = sum([n for n in new_procs],  [])

    if len(processors) != 0:
        raise ValueError

    return total
