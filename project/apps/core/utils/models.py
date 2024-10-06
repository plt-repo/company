from functools import wraps

from django.core.cache import cache


def redis_cached_property(ttl: int):
    """
    Декоратор который кэширует результаты model property в redis.
    :param ttl: Время жизни(в секундах)
    :return:
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            redis_key = f"{args[0].__class__.__name__}_{args[0].pk}_{f.__name__}"
            redis_value = cache.get(redis_key)
            if redis_value is not None:
                return redis_value

            result = f(*args, **kwargs)
            cache.set(redis_key, result, ttl)

            return result
        return wrapper
    return decorator
