# bowling

SPARE = '/'
STRIKE = 'X'
MAX_FRAMES = 10


def get_frames_from_expression(roll_sequence):
    """
    >>> get_frames_from_expression("X 45 4/ 32")
    ['X', '45', '4/', '32']
    """
    return roll_sequence.split()


def simple_frame_score(frame):
    """
    >>> simple_frame_score("X")
    10
    >>> simple_frame_score("34")
    7
    >>> simple_frame_score("3/")
    10
    """

    if frame[-1] in (STRIKE, SPARE):
        simple_score = 10
    else:
        simple_score = int(frame[0]) + int(frame[1])
    
    return simple_score


def simple_first_roll_score(frame):
    """
    >>> simple_first_roll_score("X")
    10
    >>> simple_first_roll_score("3/")
    3
    """
    first_roll = frame[0]
    if first_roll == STRIKE:
        return 10
    else:
        return int(first_roll)


def calculate_simple_frame_scores(frames):
    # I would probably have skipped the `if` and done:
    # relevant_frames = frames[:MAX_FRAMES]
    # simple_frame_scores = [simple_frame_score(frame) for frame in relevant_frames]

    simple_frame_scores = [simple_frame_score(frame) for frame in frames]
    if len(frames) > MAX_FRAMES:
            simple_frame_scores.pop()
    return simple_frame_scores


def calculate_simple_score(frames):
    # I would probably have skipped the `if` and done:
    # relevant_frames = frames[:MAX_FRAMES]
    # simple_frame_scores = [simple_frame_score(frame) for frame in relevant_frames]

    simple_frame_scores = [simple_frame_score(frame) for frame in frames]
    simple_score = sum(simple_frame_scores[:MAX_FRAMES])

    return simple_score


def calculate_bonus_points(frames):
    """
    >>> calculate_bonus_points(['X', '45', '4/', '32'])
    12
    >>> calculate_bonus_points(['X', '45', '4/', '32', 'X', '22'])
    16
    """
    bonus_points = 0

    try:
      for index, frame in enumerate(frames):
          if frame == STRIKE:
              bonus_points += simple_frame_score(frames[index+1])
          elif frame[1] == SPARE:
              bonus_points += simple_first_roll_score(frames[index+1])
    except IndexError:
        pass

    return bonus_points


def total_score(frames):
    """
    >>> total_score(['X', '45', '4/', '32'])
    46
    >>> total_score(['X', '45', '4/', '32', 'X', '22'])
    64
    >>> total_score(['X', '11', '11', '11', 'X', '11', '11', '11', '11', 'X', '11'])
    50
    >>> total_score(['X', '11', '11', '11', 'X', '11', '11', '11', '11', '1/', '11'])
    49
    >>> total_score(['X', '11', '11', '11', 'X', '11', '11', '11', '11', '1/', 'X'])
    58
    >>> total_score(['X', '11', '11', '11', 'X', '11', '11', '11', '11', 'X', 'X'])
    58
    """
    simple_score = calculate_simple_score(frames)

    bonus_points = calculate_bonus_points(frames)

    return simple_score + bonus_points    


def score(frames_expression):
    """
    >>> score("X 45 4/ 32")
    46
    """
    frames = get_frames_from_expression(frames_expression)
    
    return total_score(frames)
    

