from abc import ABC, abstractmethod
import json

# POKER_ICONS = ['\U00002662','\U00002664']
POKER_ICONS = ['♢','♧']
# CHESS_ICONS = ['\U00002654','\U00002655']
CHESS_ICONS = ['♔','♕']

class IconStrategy(ABC):
    def __init__(self) -> None:
        self.container_icon = None
        self.leaf_icon = None
    
    @abstractmethod
    def set_icons(self,config_path:str=None,icon_name:str=None) -> None:
        pass

class PokerIconStrategy(IconStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def set_icons(self, config_path: str = None, icon_name: str = None) -> None:
        self.container_icon = POKER_ICONS[0]
        self.leaf_icon = POKER_ICONS[1]

class ChessIconStrategy(IconStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def set_icons(self, config_path: str = None, icon_name: str = None) -> None:
        self.container_icon = CHESS_ICONS[0]
        self.leaf_icon = CHESS_ICONS[1]

class OtherIconStrategy(IconStrategy):
    def __init__(self) -> None:
        super().__init__()
    
    def set_icons(self, config_path: str = None, icon_name: str = None) -> None:
        if config_path is not None:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            try:
                self.container_icon = config[icon_name]["container_icon"]
                self.leaf_icon = config[icon_name]["leaf_icon"]
            except:
                raise ValueError(f"Unknown icon: {icon_name}")
        else:
            raise ValueError(f'Config path missed.')