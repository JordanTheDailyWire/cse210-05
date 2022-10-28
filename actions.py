# Import execution, and players
from execution import execution
from players import players

# Create a action class and draw all players
class actions(execution):
    def __init__(self, video_service):
        self._video_service = video_service

    # Create an execution function
    def execute(self, cast, script):
        score = players.get_move_next("scores")
        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()
        messages = cast.get_actors("messages")
        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()