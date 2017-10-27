def k2c(temp):
    """this is a function that will do stuff and convert things
    
    Parameters
    ----------
    temp: int or float
        temperature value to convert
    
    Returns
    -------
    temp: int or float
         converted temperature
    """
    return temp - 273.15

def f2c(temp):
    tk = f2k(temp)
    c = k2c(tk)
    return(c)

def f2k(temp=32):
    convert = ((temp - 32) * (5/9)) + 273.15
    return convert
