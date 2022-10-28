import constants
from point import Point
class Snake():
    """
    A long limbless reptile.
    The responsibility of Snake is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    color = constants.WHITE
    _segments = []
    _direction = None
    def __init__(self, initial_segment_list):
        # initial segment list is a list of points that represents
        # the initial body segment positions
        super().__init__()
        self._segments = initial_segment_list
    def set_direction(self, direction):
        self._direction = direction
    def get_segments(self):
        return self._segments
    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
    def get_head(self):
        return self._segments[0]
    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            segment = Point()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)
    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)