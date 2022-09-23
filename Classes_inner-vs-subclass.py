# this script demonstrates the difference in 
# inheritance/composition of sublcasses and inner classes
# it's kind of unhinged, the output is better documentation than the code.

# simplified pseudocode:
#   define some classes with various relationships
#   give each unique attributes  
#   instance each class
#   attempt to access all the unique attributes on every instance
#   change and add some attributes to demonstrate class vs instance data

class OutC:
    foo = f"{'foo':<8}accessed via MyC static variable"
    def __init__(self):
        self.bar = f"{'bar':<8}member of an {type(self).__name__} instance"
        
    class InnC:
        def __init__(self):
            self.quux = f"{'quux':<8}member of an {type(self).__name__} instance"

class SubC(OutC):
    baz = f"{'baz':<8}accessed via SubC static variable"
    def __init__(self):
        self.quuux = f"{'quuux':<8}member of an {type(self).__name__} instance"

def main():
    a = OutC()
    b = a.InnC()
    c = OutC.InnC()
    d = SubC()
    
    def say(r):
        for i, inst in enumerate([a, b, c, d]):
    
            name = f'Object {chr(65+i)}-{r+1}'                              # A-1, D-2, etc
            namespace = '.'.join(str(inst).split( )[0].split('.')[1::])     # Class.Subclass
            mem_addr = str(inst).split(' ')[-1][:-1]                        # memory address
            print(f'{name}\n\tNamespace: {namespace}\n\tAddress: {mem_addr}\n\tAttributes:')

            for attr in ['foo', 'bar', 'baz', 'quux', 'quuux']:
                try:
                    print(f'\t\t{getattr(inst, attr)}')
                except AttributeError as e:
                    # print(f"\t{j}\t{e}") # DEBUG
                    pass
                    
            output = ''
            for j, line in enumerate(comments[i][r]):
                output = f'{output}# {line}'
                if j < len(comments[i][r]) -1:
                    output = f'{output}\n\t'
            if len(output) > 0:
                output = f'\t{output}'
            if len(output) > 1: print(f'{output}')

    for i in range(2):
        if i > 0:
            b.foo = f'{"foo":<8}added for InnC B'
            d.foo = f'{"foo":<8}overloaded for SubC D'
            print(f'\nEND 1/2\n\t{b.foo}\n\t{d.foo}\nSTART 2/2\n')
        say(i)

comments = (
    (  #A
        ("A Class in the module namespace.","It carries a reference to its inner class, but not that class's members."),()
    ),(#B
        (
            "This Inner Class  has been instantiated from a reference to object A.",
            "It has none of the elements of the Outer Class.",
            "It's type is defined within the Outer Class namespace"
        ),(
            "Object B now has a member called 'foo' that it was not initialized with.",
            "This is not a static class variable.",
            "It is completely unrelated to 'foo' member in the outer class's namespace.",
            "If this were not the case, A-2 above would be modified.")
    ),(#C
        (
            "This object is instanced without reference to A, only reference to the Outer Class.",
            "It is a seperate instance from B, there is no functional difference.",
            "Note that it has a seperate memory location from B."),
        ("Object C is unchanged.","The changes to B applied only to that instance in memory.")
    ),(#D
        ("An instance of a subclass.", "It is instanced with the static member 'foo' of its base class."),
        ("D-2 has a NEW non-static member variable","This overrides the inherited definition of 'foo'")),
)

main()
