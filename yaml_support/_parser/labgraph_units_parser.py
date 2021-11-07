import builtins
from .base_parser import BaseParser
from typed_ast.ast3 import NodeVisitor, ClassDef, Module, FunctionDef, Name, Assign, AnnAssign, Attribute
from model.class_model import ClassModel
from typing import TypeVar, Generic, List
from os import chdir, system


T = TypeVar("T")


class LabGraphUnitsParser(BaseParser, NodeVisitor, Generic[T]):
    """
    Parses the LabGraph classes
    """

    def __init__(self, element_type: T = ClassModel):
        super().__init__()
        self.classes: List[element_type] = []

    def parse(self, tree):
        self.visit(tree)

    def visit_Module(self, node):
        assert isinstance(node, Module)

        for child in node.body:
            self.visit(child)

    def visit_ClassDef(self, node):

        assert isinstance(node, ClassDef)
       
        # checks if the class is a LabGraph Unit.
        # a class is a Labgraph unit if it inherents from LabGraph unit :
        #  Message, Config, State, Node, Group,  Graph
        if node.bases and node.bases[0].attr in ('Message','Config','State','Node','Group','Graph'):
            
            class_model = ClassModel(node.name, node.bases[0].attr)
            
            for child in node.body:
                
                # case of members defined using annotation
                if isinstance(child,AnnAssign):
                    
                    # member name & type
                    name:str = child.target.id
                    type:str = ''
                    

                    if(hasattr(child.annotation,'id')):
                        type = child.annotation.id
                    
                    elif(hasattr(child.annotation,'value')):

                        type = self.__construct_member_type(child.annotation,type)
                        

                    class_model.members.append({
                        "name":name,
                        "type":type
                    })
                

                # case of a class member defined using assign operator
                elif isinstance(child,Assign):
                    
                    class_model.members.append({
                        "name":child.targets[0].id,
                        "type":child.value.args[0].id
                    })


                # case of a class method
                elif isinstance(child, FunctionDef):

                    # argument type
                    arguments_info = list()

                    for arg in child.args.args:
                        if arg.arg == "self":
                            continue

                        argument_info = ""
                        argument_info += arg.arg
                        
                        if arg.annotation is not None:
                            argument_info += f": {arg.annotation.id}"

                        elif arg.type_comment is not None:
                            argument_info += f": {arg.type_comment}"

                        arguments_info.append(argument_info)

                    # return type
                    return_info = ""

                    if isinstance(child.returns, Name):
                        return_info = f": {child.returns.id}"

                    elif child.type_comment is not None:
                        return_info = f": {child.type_comment}"

                        
                    class_model.methods.append({
                        "name":child.name,
                        "args":arguments_info,
                        "return":return_info
                    })
                    
        
            assert isinstance(class_model, ClassModel)
            self.classes.append(class_model)

 
       
    def __construct_member_type(self,value,type):
        
        if(hasattr(value,'attr')):
            type = f"{self.__construct_member_type(value.value,type)}.{value.attr}"
        
        elif(hasattr(value,'id')):
            return value.id

        elif(hasattr(value,'slice')):
            type =  f"{self.__construct_member_type(value.value,type)}.{self.__construct_member_type(value.slice,type)}{f'.{type}' if type else ''}"                   
                    
        
        elif(hasattr(value,'value')):
            type = f"{self.__construct_member_type(value.value,type)}{f'.{type}' if type else ''}"

        return type
        

    