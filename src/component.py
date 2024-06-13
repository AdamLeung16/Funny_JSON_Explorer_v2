from abc import ABC, abstractmethod
from style import StyleStrategy
from icon import IconStrategy
from iterator import ComponentIterator

class Component(ABC):
    def __init__(self,icon:IconStrategy,key:str,value:str) -> None:
        self.icon = str()
        self.key = key
        self.iter = ComponentIterator()
    
    def draw(self,style:StyleStrategy,prefix:str,max_width:int,is_last:bool) -> list:
        pass

class Container(Component):
    def __init__(self, icon: IconStrategy, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.container_icon
    
    def add(self,component:Component) -> None:
        self.iter.children.append(component)
    
    def draw(self,style,prefix,max_width,is_last) -> list:
        print_list = []
        print_line,next_prefix = style.draw_container(self.icon,self.key,prefix,max_width,is_last)
        print_list+=print_line
        while self.iter.has_next():
            is_last = len(self.iter.children) == 1
            component = self.iter.next()
            print_line = component.draw(style,next_prefix,max_width,is_last)
            print_list+=print_line
        return print_list

class Leaf(Component):
    def __init__(self, icon: IconStrategy, key: str, value: str) -> None:
        super().__init__(icon, key, value)
        self.icon = icon.leaf_icon
        self.value = value
    
    def draw(self,style,prefix,max_width,is_last) -> list:
        print_line,_ = style.draw_leaf(self.icon,self.key,self.value,prefix,max_width,is_last)
        return print_line