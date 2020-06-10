import numpy as np
import json

def main(event, context):
    a = np.arange(15).reshape(3,5)
    body = {'ndim': a.ndim}
    return {"statusCode": 200, "body": json.dumps(body)}

if __name__ == '__main__':
    main("","")