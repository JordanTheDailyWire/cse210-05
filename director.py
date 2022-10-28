#from script import Script
class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """
    _video_service = None
    player1_score = 0
    player2_score = 0
    #initiates the game and the first action taking place 
    # makes sure all things are being added to the video_service too.
    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service 

    def start_game(self, players, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self.execute("input", players, script)
            self.execute("update", players, script)
            self.execute("output", players, script)
        self._video_service.close_window()

    def execute(self, execute_type, players, script):
        """Calls execute for each players script.
        
        Args:
            Players (player_1 or player_2): The action group name.
            script (Script): The script off additions and text display
            for the contestants progress or defeat.
        """