
from joernInterface.indexLookup.FunctionLookup import FunctionLookup

"""
Selection of functions based on different criteria,
e.g., symbol usage
"""

class FunctionSelector:

    # FIXME: introduce functions that only retrieve symbol
    # nodes and not entire nodes as that will greatly
    # improve performance
    SymbolUsersDict=dict()
    """
    Determine functions using the same symbol as the
    function of interest
    """
    #def selectFunctionsUsingSymbol(self, symbol):
        #if symbol.target_type == 'Parameter':
            #if symbol not in FunctionSelector.SymbolUsersDict:
                #FunctionSelector.SymbolUsersDict[symbol]= FunctionLookup.lookup_functions_by_parameter(
                    #symbol.target_name,
                    #symbol.target_decl_type)
            #functions=FunctionSelector.SymbolUsersDict[symbol]
        #elif symbol.target_type == 'Variable':
            #if symbol not in FunctionSelector.SymbolUsersDict:
                #FunctionSelector.SymbolUsersDict[symbol]= FunctionLookup.lookup_functions_by_variable(
                    #symbol.target_name,
                    #symbol.target_decl_type)
            #functions=FunctionSelector.SymbolUsersDict[symbol]
        #elif symbol.target_type == 'Callee':
            #if symbol.target_name not in FunctionSelector.SymbolUsersDict:
                #FunctionSelector.SymbolUsersDict[symbol.target_name]= FunctionLookup.lookup_functions_by_callee(
                    #symbol.target_name)
            #functions=FunctionSelector.SymbolUsersDict[symbol.target_name]
        #return functions
    def selectFunctionsUsingSymbol(self, symbol):
        if symbol in FunctionSelector.SymbolUsersDict:
            return FunctionSelector.SymbolUsersDict[symbol]
        if symbol.target_type == 'Parameter':
            functions=FunctionLookup.lookup_functions_by_parameter(
                    symbol.target_name,
                    symbol.target_decl_type)
        elif symbol.target_type == 'Variable':
            functions=FunctionLookup.lookup_functions_by_variable(
                    symbol.target_name,
                    symbol.target_decl_type)
        elif symbol.target_type == 'Callee':
            functions=FunctionLookup.lookup_functions_by_callee(
                    symbol.target_name)
        FunctionSelector.SymbolUsersDict[symbol]=functions
        return functions
    def selectAllFunctions(self):
        functions = FunctionLookup.lookup_all_functions()
        return functions