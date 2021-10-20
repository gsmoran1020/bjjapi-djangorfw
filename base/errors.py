
class BjjErrors:
    TYPE = {
        "Type Error": "Invalid Technique Type.", 
        "Valid Options": ['choke', 'sweep', 'escape', 'joint_lock', 'takedown', 'mixed']
    }

    DIFFICULTY = {
        "Difficulty Error": "Invalid Difficulty Type.",
        "Valid Options": ['easy', 'intermediate', 'advanced']
    }

    ID = {
        "ID Error": "A Technique with that ID does not exist."
    }

    NAME = {
        "Name Error": "A Technique with that name does not exist."
    }

    SAVE_FAIL = {
        "Error": "Technique saved unsuccessfully. Ensure that all fields are properly filled."
    }