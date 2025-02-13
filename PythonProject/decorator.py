def function(fun):
    def innerFunction(*args, **kwargs):
        result= fun(*args, **kwargs)
        return result