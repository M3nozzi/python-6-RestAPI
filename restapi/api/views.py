

from collections import Counter
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')
    
    counter = Counter()
    for num in request_data:
        counter[num] += 1

    solution = []

    for i in counter.most_common():
        for _ in range(i[1]):
            solution.append(i[0])
    print(solution)

    return Response({'solution': solution})