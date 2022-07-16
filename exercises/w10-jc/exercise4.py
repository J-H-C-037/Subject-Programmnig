"""Define a function that returns a tuple simulating the behaviour of the function
range(start,stop,step), which returns a sequence of numbers between the given start
integer to the stop integer incremented by the given step integer. Configure the function with
optional parameters so it also works to simulate functions range(start, stop) and
range(stop). You must check that the types of the parameters are correct (int) and that
their range is also correct. If not an empty tuple will be returned."""


def range_1(stop: int, start = 0, step=1):
    if start != 0:
        m = stop
        stop = start
        start = m
    if type(start) != int or type(stop) != int or type(step) != int:
        return tuple()
    if step > 0:
        if start > stop:
            return tuple()
    elif step < 0:
        if start < stop:
            return tuple()

    l1 = []

    for i in range(((stop - start) // step)):
        l1.append(start)

        start += step

    if (stop / start) % step != 0:
        l1.append(start)
    return l1
