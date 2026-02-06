import math
import logging

logging.basicConfig(
    filename='app.log',
    filemode= 'w',
    format='%(levelname)s:%(name)s:%(message)s',
    level=logging.DEBUG
)


def findingTangent(sin_alpha, cos_alpha):
    if sin_alpha is not None:
        logging.info(f'A value has been entered sin(alpha) = {sin_alpha}')
    if cos_alpha is not None:
        logging.info(f'A value has been entered cos(alpha) = {cos_alpha}')
    try:
        result = sin_alpha / cos_alpha
        logging.debug(f'The value of the tangent of the angle alpha is found = {result}')
    except ZeroDivisionError:
        logging.warning('The cosine of the angle alpha = 0. The tangent is not defined.')
    except (TypeError, ValueError):
        logging.critical('The tangent of the angle alpha is not defined.')

findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)

#INFO:root:A value has been entered sin(alpha) = 0.5
#INFO:root:A value has been entered cos(alpha) = 0.8660254037844386
#DEBUG:root:The value of the tangent of the angle alpha is found = 0.5773502691896258
#INFO:root:A value has been entered sin(alpha) = 0.5
#INFO:root:A value has been entered cos(alpha) = w
#CRITICAL:root:The tangent of the angle alpha is not defined.
#INFO:root:A value has been entered sin(alpha) = 0.5
#INFO:root:A value has been entered cos(alpha) = 0
#WARNING:root:The cosine of the angle alpha = 0. The tangent is not defined.