# Import players, collision, snake, constants, and points
from players import player
from collision import collisions
from snake import snake
import constants
from points import point

# Create a collision class
class collision(collisions):
    
    # Allow the snakes to grow their tales
      def _handle_collision(self, cast):
        score = cast.get_move_next("scores1")
        player1 = player.get_move_next("player1")
        player2 = player.get_move_next("player2")
        head = snake.get_head()
        if head.get_position().equals(player1.get_position()):
            points = self.player1.get_points()
            player1.grow_tail(points)
            score.add_points(points)
        score = cast.get_move_next("scores2")
        player2 = cast.get_move_next("player2")
        head = player2.get_head()
        if head.get_position().equals(player2.get_position()):
            points = player2.get_points()
            player2.grow_tail(points)
            score.add_points(points)
    
    # If collision display game over
      def _handle_segment_collision(self, cast):
        player1 = cast.get_move_next("player1 ")
        head = player1.get_segments()[0]
        segments = player1.get_segments()[1:]
        player2 = player.get_move_next("player2 ")
        head2 = player2.get_segments()[0]
        segments2 = player2.get_segments()[1:]
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
    
      def _handle_game_over(self, cast):
        if self._is_game_over:
            player1 = cast.get_move_next("player1")
            segments = player1.get_segments()
            player2 = cast.get_move_next("player2")
            segments = player2.get_segments()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = point(x, y)
            message = player()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_player("messages", message)
            for segment in segments:
                segment.set_color(constants.WHITE)

# Create a collision detection class
class collision_detection(collision):

      def _handle_collision(self, cast):
        score = cast.get_move_next("scores1")
        player1 = player.get_move_next("player1")
        player2 = player.get_move_next("player2")
        head = snake.get_head()
        if head.get_position().equals(player1.get_position()):
            points = self.player1.get_points()
            player1.grow_tail(points)
            score.add_points(points)
        score = cast.get_move_next("scores2")
        player2 = cast.get_move_next("player2")
        head = player2.get_head()
        if head.get_position().equals(player2.get_position()):
            points = player2.get_points()
            player2.grow_tail(points)
            score.add_points(points)

      def _handle_segment_collision(self, cast):
        player1 = cast.get_move_next("player1 ")
        head = player1.get_segments()[0]
        segments = player1.get_segments()[1:]
        player2 = player.get_move_next("player2 ")
        head2 = player2.get_segments()[0]
        segments2 = player2.get_segments()[1:]
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

      def _handle_game_over(self, cast):
        if self._is_game_over:
            player1 = cast.get_move_next("player1")
            segments = player1.get_segments()
            player2 = cast.get_move_next("player2")
            segments = player2.get_segments()
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = point(x, y)
            message = player()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_player("messages", message)
            for segment in segments:
                segment.set_color(constants.WHITE)