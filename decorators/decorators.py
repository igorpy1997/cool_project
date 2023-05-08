class UnexpectedTypeException(Exception):
    pass
def expected_type(return_types):
    def dec_func(wrap_function):
        def wrapper(*args, **kwargs):
            result = wrap_function(*args, **kwargs)
            if not isinstance(result, return_types):
                raise UnexpectedTypeException(f"Was expecting instance of: {return_types}")
            """
            f строки 
            raise 
            """
            return result
        return wrapper
    return dec_func






