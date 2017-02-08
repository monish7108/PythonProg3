def tag_wrap(tag):
    print(tag)
    def decorator(fn):
        print(fn,"\t",type(fn))
        def inner(s):
            print(s)
            return '<%s>%s</%s>' % ( tag,fn(s),tag)

        return inner

    return decorator


#@tag_wrap('b')
@tag_wrap('em')
def greet(name):
    return 'Hello, %s!' % name
greet('world')
print(type(greet))