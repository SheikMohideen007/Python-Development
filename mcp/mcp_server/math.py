from mcp.server.fastmcp import FastMCP


math_mcp=FastMCP("Math_server")


@math_mcp.tool()
def addition(numbers:list):
    """
    Function to perform addition of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to be added.
        
    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(numbers)

@math_mcp.tool()
def subtraction(numbers:list):
    """
    Function to perform subtraction of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to be subtracted.
        
    Returns:
        float: The result of subtracting all subsequent numbers from the first number in the list.
    """
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


if __name__=="__main__":
    math_mcp.run(transport="stdio")
