def invariant(fn):
    def invariant_fn(cls, instance):
        return fn(cls, instance)

    return invariant_fn


def param_invariant(fn):
    def param_invariant_fn(cls, instance):
        return fn(cls, instance)

    return param_invariant_fn
