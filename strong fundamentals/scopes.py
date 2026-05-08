# Local Scope: Variables defined within a function are local to that function and cannot be accessed outside of it.
# Nonlocal Scope: Variables defined in the nearest enclosing scope that is not global. They can be accessed and modified within nested functions.
# Global Scope: Variables defined at the top level of a script or module are global and can be accessed from anywhere in the code.
class ScopeDemo:
    str="Sample to check on __dict__"
    def scopes():
        var="Top Function Scope"
        def localScope():
            var="Local Scope"

        def nonlocalScope():
            nonlocal var
            var="Nonlocal Scope"

        def globalScope():
            global var
            var="Global Scope"
        print(var) # Top Function Scope
        localScope()            
        print(var) # Top Function Scope
        nonlocalScope()
        print(var) # Nonlocal Scope
        globalScope()
        print(var) # Nonlocal Scope

    scopes()
    print(var) # Global Scope

print(ScopeDemo.__dict__) # this will show the attributes of the ScopeDemo class, including the scopes method and any variables defined within it.
