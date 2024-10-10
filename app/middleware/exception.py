def exception_message(e):
    """ Define the format of exception message
    Args:
        e (Exception) : An Exception
    Returns:
        str : message
    """
    return f"Exception[{type(e).__name__}] occurred. Details: {str(e)}"