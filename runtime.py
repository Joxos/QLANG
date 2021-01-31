class Variable:
    def __init__(self,type,name,value):
        self.type=type
        self.name=name
        self.value=value

class Function:
    def __init__(self,return_type,name,args):
        self.return_type=return_type
        self.name=name
        self.args=args

class Class:
    def __init__(self,class_name):
        self.class_name=class_name
    def add_member(member):
        pass

class Runtime:
    def __init__(self):
        self.variables={}
        self.functions={}
        self.classes={}
    def execute(line):
        pass
    def analysis(line):
        pass
